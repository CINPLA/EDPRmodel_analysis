import matplotlib.pyplot as plt

def calculate_phiVC_and_phidiff(my_cell, phi_se, phi_de):

    I_e_diff = my_cell.F * (my_cell.Z_Na*my_cell.j_k_diff(my_cell.D_Na, my_cell.lamda_e, my_cell.Na_se, my_cell.Na_de) \
    + my_cell.Z_K*my_cell.j_k_diff(my_cell.D_K, my_cell.lamda_e, my_cell.K_se, my_cell.K_de) \
    + my_cell.Z_Cl*my_cell.j_k_diff(my_cell.D_Cl, my_cell.lamda_e, my_cell.Cl_se, my_cell.Cl_de) \
    + my_cell.Z_Ca*my_cell.j_k_diff(my_cell.D_Ca, my_cell.lamda_e, my_cell.Ca_se, my_cell.Ca_de))
   
    I_e_drift = my_cell.F \
        * (my_cell.Z_Na*my_cell.j_k_drift(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_e, my_cell.Na_se, my_cell.Na_de, phi_se, phi_de) \
        + my_cell.Z_K*my_cell.j_k_drift(my_cell.D_K, my_cell.Z_K, my_cell.lamda_e, my_cell.K_se, my_cell.K_de, phi_se, phi_de) \
        + my_cell.Z_Cl*my_cell.j_k_drift(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_e, my_cell.Cl_se, my_cell.Cl_de, phi_se, phi_de) \
        + my_cell.Z_Ca*my_cell.j_k_drift(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_e, my_cell.Ca_se, my_cell.Ca_de, phi_se, phi_de))

    I_e = I_e_diff + I_e_drift

    sigma_e = my_cell.conductivity_k(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_e, my_cell.Na_se, my_cell.Na_de) \
    + my_cell.conductivity_k(my_cell.D_K, my_cell.Z_K, my_cell.lamda_e, my_cell.K_se, my_cell.K_de) \
    + my_cell.conductivity_k(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_e, my_cell.Cl_se, my_cell.Cl_de) \
    + my_cell.conductivity_k(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_e, my_cell.Ca_se, my_cell.Ca_de)

    phi_diff = - I_e_diff * my_cell.dx / sigma_e
    phi_vc = I_e * my_cell.dx / sigma_e

    return phi_diff, phi_vc

