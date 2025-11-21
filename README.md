# Scripts for "Stranger Things: A Grid-based Survey of Strange Modes in Post-Main Sequence Models"


This repository contains the Python scripts used to generate the models and data presented in "Stranger Things: A Grid-based Survey of Strange Modes in Post-Main Sequence Models" (Tarczay-Nehéz et al., 2026). The scripts automate the creation of MESA input directories for a grid of stellar masses and metallicities, including overshoot prescriptions and inlist configurations.


> ⚠️ **Important compatibility note**  
> These scripts have been tested and are known to work with:  
> - **MESA version 23.05.1**  
> - **GYRE version 7.0**  
>  
> Other versions may lead to unexpected behavior or incompatibilities.  
>  
> ⚠️ **Disclaimer**  
> It is assumed that the user is already familiar with MESA, has it properly installed, and knows how to run it. Installation instructions, tutorials, and general usage guides are **not** part of this repository.




## Contents

* **generate_dirs/** – this includes the grid generating pys.
* **include/** – this direcotry contains ``MESA`` ``src/`` and ``make`` dirs for the current runs.
* **exec/** - this directory contains the ``MESA`` executables (``clean``, ``rn``, ``star``, etc) for the script.
* **example/** – sample run directory structure.


## Requirements

- Python 3.8 or newer
- NumPy ≥ 1.18
- MESA version 23.05.1
- GYRE version 7.0


## Usage

1. To recreate your grid of *MESA* runs, clone the repository:

```bash:
git clone https://github.com/username/Strange-mode-cepheids.git
cd Strange-mode-cepheids
```

2. Run the scripts in one of two ways:

** Option A — generate all grids at once (recommended): **

```bash:
python initialize_grid.py
```

This will run all generator scripts (``initialize_convos_low_grid.py``, ``initialize_convos_mid_grid.py``, ``initialize_convos_high_grid.py``, ``initialize_no_os_grid.py``) and create the corresponding directories in the repository ``root``.


** Option B — generate grids individually: **

```bash:
cd generata_dirs
python initialize_convos_high_grid.py
```
... or the corresponding script (``initialize_convos_mid_grid.py``, ``initialize_convos_high_grid.py``) depending on the grid you want to generate.


3. After successful execution, a set of run directories will be created under the chosen ``base_dir`` in the ``root`` directory (i.e., ``no_os``, ``nad_convos_low``, ``nad_convos_mid``, ``nad_convos_high``). Each run directory contains:

* ``inlist`` and ``inlist_project`` input files
* copied executables from exec/
* copied source/build directories from include/

👉 See ``example/run_no_os_2.0MSUN_z0.0120/`` for a reference of how a correctly generated run directory should look.





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


