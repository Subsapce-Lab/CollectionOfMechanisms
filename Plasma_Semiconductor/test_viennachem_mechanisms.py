#!/usr/bin/env python3
"""Compile copied ViennaChem surface mechanisms and check atom balance."""
from collections import Counter
from pathlib import Path
import re
import viennachem as vc
import yaml
root = Path(__file__).resolve().parent / "ViennaChem_GPL"
expected = {
    "silane.yaml": (5, 3, 3),
    "gaas_cvd.yaml": (24, 26, 30),
    "sf6o2.yaml": (9, 7, 7),
}
def atoms_for(species, definition):
    if definition.get("phase") == "ion":
        return Counter()  # energetic projectile; ViennaChem treats it as a flux/yield
    if "atoms" in definition:
        return Counter(definition["atoms"])
    formula = species[:-1] if species.endswith("*") else species
    tokens = list(re.finditer(r"([A-Z][a-z]?)([0-9]*)", formula))
    if not tokens or "".join(m.group(0) for m in tokens) != formula:
        raise AssertionError(f"No element formula for {species}; declare atoms explicitly")
    return Counter({m.group(1): int(m.group(2) or "1") for m in tokens})
def side_atoms(text, species):
    total = Counter()
    for term in text.split(" + "):
        m = re.fullmatch(r"(\d+)?\s*(.+)", term.strip())
        count, name = int(m.group(1) or "1"), m.group(2)
        if name not in species:
            raise AssertionError(f"Unknown species {name}")
        for element, amount in atoms_for(name, species[name]).items():
            total[element] += count * amount
    return total
for filename, expected_counts in expected.items():
    path = root / filename
    original = yaml.safe_load(path.read_text())
    compiled = vc.from_file(str(path))
    observed = (len(original["species"]), len(original["surface"]), len(compiled["reactions"]))
    if observed != expected_counts:
        raise AssertionError(f"{filename}: expected {expected_counts}, got {observed}")
    for row, reaction in enumerate(original["surface"], 1):
        equation = reaction["eq"]
        arrow = "<->" if "<->" in equation else "->"
        left, right = equation.split(arrow)
        delta = side_atoms(left, original["species"])
        for element, count in side_atoms(right, original["species"]).items():
            delta[element] -= count
        bad = {e: n for e, n in delta.items() if n}
        if bad:
            raise AssertionError(f"{filename} surface row {row}: atom imbalance {bad}")
    print(f"{filename}: {observed[0]} species, {observed[1]} source rows, {observed[2]} compiled rates; balanced")
