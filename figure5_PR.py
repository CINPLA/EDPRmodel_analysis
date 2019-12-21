import numpy as np
import time
import matplotlib.pyplot as plt
from originalPRmodel import solve_originalPRmodel

start_time = time.time()

t_dur = 3600e3      # [ms]
g_c = 10.5        # [mS/cm^2] Strong
I_stim = 0.78      # [uA/cm^2]
stim_start = 10e3 # [ms]
stim_end = 3601e3   # [ms]

sol = solve_originalPRmodel(t_dur, g_c, I_stim, stim_start, stim_end)

Vs, Vd, n, h, s, c, q, Ca = sol.y
t = sol.t

print('elapsed time: ', round(time.time() - start_time, 1), 'seconds')

# plot
f1 = plt.figure(1)
plt.plot(t/1000, Vs, '-', label='V_s')
plt.plot(t/1000, Vd, '-', label='V_d')
plt.title('Membrane potentials')
plt.xlabel('time [s]')
plt.ylabel('[mV]')
plt.legend(loc='upper right')

# save to file
np.savez('data/figure5_PR', t=t, Vs=Vs, Vd=Vd, Ca=Ca)

plt.show()
