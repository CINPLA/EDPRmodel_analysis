import uncertainpy as un
import chaospy as cp
from wrapper_sensitivity_analysis import pinskyrinzelpump

# Initialize the model and add labels
model = un.Model(run=pinskyrinzelpump, labels=["Time (s)", "Somatic membrane potential (mV)"], interpolate=True)

# Define a parameter dictionary
parameters = {"g_Na_leak": 0.247,
              "g_K_leak": 0.5,
              "g_Cl_leak": 1.0,
              "rho": 1.87e-6,
              "U_kcc2": 7.0e-7,
              "U_nkcc1": 2.33e-7}

# Create the parameters
parameters = un.Parameters(parameters)

# Set all parameters to have a uniform distribution 
# within a +/- 15 % interval around their fixed value
parameters.set_all_distributions(un.uniform(0.3))

# Perform the uncertainty quantification
UQ = un.UncertaintyQuantification(model, parameters=parameters)

# We set the seed to easier be able to reproduce the result
data = UQ.quantify(seed=10)

