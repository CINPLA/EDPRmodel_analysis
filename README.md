# An electrodiffusive, ion conserving Pinsky-Rinzel model with homeostatic mechanisms

 This code was used to produce the results presented in Sætra et al. 2020: [An electrodiffusive, ion conserving Pinsky-Rinzel model with homeostatic mechanisms](https://doi.org/10.1371/journal.pcbi.1007661
).

# Installation

To install the code, clone or download the repo, navigate to the top directory of the repo and enter the following command
in the terminal: 
```bash
python setup.py install
```

Requirements are given in `requirements.txt` and can be installed by the following command:
```bash
pip install -r requirements.txt
```

You must also have EDPRmodel and PRmodel installed. They can be downloaded from 
[https://github.com/CINPLA/EDPRmodel](https://github.com/CINPLA/EDPRmodel) and [https://github.com/CINPLA/PRmodel](https://github.com/CINPLA/PRmodel), respectively.

The code was run with Ubuntu 18.04.3 and Python 3.6.9.

# Reproducing the results of the paper

To reproduce the results of the paper,
run `bash run_all.sh`. Note that this might run for a couple of days on a normal computer. To plot and save the figures, run 
`bash plot_all.sh` from the folder named figures.

If you have problems reading the initial_values.npz-file, install git lfs and try `git-lfs pull`.
