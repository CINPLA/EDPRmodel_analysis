import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from set_style import set_style

set_style('article', w=1, h=3)

fig, [[ax1,ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8], [ax9, ax10]] = plt.subplots(5,2)

data_EDPR = np.load('../data/figure6_EDPR.npz')
data_PR = np.load('../data/figure6_PR.npz')

t_PR = data_PR['t']/1000.
phi_sm_PR = data_PR['Vs']
free_Ca_PR = data_PR['Ca']

t_phi = data_EDPR['t']
phi_sm = data_EDPR['phi_sm']*1000
free_Ca_EDPR = data_EDPR['free_Ca_di']

t = data_EDPR['t'][0::1000]
E_Na_s = data_EDPR['E_Na_s'][0::10000]*1000
E_Na_d = data_EDPR['E_Na_d'][0::100]*1000
E_K_s = data_EDPR['E_K_s'][0::10000]*1000
E_K_d = data_EDPR['E_K_d'][0::100]*1000
E_Cl_s = data_EDPR['E_Cl_s'][0::10000]*1000
E_Cl_d = data_EDPR['E_Cl_d'][0::100]*1000
E_Ca_s = data_EDPR['E_Ca_s'][0::10000]*1000
E_Ca_d = data_EDPR['E_Ca_d'][0::100]*1000
Na_si = data_EDPR['Na_si'][0::1000]
Na_se = data_EDPR['Na_se'][0::1000]
Na_di = data_EDPR['Na_di'][0::1000]
Na_de = data_EDPR['Na_de'][0::1000]
K_si = data_EDPR['K_si'][0::1000]
K_se = data_EDPR['K_se'][0::1000]
K_di = data_EDPR['K_di'][0::1000]
K_de = data_EDPR['K_de'][0::1000]
Cl_si = data_EDPR['Cl_si'][0::1000]
Cl_se = data_EDPR['Cl_se'][0::1000]
Cl_di = data_EDPR['Cl_di'][0::1000]
Cl_de = data_EDPR['Cl_de'][0::1000]
Ca_si = data_EDPR['Ca_si'][0::1000]
Ca_se = data_EDPR['Ca_se'][0::1000]
Ca_di = data_EDPR['Ca_di']
Ca_de = data_EDPR['Ca_de']

### Panel A ###
ax1.plot(t_PR, phi_sm_PR, ls='-', color='k')
ax1.set_title('PR $\phi\mathrm{_{sm}}$')
ax1.set_yticks([-65, 0])
ax1.set_xlim(10,20)
ax1.set_ylim(-75, 25)
axin1 = inset_axes(ax1, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax1.transAxes, loc=3)
axin1.plot(t_PR, phi_sm_PR, ls='-', color='k')
axin1.set_xticklabels([])
axin1.set_yticklabels([])
axin1.set_ylim(-78, 28)
axin1.set_xlim(0, 3600)

### Panel B ###
ax2.plot(t_PR, free_Ca_PR, ls='-', color='k')
ax2.set_title('PR $\mathrm{[Ca^{2+}]_{di}}$')
ax2.set_ylabel('a.u.')
ax2.set_xlim(10,20)
ax2.set_ylim(-10,260)
axin2 = inset_axes(ax2, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax2.transAxes, loc=3)
axin2.plot(t_PR, free_Ca_PR, ls='-', color='k')
axin2.set_ylim(-40,300)
axin2.set_xticklabels([])
axin2.set_yticklabels([])
axin2.set_xlim(0, 3600)

### Panel C ###
ax3.plot(t_phi, phi_sm, ls='-', color='k')
ax3.set_title('edPR $\phi\mathrm{_{sm}}$')
ax3.set_yticks([-65, 0])
ax3.set_xlim(10,20)
ax3.set_ylim(-75, 25)
axin3 = inset_axes(ax3, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax3.transAxes, loc=3)
axin3.plot(t_phi, phi_sm, ls='-', color='k')
axin3.set_xticklabels([])
axin3.set_yticklabels([])
axin3.set_ylim(-80, 28)
axin3.set_xlim(0, 3600)

### Panel D ###
ax4.plot(t_phi, free_Ca_EDPR*1e6, ls='-', color='k')
ax4.set_title('edPR free $\mathrm{[Ca^{2+}]_{di}}$')
ax4.set_ylabel('nM')
ax4.set_xlim(10,20)
axin4 = inset_axes(ax4, width="40%", height="40%", bbox_to_anchor=(0.0, 0.5, 1., 1.), bbox_transform=ax4.transAxes, loc=3)
axin4.plot(t_phi, free_Ca_EDPR*1e6, ls='-', color='k')
axin4.set_xticklabels([])
axin4.set_yticklabels([])
axin4.set_ylim(-20, 1150)
axin4.set_xlim(0, 3600)

### Panel E ###
l1 = ax5.plot(data_EDPR['t'][0::10000], E_Na_s)[0]
l2 = ax5.plot(data_EDPR['t'][0::10000], E_K_s)[0]
l3 = ax5.plot(data_EDPR['t'][0::10000], E_Cl_s)[0]
l4 = ax5.plot(data_EDPR['t'][0::10000], E_Ca_s)[0]
ax5.set_title('$E\mathrm{_{k,s}}$')
ax5.spines['bottom'].set_position('zero')
fig.legend([l1, l2, l3, l4], ['$\mathrm{Na^+}$', '$\mathrm{K^+}$', '$\mathrm{Cl^-}$', '$\mathrm{Ca^{2+}}$'], \
    loc=(0.4,0.56), ncol=2, fontsize='small', handlelength=1, handletextpad=0.4, columnspacing=0.4)
ax5.set_yticks([-80, 0, 100])
ax5.set_ylim(-80, 140)

### Panel F ###
l1 = ax6.plot(data_EDPR['t'][0::100], E_Na_d)
l2 = ax6.plot(data_EDPR['t'][0::100], E_K_d)
l3 = ax6.plot(data_EDPR['t'][0::100], E_Cl_d)
l4 = ax6.plot(data_EDPR['t'][0::100], E_Ca_d)
ax6.set_title('$E\mathrm{_{k,d}}$')
ax6.spines['bottom'].set_position('zero')
ax6.set_yticks([-80, 0, 100])
ax6.set_ylim(-80, 140)

### Panel G ###
l1 = ax7.plot(t, Na_si-Na_si[0], zorder=10)[0]
l2 = ax7.plot(t, Na_se-Na_se[0], zorder=11)[0]
l3 = ax7.plot(t, Na_di-Na_di[0], zorder=10)[0]
l4 = ax7.plot(t, Na_de-Na_de[0], zorder=10)[0]
ax7.spines['bottom'].set_position('zero')
ax7.set_title('$\Delta\mathrm{[Na^+]}$')
ax7.set_ylim(-5, 2.5)
fig.legend([l1, l2, l3, l4], ['si', 'se', 'di', 'de'], \
    loc=(0.45,0.2), ncol=2, fontsize='small', handlelength=1, handletextpad=0.4, columnspacing=0.4)

### Panel H ###
ax8.plot(t, K_si-K_si[0], zorder=10)
ax8.plot(t, K_se-K_se[0], zorder=10)
ax8.plot(t, K_di-K_di[0], zorder=10)
ax8.plot(t, K_de-K_de[0], zorder=10)
ax8.spines['bottom'].set_position('zero')
ax8.set_title('$\Delta\mathrm{[K^+]}$')
ax8.set_ylim(-1, 2)

### Panel I ###
ax9.plot(t, Cl_si-Cl_si[0], zorder=10)
ax9.plot(t, Cl_se-Cl_se[0], zorder=10)
ax9.plot(t, Cl_di-Cl_di[0], ':', zorder=10)
ax9.plot(t, Cl_de-Cl_de[0], ':', zorder=10)
ax9.set_title('$\Delta\mathrm{[Cl^-]}$')
ax9.set_xlabel('time [s]')
ax9.set_ylim(-2.6, 1.3)

### Panel J ###
ax10.plot(t, Ca_si-Ca_si[0], '--', zorder=11)
ax10.plot(t, Ca_se-Ca_se[0], zorder=10)
ax10.plot(t_phi, Ca_di-Ca_di[0], zorder=9)
ax10.plot(t_phi, Ca_de-Ca_de[0], zorder=9)
ax10.set_title('$\Delta\mathrm{[Ca^{2+}]}$')
ax10.set_xlabel('time [s]')
ax10.set_ylim(-0.2, 0.1)

ax9.set_xticks([0, 1800, 3600])
ax10.set_xticks([0, 1800, 3600])

axarr = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]

for ax in [ax1, ax3, ax5, ax6]:
    ax.set_ylabel('mV')

for ax in axarr[6:]:
    ax.set_ylabel('mM')

for ax in axarr[4:]:
    ax.set_xlim(0,3600)

for ax in [ax5, ax6, ax7, ax8]:
    ax.set_xticks([0, 1800, 3600])
    ax.set_xticklabels([])

for ax in axarr:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

panel = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
for i in range(0,10):
    if i == 5 or i==9:
        axarr[i].text(0.13, 1.35, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    else:
        axarr[i].text(-0.1, 1.35, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')


fig.align_ylabels(axarr)
plt.tight_layout()
plt.savefig('figure6.eps', dpi=600)
