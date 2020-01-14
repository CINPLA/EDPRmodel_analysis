import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('article', w=1, h=3)

data = np.load('../data/figure8.npz')

t = data['t']/60.
phi_sm = data['phi_sm']*1000
phi_dm = data['phi_dm']*1000
E_Na_s = data['E_Na_s']*1000
E_Na_d = data['E_Na_d']*1000
E_K_s = data['E_K_s']*1000
E_K_d = data['E_K_d']*1000
E_Cl_s = data['E_Cl_s']*1000
E_Cl_d = data['E_Cl_d']*1000
E_Ca_s = data['E_Ca_s']*1000
E_Ca_d = data['E_Ca_d']*1000
Na_si = data['Na_si']
Na_se = data['Na_se']
Na_di = data['Na_di']
Na_de = data['Na_de']
K_si = data['K_si']
K_se = data['K_se']
K_di = data['K_di']
K_de = data['K_de']
Cl_si = data['Cl_si']
Cl_se = data['Cl_se']
Cl_di = data['Cl_di']
Cl_de = data['Cl_de']
Ca_si = data['Ca_si']
Ca_se = data['Ca_se']
Ca_di = data['Ca_di']
Ca_di = data['Ca_di']
Ca_de = data['Ca_de']

fig = plt.figure()
gs = gridspec.GridSpec(4, 4)
ax0 = plt.subplot(gs[0,:])
ax1 = plt.subplot(gs[1,0:2])
ax2 = plt.subplot(gs[1,2:])
ax3 = plt.subplot(gs[2,0:2])
ax4 = plt.subplot(gs[2,2:])
ax5 = plt.subplot(gs[3,0:2])
ax6 = plt.subplot(gs[3,2:])

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

### Panel A ###
l1 = ax0.plot(t*60, phi_sm, ls='-', lw=1, color='k')[0]
ax0.set_title('$\phi\mathrm{_{sm}}$')
ax0.set_ylabel('mV')
ax0.set_yticks([-65, -20, 0])
ax0.set_xlabel('time [s]')
axin0 = inset_axes(ax0, width="40%", height="40%", bbox_to_anchor=(0.01, 0.5, 1., 1.), bbox_transform=ax0.transAxes, loc=3)
axin0.plot(t*60, phi_sm, ls='-', color='k')
axin0.set_ylim(-70, 20)
axin0.set_xlim(30.2, 31.2)
axin0.yaxis.set_label_position('right')
axin0.yaxis.tick_right()
axin0.tick_params(axis='y', labelsize=6, pad=1)
axin0.set_yticks([-65,-20,0])
axin0.tick_params(axis='x', labelsize=6)

### Panel B ###
l1 = ax1.plot(t, E_K_s, lw=3, ls='-', zorder=10)[0]
l2 = ax1.plot(t, E_Na_s, lw=3, ls=':', zorder=10)[0]
l3 = ax1.plot(t, E_Cl_s, lw=2, ls='--', zorder=10)[0]
l4 = ax1.plot(t, E_Ca_s, lw=3, ls='-', zorder=10)[0]
ax1.set_title('$E\mathrm{_{k,s}}$')
ax1.set_ylabel('mV')
ax1.spines['bottom'].set_position('zero')
ax1.set_yticks([-20, 100])
ax1.set_xticklabels([])
fig.legend([l2, l1, l3, l4], ['$E\mathrm{_{Na}}$', '$E\mathrm{_K}$', '$E\mathrm{_{Cl}}$', '$E\mathrm{_{Ca}}$'], \
    loc=(0.41,0.48), ncol=2, fontsize='small', handlelength=1, handletextpad=0.4, columnspacing=0.4)

### Panel C ###
ax2.plot(t, E_K_d, lw=3, ls='-', zorder=10)
ax2.plot(t, E_Na_d, lw=3, ls=':', zorder=10)
ax2.plot(t, E_Cl_d, lw=2, ls='--', zorder=10)
ax2.plot(t, E_Ca_d, lw=3, ls='-', zorder=9)
ax2.set_title('$E\mathrm{_{k,d}}$')
ax2.set_ylabel('mV')
ax2.spines['bottom'].set_position('zero')
ax2.set_yticks([-20, 100])
ax2.set_xticklabels([])

### Panel D ###
l1 = ax3.plot(t, Na_si, lw=3, ls='-', zorder=10)[0]
l2 = ax3.plot(t, Na_se, lw=3, ls='-', zorder=10)[0]
l3 = ax3.plot(t, Na_di, lw=2.5, ls=':', zorder=10)[0]
l4 = ax3.plot(t, Na_de, lw=2.5, ls=':', zorder=10)[0]
ax3.set_title('$[\mathrm{Na^+}]$')
ax3.set_ylabel('mM')
ax3.set_xticklabels([])
fig.legend([l1, l2, l3, l4], ['$\mathrm{[k]_s^i}$', '$\mathrm{[k]_s^e}$', '$\mathrm{[k]_d^i}$', '$\mathrm{[k]_d^e}$'], \
    loc=(0.41,0.22), ncol=2, fontsize='small', handlelength=1, handletextpad=0.4, columnspacing=0.4)

### Panel E ###
ax4.plot(t, K_si, lw=3, ls='-', zorder=10)[0]
ax4.plot(t, K_se, lw=3, ls='-', zorder=10)[0]
ax4.plot(t, K_di, lw=2.5, ls=':', zorder=10)[0]
ax4.plot(t, K_de, lw=2.5, ls=':', zorder=10)[0]
ax4.set_title('$[\mathrm{K^+}]$')
ax4.set_ylabel('mM')
ax4.set_xticklabels([])

### Panel F ###
ax5.plot(t, Cl_si, lw=3, ls='-', zorder=10)[0]
ax5.plot(t, Cl_se, lw=3, ls='-', zorder=10)[0]
ax5.plot(t, Cl_di, lw=2.5, ls=':', zorder=10)[0]
ax5.plot(t, Cl_de, lw=2.5, ls=':', zorder=10)[0]
ax5.set_title('$[\mathrm{Cl^-}]$')
ax5.set_ylabel('mM')
ax5.set_xlabel('time [min]')

#### Panel G ###
ax6.plot(t, Ca_si, lw=3, ls='-', zorder=10)[0]
ax6.plot(t, Ca_se, lw=3, ls='-', zorder=10)[0]
ax6.plot(t, Ca_di, lw=2.5, ls=':', zorder=10)[0]
ax6.plot(t, Ca_de, lw=2.5, ls=':', zorder=10)[0]
ax6.set_title('$[\mathrm{Ca^{2+}}]$')
ax6.set_ylabel('mM')
ax6.set_xlabel('time [min]')
ax6.set_ylim(0,1.2)

for ax in [ax3, ax4, ax5]:
    ax.set_ylim(0,145)

# remove top and right borders
ax0.set_xlim(0,60)
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0,10)

axarr = [ax0, ax1, ax2, ax3, ax4, ax5, ax6]
panel = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i in range(0,7):
    if i == 4 or i == 6:
        axarr[i].text(0.13, 1.32, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    else:
        axarr[i].text(-0.09, 1.32, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

fig.align_ylabels([ax1, ax3, ax5])
fig.align_ylabels([ax2, ax4, ax6])
plt.tight_layout()
plt.savefig('figures_pdf/figure7.pdf', dpi=300)
