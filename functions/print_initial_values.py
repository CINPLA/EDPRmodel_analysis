
def print_initial_values(init_cell):

    phi_si, phi_se, phi_di, phi_de, phi_sm, phi_dm = init_cell.membrane_potentials()

    E_Na_s, E_Na_d, E_K_s, E_K_d, E_Cl_s, E_Cl_d, E_Ca_s, E_Ca_d = init_cell.reversal_potentials()

    q_si = init_cell.total_charge([init_cell.Na_si, init_cell.K_si, init_cell.Cl_si, init_cell.Ca_si, init_cell.X_si], init_cell.V_si)
    q_se = init_cell.total_charge([init_cell.Na_se, init_cell.K_se, init_cell.Cl_se, init_cell.Ca_se, init_cell.X_se], init_cell.V_se)        
    q_di = init_cell.total_charge([init_cell.Na_di, init_cell.K_di, init_cell.Cl_di, init_cell.Ca_di, init_cell.X_di], init_cell.V_di)
    q_de = init_cell.total_charge([init_cell.Na_de, init_cell.K_de, init_cell.Cl_de, init_cell.Ca_de, init_cell.X_de], init_cell.V_de)

    print("----------------------------")
    print("Initial values")
    print("----------------------------")
    print("initial total charge(C): ", q_si + q_se + q_di + q_de)
    print("Q_si (C):", q_si)
    print("Q_se (C):", q_se)
    print("Q_di (C):", q_di)
    print("Q_de (C):", q_de)
    print("----------------------------")
    print("potentials [mV]")
    print('phi_si: ', round(phi_si*1000))
    print('phi_se: ', round(phi_se*1000))
    print('phi_di: ', round(phi_di*1000))
    print('phi_de: ', round(phi_de*1000))
    print('phi_sm: ', round(phi_sm*1000,1))
    print('phi_dm: ', round(phi_dm*1000,1))
    print('E_Na_s: ', round(E_Na_s*1000))
    print('E_Na_d: ', round(E_Na_d*1000))
    print('E_K_s: ', round(E_K_s*1000))
    print('E_K_d: ', round(E_K_d*1000))
    print('E_Cl_s: ', round(E_Cl_s*1000))
    print('E_Cl_d: ', round(E_Cl_d*1000))
    print('E_Ca_s: ', round(E_Ca_s*1000))
    print('E_Ca_d: ', round(E_Ca_d*1000))
    print("----------------------------")

