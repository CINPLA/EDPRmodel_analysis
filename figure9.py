import numpy as np
import time
import matplotlib.pyplot as plt
from ICPRmodel.ICPRmodel import *
from functions.solve_ICPRmodel import *
from functions.print_final_values import *
from functions.calculate_phiVC_and_phidiff import *

start_time = time.time()

t_dur = 30      # [s]
alpha = 2.0
I_stim = 28e-12 # [A]
stim_start = 10 # [s]
stim_end = 20   # [s]

sol = solve_ICPRmodel(t_dur, alpha, I_stim, stim_start, stim_end)

Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, \
    k_res_si, k_res_se, k_res_di, k_res_de, n, h, s, c, q, z = sol.y
t = sol.t

my_cell = ICPRmodel(309.14, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, alpha, Ca_si[0], Ca_di[0], n, h, s, c, q, z)
print_final_values(my_cell)

phi_si, phi_se, phi_di, phi_de, phi_sm, phi_dm = my_cell.membrane_potentials()

E_Na_s, E_Na_d, E_K_s, E_K_d, E_Cl_s, E_Cl_d, E_Ca_s, E_Ca_d = my_cell.reversal_potentials()

print("----------------------------")
print('elapsed time: ', round(time.time() - start_time, 1), 'seconds')

f1 = plt.figure(1)
plt.plot(t, phi_sm*1000, '-', label='V_s')
plt.plot(t, phi_dm*1000, '-', label='V_d')
plt.title('Membrane potentials')
plt.xlabel('time [s]')
plt.ylabel('[mV]')
plt.legend(loc='upper right')

phi_diff, phi_vc = calculate_phiVC_and_phidiff(my_cell, phi_se, phi_de)

np.savez('data/figure9', t=t, phi_si=phi_si, phi_se=phi_se, phi_di=phi_di, phi_de=phi_de, phi_sm=phi_sm, phi_dm=phi_dm, phi_diff=phi_diff, phi_vc=phi_vc)

plt.show()
