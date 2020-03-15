import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('article', w=1, h=1.1)

data = np.load('../data/figure10.npz')

t = data['t']
phi_sm = data['phi_sm']*1000
phi_dm = data['phi_dm']*1000
phi_se = data['phi_se']*1000
phi_diff = data['phi_diff']*1000
phi_vc = data['phi_vc']*1000

fig, [ax1, ax2] = plt.subplots(1, 2)

### Panel A ###
ax1.plot(t, phi_vc, ':', zorder=10, label='$\phi\mathrm{_{VC,e}}$')
ax1.plot(t, phi_diff, '-', zorder=10, label='$\phi\mathrm{_{diff,e}}$')
ax1.plot(t, phi_se, 'k-', zorder=9, label='$\phi\mathrm{_{KNP,e}}$')
ax1.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')
ax1.set_xlim([0,30])
ax1.set_ylim([-7,7])
ax1.set_ylabel('mV')
ax1.set_xlabel('time [s]')

### Panel B ###
ax2.plot(t*1000, phi_vc, ':', zorder=10)
ax2.plot(t*1000, phi_diff, '-', zorder=10)
ax2.plot(t*1000, phi_se, 'k', '-', zorder=9)
ax2.set_xlim([19100,19200])
ax2.set_ylim([-0.25,0.25])
ax2.set_yticks([-0.2, 0])
ax2.set_yticklabels([-0.2, 0])
ax2.set_xlabel('time [ms]')

plt.suptitle('Extracellular potential')

for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

axarr = [ax1, ax2]
panel = ['A', 'B']
for i in range(0,2):
    axarr[i].text(-0.1, 0.9, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

plt.tight_layout()
plt.savefig('figure10.eps', dpi=600)
