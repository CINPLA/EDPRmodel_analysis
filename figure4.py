from EDPRmodel.EDPRmodel import *
import numpy as np
import random
from functions.solve_EDPRmodel_sensitivity_analysis import *

g_Na_leak_array = np.ones(12)*0.247
g_K_leak_array = np.ones(12)*0.5
g_Cl_leak_array = np.ones(12)
rho_array = np.ones(12)*1.87e-6
U_kcc2_array = np.ones(12)*7e-7
U_nkcc1_array = np.ones(12)*2.33e-7

g_Na_leak_array[0] = g_Na_leak_array[0]*0.85
g_K_leak_array[1] = g_K_leak_array[1]*0.85
g_Cl_leak_array[2] = g_Cl_leak_array[2]*0.85
rho_array[3] = rho_array[3]*0.85
U_kcc2_array[4] = U_kcc2_array[4]*0.85
U_nkcc1_array[5] = U_nkcc1_array[5]*0.85

g_Na_leak_array[6] = g_Na_leak_array[6]*1.15
g_K_leak_array[7] = g_K_leak_array[7]*1.15
g_Cl_leak_array[8] = g_Cl_leak_array[8]*1.15
rho_array[9] = rho_array[9]*1.15
U_kcc2_array[10] = U_kcc2_array[10]*1.15
U_nkcc1_array[11] = U_nkcc1_array[11]*1.15

for N in range(0,12):
    
    g_Na_leak = g_Na_leak_array[N]
    g_K_leak = g_K_leak_array[N]
    g_Cl_leak = g_Cl_leak_array[N]
    rho = rho_array[N]
    U_kcc2 = U_kcc2_array[N]
    U_nkcc1 = U_nkcc1_array[N]
    
    sol = solve_EDPRmodel_sensitivity_analysis(g_Na_leak, g_K_leak, g_Cl_leak, rho, U_kcc2, U_nkcc1)

    Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, \
        X_si, X_se, X_di, X_de, n, h, s, c, q, z = sol.y
    t = sol.t

    my_cell = EDPRmodel(309.14, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, 2.0, 0.01, 0.01, n, h, s, c, q, z)

    phi_si, phi_se, phi_di, phi_de, phi_sm, phi_dm = my_cell.membrane_potentials()

    E_Na_s, E_Na_d, E_K_s, E_K_d, E_Cl_s, E_Cl_d, E_Ca_s, E_Ca_d = my_cell.reversal_potentials()

    np.savez('data/figure4_' + str(N+1), t=t, phi_si=phi_si, phi_se=phi_se, phi_di=phi_di, phi_de=phi_de, phi_sm=phi_sm, phi_dm=phi_dm, \
        E_Na_s=E_Na_s, E_Na_d=E_Na_d, E_K_s=E_K_s, E_K_d=E_K_d, E_Cl_s=E_Cl_s, E_Cl_d=E_Cl_d, E_Ca_s=E_Ca_s, E_Ca_d=E_Ca_d, \
        Na_si=Na_si, Na_se=Na_se, Na_di=Na_di, Na_de=Na_de, K_si=K_si, K_se=K_se, K_di=K_di, K_de=K_de, Cl_si=Cl_si, Cl_se=Cl_se, Cl_di=Cl_di, Cl_de=Cl_de, \
        Ca_si=Ca_si, Ca_se=Ca_se, Ca_di=Ca_di, Ca_de=Ca_de, free_Ca_di=my_cell.free_Ca_di, g_Na_leak=g_Na_leak, g_K_leak=g_K_leak, g_Cl_leak=g_Cl_leak, rho=rho, U_kcc2=U_kcc2, U_nkcc1=U_nkcc1)

