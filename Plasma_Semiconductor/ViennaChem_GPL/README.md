# GPL-licensed surface chemistry mechanisms

These three native ViennaChem surface-mechanism input files are copied verbatim from [ViennaChem](https://github.com/ViennaTools/ViennaChem), commit [`6d64b409c0af3487a7040919cfcfc3eaee35550d`](https://github.com/ViennaTools/ViennaChem/tree/6d64b409c0af3487a7040919cfcfc3eaee35550d). ViennaChem is licensed GPL-3.0-or-later; its complete license is included here. The copied files remain under that license. The repository root MIT license does not replace these terms.

| File | Scope and input counts | Literature/source |
|---|---|---|
| `silane.yaml` | SiH4 silicon LPCVD surface growth; 5 species and 3 surface reactions | ViennaChem’s source file and its GPL-licensed, hand-written ViennaPS reference implementation. The upstream file has no separate DOI citation. This is a surface-only test chemistry; gas-phase kinetics are absent. |
| `gaas_cvd.yaml` | Trimethylgallium/arsine GaAs MOVPE (110) surface chemistry; 24 species, 26 surface rows; compiler expands reversible steps to 30 directional rates | Mountziaris, T. J., and Jensen, K. F., “Gas-phase and surface reaction mechanisms in MOCVD of GaAs with trimethyl-gallium and arsine,” *Journal of The Electrochemical Society* 138(8) (1991), 2426–2439. DOI [10.1149/1.2085990](https://doi.org/10.1149/1.2085990). The native file contains only the surface subsystem; the paper’s gas-phase chemistry is not included. |
| `sf6o2.yaml` | SF6/O2 silicon etch surface model; 9 species and 7 surface reactions | Belen, R. J., Gomez, S., Cooperberg, D., Kiehlbauch, M., and Aydil, E. S., “Feature-scale model of Si etching in SF6/O2 plasma and comparison with experiments,” *Journal of Vacuum Science & Technology A* 23(5) (2005), 1430–1439. DOI [10.1116/1.2013317](https://doi.org/10.1116/1.2013317). ViennaPS model defaults are transcribed; no gas-phase plasma chemistry is included. |

```bibtex
@article{Mountziaris1991GaAsMOCVD,
  author = {Mountziaris, Triantafillos J. and Jensen, Klavs F.},
  title = {Gas-phase and surface reaction mechanisms in MOCVD of GaAs with trimethyl-gallium and arsine},
  journal = {Journal of The Electrochemical Society},
  year = {1991}, volume = {138}, number = {8}, pages = {2426--2439},
  doi = {10.1149/1.2085990}
}

@article{Belen2005SF6O2Etching,
  author = {Belen, Rodolfo Jun and Gomez, Sergi and Cooperberg, David and Kiehlbauch, Mark and Aydil, Eray S.},
  title = {Feature-scale model of Si etching in SF6/O2 plasma and comparison with experiments},
  journal = {Journal of Vacuum Science and Technology A},
  year = {2005}, volume = {23}, number = {5}, pages = {1430--1439},
  doi = {10.1116/1.2013317}
}

@software{Filipovic2026ViennaChem,
  author = {Filipovic, Lado}, title = {ViennaChem: Surface-kinetics mechanisms derived from chemical reaction equations},
  year = {2026}, version = {6d64b409c0af3487a7040919cfcfc3eaee35550d},
  url = {https://github.com/ViennaTools/ViennaChem/tree/6d64b409c0af3487a7040919cfcfc3eaee35550d}
}
```

These YAML files are **not Cantera YAML**. They use ViennaChem’s surface syntax for gas/surface/solid phases, incident fluxes, sticking, site balance, and ion-enhanced yields. `test_viennachem_mechanisms.py` invokes the native ViennaChem compiler and checks the three files' species, source-row, and compiled-rate counts. It requires the ViennaChem package (SymPy and PyYAML).
