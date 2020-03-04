import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from EDPRmodel.EDPRmodel import *
from EDPRmodel.somatic_injection_current import *
import pkg_resources

def pinskyrinzelpump(g_Na_leak,
                     g_K_leak,
                     g_Cl_leak,
                     rho,
                     U_kcc2,
                     U_nkcc1):

    T = 309.14
    alpha = 2.0

    filename = pkg_resources.resource_filename('data', 'initial_values/initial_values.npz')
    data = np.load(filename)

    Na_si0 = data['Na_si']
    Na_se0 = data['Na_se']
    K_si0 = data['K_si']
    K_se0 = data['K_se']
    Cl_si0 = data['Cl_si']
    Cl_se0 = data['Cl_se']
    Ca_si0 = data['Ca_si']
    Ca_se0 = data['Ca_se']

    Na_di0 = data['Na_di']
    Na_de0 = data['Na_de']
    K_di0 = data['K_di'] 
    K_de0 = data['K_de']
    Cl_di0 = data['Cl_di']
    Cl_de0 = data['Cl_de']
    Ca_di0 = data['Ca_di']
    Ca_de0 = data['Ca_de']

    X_si0 = data['X_si']
    X_se0 = data['X_se']
    X_di0 = data['X_di']
    X_de0 = data['X_de']

    n0 = data['n']
    h0 = data['h']
    s0 = data['s']
    c0 = data['c']
    q0 = data['q']
    z0 = data['z']

    def dkdt(t, k,
             g_Na_leak,
             g_K_leak,
             g_Cl_leak,
             rho,
             U_kcc2,
             U_nkcc1):
        
        Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, \
            X_si, X_se, X_di, X_de, n, h, s, c, q, z = k
        my_cell = EDPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, \
            Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, alpha, Ca_si0, Ca_di0, n, h, s, c, q, z)
        
        my_cell.g_Na_leak = g_Na_leak
        my_cell.g_K_leak = g_K_leak
        my_cell.g_Cl_leak = g_Cl_leak
        my_cell.rho = rho
        my_cell.U_kcc2 = U_kcc2
        my_cell.U_nkcc1 = U_nkcc1

        dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, dCldt_si, dCldt_se, dCldt_di, dCldt_de, \
            dCadt_si, dCadt_se, dCadt_di, dCadt_de, dresdt_si, dresdt_se, dresdt_di, dresdt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()

        return dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, \
            dCldt_si, dCldt_se, dCldt_di, dCldt_de, dCadt_si, dCadt_se, dCadt_di, dCadt_de, \
            dresdt_si, dresdt_se, dresdt_di, dresdt_de, dndt, dhdt, dsdt, dcdt, dqdt, dzdt

    # solve
    t_span = (0, 15)
    k0 = [Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, \
        X_si0, X_se0, X_di0, X_de0, n0, h0, s0, c0, q0, z0]
    sol = solve_ivp(lambda t, k: dkdt(t, k, g_Na_leak, g_K_leak, g_Cl_leak, rho, U_kcc2, U_nkcc1), t_span, k0, max_step=1e-4)

    Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, \
        X_si, X_se, X_di, X_de, n, h, s, c, q, z = sol.y

    t = sol.t

    my_cell = EDPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, \
        Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, alpha, Ca_si0, Ca_di0, n, h, s, c, q, z)
    phi_si, phi_se, phi_di, phi_de, phi_sm, phi_dm = my_cell.membrane_potentials()

    return t, phi_sm*1000

if __name__ == "__main__":
    
    time, phi_sm = pinskyrinzelpump(0.247, 0.5, 1.0, 1.87e-6, 7.0e-7, 2.33e-7)
    plt.plot(time, phi_sm*1000)
    plt.ylim(-75, 0)
    plt.show()
