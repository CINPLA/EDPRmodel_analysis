# An electrodiffusive, ion conserving Pinsky-Rinzel model with homeostatic mechanisms

This code was used to produce the results presented in Sætra et al. 202X: [link]

# Installation

To install the code in this repo, clone or download the repo, navigate to the top directory of the repo and enter the following command
in the terminal: 
```bash
python setup.py install
```

Requirements are given in `requirements.txt` and can be installed by the following command:
```bash
pip install -r requirements.txt
```

You must also have ICPRmodel and originalPRmodel installed. They can be downloaded from 
[https://github.com/CINPLA/ICPRmodel](https://github.com/CINPLA/ICPRmodel) and [https://github.com/CINPLA/originalPRmodel](https://github.com/CINPLA/originalPRmodel), respectively.

The code was run with Ubuntu 18.04.3. 

# Reproducing the results of the paper

To reproduce the results of the paper, run `run_all.sh`. To plot and save the figures, run 
`plot_all.sh` in the folder named figures. The folder named sensitivity_analysis includes code
needed to run the sensitivity analysis presented in the appendix. 
