# SiH4/H2 PECVD gas-phase chemistry

**Citation:** Sushkov, V., Rachdi, L., and Hofmann, M., “A plasma chemistry model for H2/SiH4 mixtures used in PECVD processes,” *Physica Scripta* 98 (2023), 055614. DOI [10.1088/1402-4896/acc140](https://doi.org/10.1088/1402-4896/acc140). The version of record is explicitly licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

```bibtex
@article{Sushkov2023SiH4H2PECVD,
  author = {Sushkov, Vladimir and Rachdi, Lazhar and Hofmann, Marc},
  title = {A plasma chemistry model for H2/SiH4 mixtures used in PECVD processes},
  journal = {Physica Scripta}, year = {2023}, volume = {98}, number = {5}, pages = {055614},
  doi = {10.1088/1402-4896/acc140}
}
```

The paper describes a 20-species model over 0.1–1.5 Torr and 300–700 K. `heavy_reactions.csv` transcribes its 29 heavy-particle reactions. `chem.yaml` includes 26 reactions with ordinary Arrhenius rate laws; source R24, R26, and R27 are pressure-dependent and remain only in the CSV because a single ordinary Arrhenius expression would lose their pressure dependence. Source pre-exponentials are normalized from `(T/298)^b` and molecule-based cm3/s to Cantera molar units; source activation factors `exp(-E/T)` are converted to cal/mol using `R`.
