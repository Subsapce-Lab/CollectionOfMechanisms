#!/usr/bin/env python3
"""Load curated kinetics files; verify inventories and elemental/charge balance."""
from pathlib import Path
import csv
import cantera as ct
root = Path(__file__).resolve().parent
expected = {
    "ArO2_DBD_atmospheric": (31, None, 28),
    "SiH4_H2_PECVD_2023": (29, 19, 26),
}
for name, (heavy_rows, electron_rows, active_reactions) in expected.items():
    folder = root / name
    gas = ct.Solution(str(folder / "chem.yaml"))
    if gas.n_reactions != active_reactions:
        raise AssertionError(f"{name}: expected {active_reactions} YAML reactions, got {gas.n_reactions}")
    for i, reaction in enumerate(gas.reactions(), 1):
        delta = {e: 0.0 for e in gas.element_names}
        charge = 0.0
        for species, coefficient in reaction.products.items():
            sp = gas.species(species)
            for e, count in sp.composition.items():
                delta[e] += coefficient * count
            charge += coefficient * sp.charge
        for species, coefficient in reaction.reactants.items():
            sp = gas.species(species)
            for e, count in sp.composition.items():
                delta[e] -= coefficient * count
            charge -= coefficient * sp.charge
        bad = {e: v for e, v in delta.items() if abs(v) > 1e-12}
        if bad or abs(charge) > 1e-12:
            raise AssertionError(f"{name} reaction {i}: atoms={bad}, charge={charge}")
    heavy = folder / ("reactions.csv" if name.startswith("ArO2") else "heavy_reactions.csv")
    heavy_count = sum(1 for _ in csv.DictReader(heavy.open(newline="")))
    if heavy_count != heavy_rows:
        raise AssertionError(f"{name}: expected {heavy_rows} source heavy reactions, got {heavy_count}")
    if electron_rows is not None:
        e_count = sum(1 for _ in csv.DictReader((folder / "electron_processes.csv").open(newline="")))
        if e_count != electron_rows:
            raise AssertionError(f"{name}: expected {electron_rows} electron reactions, got {e_count}")
    print(f"{name}: {gas.n_species} species, {gas.n_reactions} YAML reactions; {heavy_count} source reaction rows; balanced")
