# Semiconductor plasma chemistry

Curated, source-attributed gas-phase and surface data for semiconductor processes. The two gas-phase Cantera files are **kinetics-only** transcriptions with ideal-gas phases and species compositions; they omit thermodynamic property fits, energy distributions, reactor/source terms, and surface boundary models. The separate GPL-licensed ViennaChem files provide surface submodels, not Cantera mechanisms.

| Set | Scope | Cantera species/reactions | Other source data |
|---|---|---:|---|
| [Ar/O2 atmospheric DBD](ArO2_DBD_atmospheric/README.md) | Ar with ≤1% O2, atmospheric DBD and post-discharge; thermal/excited-state gas chemistry | 9 / 28 | 31-row source reaction inventory, including excluded source and wall terms |
| [SiH4/H2 PECVD](SiH4_H2_PECVD_2023/README.md) | 0.1–1.5 Torr, 300–700 K, gas-phase silane/hydrogen chemistry | 21 / 26 | 29 heavy reaction rows; 19 electron-impact equations (rates unavailable in article) |
| [Silane LPCVD, GaAs MOVPE, SF6/O2 silicon etch](ViennaChem_GPL/README.md) | Surface submodels for semiconductor deposition and plasma etching | ViennaChem native format | 3 GPL-licensed source mechanisms; see local license and native-loader test |

## Source pointers (not redistributed)

| Source | Why it is a pointer |
|---|---|
| Lieberman & Lichtenberg, *Principles of Plasma Discharges and Materials Processing*, 2nd ed. (2005), and Lee & Lieberman, “Global model of Ar, O2, Cl2, and Ar/O2 discharges,” J. Vac. Sci. Technol. A 13, 368 (1995), DOI [10.1116/1.579366](https://doi.org/10.1116/1.579366). Report: [ERL-94-49](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1994/Archive/ERL-94-49.pdf). | Report states “All rights reserved” and restricts redistribution; source pointer only. |
| Gudmundsson & Thorsteinsson, “Oxygen discharges diluted with argon: dissociation processes,” Plasma Sources Sci. Technol. 16 (2007), DOI [10.1088/0963-0252/16/2/025](https://doi.org/10.1088/0963-0252/16/2/025). | No explicit redistribution licence verified; pointer only. |
| LXCat cross sections, [redistribution policy](https://master.lxcat.net/instructions/redistribution.php). | Data contributors retain ownership; the policy directs users to LXCat rather than authorizing third-party republication. |
| Quantemol-DB. | Commercial database; no data copied. |
| Published SiH4/NH3/N2, TEOS/O2, CF4/O2, Cl2/Ar, and surface-reaction datasets. | Candidate literature was not included absent an explicit redistribution basis and complete, reusable numerical data. |

## Loader checks

Run the ViennaChem-native test with ViennaChem installed at the pinned upstream commit (it needs SymPy and PyYAML):

```sh
python3 test_viennachem_mechanisms.py
```

This checks native compilation and element balance for each surface reaction. These three files are not Cantera YAML.


Run from this directory with Cantera installed:

```sh
python3 test_mechanisms.py
```

The script loads each YAML and checks every reaction for elemental and charge balance. No Arrhenius.jl compatibility is claimed; its plasma/native reader support was not established in this task.
