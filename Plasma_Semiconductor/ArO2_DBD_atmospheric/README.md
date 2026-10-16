# Ar/O2 atmospheric DBD and post-discharge subset

**Citation:** Klages, Claus-Peter; Bröcker, Lars; Betz, Meret Leonie; and Raev, Vitaly, “Atomic-Oxygen Number Densities in Ar-O2 DBDs and Post-discharges with Small Initial O2 Fractions: Plug-Flow Model and Experiments,” *Plasma Chemistry and Plasma Processing* 43 (2023), 285–314. DOI [10.1007/s11090-022-10293-9](https://doi.org/10.1007/s11090-022-10293-9). The version of record is explicitly licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

```bibtex
@article{Klages2023ArO2DBD,
  author = {Klages, Claus-Peter and Bröcker, Lars and Betz, Meret Leonie and Raev, Vitaly},
  title = {Atomic-Oxygen Number Densities in Ar-O2 DBDs and Post-discharges with Small Initial O2 Fractions: Plug-Flow Model and Experiments},
  journal = {Plasma Chemistry and Plasma Processing},
  year = {2023}, volume = {43}, pages = {285--314},
  doi = {10.1007/s11090-022-10293-9}
}
```

`chem.yaml` is an original transcription/conversion of 28 gas-phase Table 2 reactions (source R2–R10, R12–R13, R15–R31) into Cantera elementary and three-body Arrhenius form. The source rates are in molecule-based cm units; the Cantera pre-exponential factors are converted to molar concentration units, including normalization of source `(T/300)^b` factors. Temperature dependencies are transcribed with `T` in kelvin. State definitions contain compositions only, not thermodynamic fits.

`reactions.csv` records the full 31-reaction source table. Source R1, R11, and R14 are omitted from the Cantera subset: R1 is a power/volume source, R11 has condition-dependent mixed-product branching, and R14 is wall/geometry-dependent. Photon products are omitted from R28, R29, and R31, while the gas-phase species balance is retained. The paper says Ar is the only third body considered at O2 fractions up to 1%; R12 uses Ar-only efficiency. O* pools several excited O states as in the source footnote. This is a limited afterglow/DBD chemistry set, not a generic CCP/global discharge model. No electron-impact cross sections, complete reactor model, or surface chemistry are included.
