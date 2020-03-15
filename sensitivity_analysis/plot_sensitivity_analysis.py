import uncertainpy as un
import matplotlib.pyplot as plt
from figures.set_style import set_style
import numpy as np

set_style('article', w=1, h=3)
fig, [ax1, ax2] = plt.subplots(2, 1)

data = un.Data()
data.load("data/pinskyrinzelpump.h5")

t = data["pinskyrinzelpump"].time
mean = data["pinskyrinzelpump"].mean
variance = data["pinskyrinzelpump"].variance
sd = np.sqrt(variance)
sobol = data['pinskyrinzelpump'].sobol_total_average

ax1.plot(t, mean, 'k', label='mean')
ax1.fill_between(t, mean-sd, mean+sd, lw=3, label='standard deviation')
ax1.legend()
ax1.set_title('Somatic membrane potential')
ax1.set_ylabel('mV')
ax1.set_xlabel('Time [s]')
ax1.set_xlim(0, 15)
ax1.set_ylim(-70, -65)

ax2.set_title('Total-order Sobol indices')
ax2.bar(np.arange(0,6), sobol)
ax2.set_ylim(0,1)
ax2.set_xticklabels([0, '$g\mathrm{_{Na,leak}}$', '$g\mathrm{_{K,leak}}$', '$g\mathrm{_{Cl,leak}}$', r'$\rho$', '$U\mathrm{_{kcc2}}$', '$U\mathrm{_{nkcc1}}$'])

for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax1.text(-0.1, 1.1, 'A', transform=ax1.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
ax2.text(-0.1, 1.1, 'B', transform=ax2.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

plt.tight_layout()
plt.savefig('figure4.eps', dpi=600)
