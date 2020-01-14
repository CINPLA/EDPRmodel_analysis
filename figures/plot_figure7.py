import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from set_style import set_style

set_style('article', w=1, h=3)

fig, [[ax1,ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8], [ax9, ax10]] = plt.subplots(5,2)

data_EDPR = np.load('../data/figure7_EDPR.npz')
data_PR = np.load('../data/figure7_PR.npz')

t_PR = data_PR['t']/1000.
phi_sm_PR = data_PR['Vs']
free_Ca_PR = data_PR['Ca']

t = data_EDPR['t']
phi_sm = data_EDPR['phi_sm']*1000
phi_dm = data_EDPR['phi_dm']*1000
E_Na_s = data_EDPR['E_Na_s']*1000
E_Na_d = data_EDPR['E_Na_d']*1000
E_K_s = data_EDPR['E_K_s']*1000
E_K_d = data_EDPR['E_K_d']*1000
E_Cl_s = data_EDPR['E_Cl_s']*1000
E_Cl_d = data_EDPR['E_Cl_d']*1000
E_Ca_s = data_EDPR['E_Ca_s']*1000
E_Ca_d = data_EDPR['E_Ca_d']*1000
Na_si = data_EDPR['Na_si']
Na_se = data_EDPR['Na_se']
Na_di = data_EDPR['Na_di']
Na_de = data_EDPR['Na_de']
K_si = data_EDPR['K_si']
K_se = data_EDPR['K_se']
K_di = data_EDPR['K_di']
K_de = data_EDPR['K_de']
Cl_si = data_EDPR['Cl_si']
Cl_se = data_EDPR['Cl_se']
Cl_di = data_EDPR['Cl_di']
Cl_de = data_EDPR['Cl_de']
Ca_si = data_EDPR['Ca_si']
Ca_se = data_EDPR['Ca_se']
Ca_di = data_EDPR['Ca_di']
Ca_de = data_EDPR['Ca_de']
free_Ca_EDPR = data_EDPR['free_Ca_di']

t_reduced = t[0::1000]
Na_si = Na_si[0::1000]
Na_se = Na_se[0::1000]
Na_di = Na_di[0::1000]
Na_de = Na_de[0::1000]
K_si = K_si[0::1000]
K_se = K_se[0::1000]
K_di = K_di[0::1000]
K_de = K_de[0::1000]
Cl_si = Cl_si[0::1000]
Cl_se = Cl_se[0::1000]
Cl_di = Cl_di[0::1000]
Cl_de = Cl_de[0::1000]
Ca_se = Ca_se[0::1000]

### Panel A ###
ax1.plot(t_PR, phi_sm_PR, ls='-', color='k')
ax1.set_title('PR $\phi\mathrm{_{sm}}$')
ax1.set_yticks([-65, 0])
ax1.set_xlim(10,22)
ax1.set_ylim(-75, 25)
axin1 = inset_axes(ax1, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax1.transAxes, loc=3)
axin1.plot(t_PR, phi_sm_PR, ls='-', color='k')
axin1.set_xticklabels([])
axin1.set_yticklabels([])
axin1.set_ylim(-75, 25)
axin1.set_xlim(0, 200)

### Panel B ###
ax2.plot(t_PR, free_Ca_PR, ls='-', color='k')
ax2.set_title('PR $\mathrm{[Ca^{2+}]_{di}}$')
ax2.set_ylabel('a.u.')
ax2.set_xlim(10,22)
ax2.set_ylim(-10,260)
axin2 = inset_axes(ax2, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax2.transAxes, loc=3)
axin2.plot(t_PR, free_Ca_PR, ls='-', color='k')
axin2.set_xticklabels([])
axin2.set_yticklabels([])
axin2.set_xlim(0, 200)

### Panel C ###
ax3.plot(t, phi_sm, ls='-', color='k')
ax3.set_title('EDPR $\phi\mathrm{^{sm}}$')
ax3.set_yticks([-65, 0])
ax3.set_xlim(10,22)
ax3.set_ylim(-75, 25)
axin3 = inset_axes(ax3, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax3.transAxes, loc=3)
axin3.plot(t, phi_sm, ls='-', color='k')
axin3.set_xticklabels([])
axin3.set_yticklabels([])
axin3.set_ylim(-75, 25)
axin3.set_xlim(0, 200)

### Panel D ###
ax4.plot(t, free_Ca_EDPR*1e6, ls='-', color='k')
ax4.set_title('EDPR free $\mathrm{[Ca^{2+}]_{di}}$')
ax4.set_ylabel('nM')
ax4.set_xlim(10,22)
axin4 = inset_axes(ax4, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax4.transAxes, loc=3)
axin4.plot(t, free_Ca_EDPR*1e6, ls='-', color='k')
axin4.set_xticklabels([])
axin4.set_yticklabels([])
axin4.set_xlim(0, 200)

### Panel E ###
l1 = ax5.plot(t, E_Na_s-E_Na_s[0], zorder=10)[0]
l2 = ax5.plot(t, E_K_s-E_K_s[0], zorder=10)[0]
l3 = ax5.plot(t, E_Cl_s-E_Cl_s[0], zorder=10)[0]
l4 = ax5.plot(t, E_Ca_s-E_Ca_s[0], zorder=10)[0]
ax5.set_title('$\Delta E\mathrm{_{k,s}}$')
ax5.spines['bottom'].set_position('zero')
fig.legend([l1, l2, l3, l4], ['$\mathrm{Na^+}$', '$\mathrm{K^+}$', '$\mathrm{Cl^-}$', '$\mathrm{Ca^{2+}}$'], \
    loc=(0.38,0.38), ncol=2, fontsize='small', handlelength=1, handletextpad=0.4, columnspacing=0.4)
ax5.set_ylim(-20, 20)

axin5 = inset_axes(ax5, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax5.transAxes, loc=3)
axin5.plot(t, E_Na_s-E_Na_s[0], zorder=10)[0]
axin5.plot(t, E_K_s-E_K_s[0], zorder=10)[0]
axin5.plot(t, E_Cl_s-E_Cl_s[0], zorder=10)[0]
axin5.plot(t, E_Ca_s-E_Ca_s[0], zorder=10)[0]
axin5.set_xticklabels([])
axin5.yaxis.set_label_position('right')
axin5.yaxis.tick_right()
axin5.tick_params(axis='y', labelsize=6, pad=1)
axin5.set_yticks([0,50])
axin5.set_xlim(0, 200)

### Panel F ###
l1 = ax6.plot(t, E_Na_d-E_Na_d[0], zorder=10)
l2 = ax6.plot(t, E_K_d-E_K_d[0], zorder=10)
l3 = ax6.plot(t, E_Cl_d-E_Cl_d[0], zorder=10)
l4 = ax6.plot(t, E_Ca_d-E_Ca_d[0], zorder=10)
ax6.set_title('$\Delta E\mathrm{_{k,d}}$')
ax6.spines['bottom'].set_position('zero')
axin6 = inset_axes(ax6, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax6.transAxes, loc=3)
axin6.plot(t, E_Na_d-E_Na_d[0])
axin6.plot(t, E_K_d-E_K_d[0])
axin6.plot(t, E_Cl_d-E_Cl_d[0])
axin6.plot(t, E_Ca_d-E_Ca_d[0])
axin6.set_xticklabels([])
axin6.yaxis.set_label_position('right')
axin6.yaxis.tick_right()
axin6.tick_params(axis='y', labelsize=6, pad=1)
axin6.set_yticks([0,50])
axin6.set_xlim(0, 200)

### Panel G ###
ax7.plot(t_reduced, Na_si-Na_si[0], zorder=10)
ax7.plot(t_reduced, K_si-K_si[0], zorder=10)
ax7.plot(t_reduced, Cl_si-Cl_si[0], zorder=10)
ax7.plot(t, Ca_si-Ca_si[0], zorder=10)
ax7.spines['bottom'].set_position('zero')
ax7.set_title('$\Delta\mathrm{[k]_{si}}$')

axin7 = inset_axes(ax7, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax7.transAxes, loc=3)
axin7.plot(t_reduced, Na_si-Na_si[0], zorder=10)
axin7.plot(t_reduced, K_si-K_si[0], zorder=10)
axin7.plot(t_reduced, Cl_si-Cl_si[0], zorder=10)
axin7.plot(t, Ca_si-Ca_si[0], zorder=10)
axin7.set_xticklabels([])
axin7.yaxis.set_label_position('right')
axin7.yaxis.tick_right()
axin7.tick_params(axis='y', labelsize=6, pad=1)
axin7.set_yticks([0,25])
axin7.set_xlim(0, 200)

### Panel H ###
ax8.plot(t_reduced, Na_di-Na_di[0], zorder=10)
ax8.plot(t_reduced, K_di-K_di[0], zorder=10)
ax8.plot(t_reduced, Cl_di-Cl_di[0], zorder=10)
ax8.plot(t, Ca_di-Ca_di[0], zorder=10)
ax8.spines['bottom'].set_position('zero')
ax8.set_title('$\Delta\mathrm{[k]_{di}}$')
axin8 = inset_axes(ax8, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax8.transAxes, loc=3)
axin8.plot(t_reduced, Na_di-Na_di[0], zorder=10)
axin8.plot(t_reduced, K_di-K_di[0], zorder=10)
axin8.plot(t_reduced, Cl_di-Cl_di[0], zorder=10)
axin8.plot(t, Ca_di-Ca_di[0], zorder=10)
axin8.set_xticklabels([])
axin8.yaxis.set_label_position('right')
axin8.yaxis.tick_right()
axin8.tick_params(axis='y', labelsize=6, pad=1)
axin8.set_yticks([0,25])
axin8.set_xlim(0, 200)

### Panel I ###
ax9.plot(t_reduced, Na_se-Na_se[0], zorder=10)
ax9.plot(t_reduced, K_se-K_se[0], zorder=10)
ax9.plot(t_reduced, Cl_se-Cl_se[0], zorder=10)
ax9.plot(t_reduced, Ca_se-Ca_se[0], zorder=10)
ax9.set_title('$\Delta\mathrm{[k]_{se}}$')
ax9.set_xlabel('time [s]')
axin9 = inset_axes(ax9, width="40%", height="40%", bbox_to_anchor=(0.0, 0.6, 1., 1.), bbox_transform=ax9.transAxes, loc=3)
axin9.plot(t_reduced, Na_se-Na_se[0], zorder=10)
axin9.plot(t_reduced, K_se-K_se[0], zorder=10)
axin9.plot(t_reduced, Cl_se-Cl_se[0], zorder=10)
axin9.plot(t_reduced, Ca_se-Ca_se[0], zorder=10)
axin9.set_xticklabels([])
axin9.yaxis.set_label_position('right')
axin9.yaxis.tick_right()
axin9.tick_params(axis='y', labelsize=6, pad=1)
axin9.set_yticks([-50, 0])
axin9.set_xlim(0, 200)

### Panel J ###
ax10.plot(t_reduced, Na_de-Na_de[0], zorder=10)
ax10.plot(t_reduced, K_de-K_de[0], zorder=10)
ax10.plot(t_reduced, Cl_de-Cl_de[0], zorder=10)
ax10.plot(t, Ca_de-Ca_de[0], zorder=10)
ax10.set_title('$\Delta\mathrm{[k]_{de}}$')
ax10.set_xlabel('time [s]')
axin10 = inset_axes(ax10, width="40%", height="40%", bbox_to_anchor=(0.0, 0.6, 1., 1.), bbox_transform=ax10.transAxes, loc=3)
axin10.plot(t_reduced, Na_de-Na_de[0], zorder=10)
axin10.plot(t_reduced, K_de-K_de[0], zorder=10)
axin10.plot(t_reduced, Cl_de-Cl_de[0], zorder=10)
axin10.plot(t, Ca_de-Ca_de[0], zorder=10)
axin10.set_xticklabels([])
axin10.yaxis.set_label_position('right')
axin10.yaxis.tick_right()
axin10.tick_params(axis='y', labelsize=6, pad=1)
axin10.set_yticks([-50, 0])
axin10.set_xlim(0, 200)

axarr = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]

for ax in [ax1, ax3, ax5, ax6]:
    ax.set_ylabel('mV')

for ax in axarr[6:]:
    ax.set_ylabel('mM')

for ax in axarr[4:6]:
    ax.set_xlim(10,22)

for ax in axarr[6:]:
    ax.set_xlim(10,22)
    ax.set_ylim(-7,7)

for ax in [ax5, ax6, ax7, ax8]:
    ax.set_xticklabels([])

for ax in axarr:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

panel = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
for i in range(0,10):
    if i == 7:
        axarr[i].text(-0.03, 1.38, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    else:
        axarr[i].text(-0.1, 1.38, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

fig.align_ylabels(axarr)
plt.tight_layout()
plt.savefig('figures_pdf/figure6.pdf', dpi=300)
