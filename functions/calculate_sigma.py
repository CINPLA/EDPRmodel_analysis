
def calculate_sigma(my_cell, t):
    """
    Calculates the conductivity of the intra- and extracellular media
    (sigma_i and sigma_e, respectively).
    """

    sigma_i = my_cell.conductivity_k(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_i, my_cell.Na_si, my_cell.Na_di) \
    + my_cell.conductivity_k(my_cell.D_K, my_cell.Z_K, my_cell.lamda_i, my_cell.K_si, my_cell.K_di) \
    + my_cell.conductivity_k(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_i, my_cell.Cl_si, my_cell.Cl_di) \
    + my_cell.conductivity_k(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_i, my_cell.free_Ca_si, my_cell.free_Ca_di)

    sigma_e = my_cell.conductivity_k(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_e, my_cell.Na_se, my_cell.Na_de) \
    + my_cell.conductivity_k(my_cell.D_K, my_cell.Z_K, my_cell.lamda_e, my_cell.K_se, my_cell.K_de) \
    + my_cell.conductivity_k(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_e, my_cell.Cl_se, my_cell.Cl_de) \
    + my_cell.conductivity_k(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_e, my_cell.Ca_se, my_cell.Ca_de)
    
    return sigma_i, sigma_e
