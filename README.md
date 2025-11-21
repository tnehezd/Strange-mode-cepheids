# Scripts for "Stranger Things: A Grid-based Survey of Strange Modes in Post-Main Sequence Models"


This repository contains the Python scripts used to generate the models and data presented in "Stranger Things: A Grid-based Survey of Strange Modes in Post-Main Sequence Models" (Tarczay-Nehéz et al., 2026). The scripts automate the creation of MESA input directories for a grid of stellar masses and metallicities, including overshoot prescriptions and inlist configurations.


> ⚠️ **Important compatibility note**  
> These scripts have been tested and are known to work with:  
> - **MESA version 23.05.1**  
> - **GYRE version 7.0**  
>  
> Other versions may lead to unexpected behavior or incompatibilities.



## Contents

* **generate_dirs** – this includes the grid generating pys.
* **include/** – this direcotry contains surce files for the current runs.


## Usage

1. To recreate your grid of *MESA* runs, clone the repository:

```bash:
git clone https://github.com/username/Strange-mode-cepheids.git
cd Strange-mode-cepheids
```

2. Run the script:

```bash:
cd generata_dirs
python initialize_low_grid
```
... or the script you need.




## Citation

In case you use these scripts, please cite the associated paper:

```bibtex
@article{TarczayNehez2026,
  author  = {Tarczay-Nehéz, D. and Coauthors},
  title   = {Stranger Things: A Grid-based Survey of Strange Modes in Post-Main Sequence Models},
  journal = {Astronomy & Astrophysics},
  year    = {2026},
  volume  = {XXX},
  pages   = {YYY-ZZZ},
  doi     = {10.1234/zenodo.XXXXX}
}
```


Additionally, you can cite the Zenodo DOI for this repository:


