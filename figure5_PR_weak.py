import numpy as np
import time
import matplotlib.pyplot as plt
from PRmodel import solve_PRmodel

start_time = time.time()

t_dur = 30e3      # [ms]
g_c = 2.26        # [mS/cm^2] Weak
I_stim = 1.35     # [uA/cm^2]
stim_start = 10e3 # [ms]
stim_end = 20e3   # [ms]

sol = solve_PRmodel(t_dur, g_c, I_stim, stim_start, stim_end)

Vs, Vd, n, h, s, c, q, Ca = sol.y
t = sol.t

#print('elapsed time: ', round(time.time() - start_time, 1), 'seconds')

# plot
f1 = plt.figure(1)
plt.plot(t/1000, Vs, '-', label='V_s')
plt.plot(t/1000, Vd, '-', label='V_d')
plt.title('Membrane potentials')
plt.xlabel('time [s]')
plt.ylabel('[mV]')
plt.legend(loc='upper right')

# save to file
np.savez('data/figure5_PR_weak', t=t, Vs=Vs, Vd=Vd, Ca=Ca)

#plt.show()
