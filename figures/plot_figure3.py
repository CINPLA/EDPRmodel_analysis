import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('article', w=1, h=3)

data = np.load('../data/figure3.npz')

t = data['t']
phi_sm = data['phi_sm']
phi_dm = data['phi_dm']
phi_si = data['phi_si']
phi_se = data['phi_se']
phi_di = data['phi_di']
phi_de = data['phi_de']
E_Na_s = data['E_Na_s']
E_Na_d = data['E_Na_d']
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
Ca_de = data['Ca_de']

E_K_s = data['E_K_s']
E_K_d = data['E_K_d']
E_Cl_s = data['E_Cl_s']
E_Cl_d = data['E_Cl_d']
E_Ca_s = data['E_Ca_s']
E_Ca_d = data['E_Ca_d']
sigma_i = data['sigma_i']
sigma_e = data['sigma_e']
ATP_pump = data['ATP_pump']
ATP_Ca = data['ATP_Ca']

fig, axarr = plt.subplots(6,2, sharex='col')

### Panel A ###
axarr[0,0].plot(t, phi_sm*1000, 'k')
axarr[0,0].set_title('$\phi\mathrm{_{sm}}$')
axarr[0,0].set_ylabel('mV')
axarr[0,0].spines['top'].set_visible(False)
axarr[0,0].spines['right'].set_visible(False)
axarr[0,0].set_yticks([-65, 0])

### Panel B ###
axarr[0,1].plot(t, phi_dm*1000, 'k')
axarr[0,1].set_title('$\phi\mathrm{_{dm}}$')
axarr[0,1].set_ylabel('mV')
axarr[0,1].spines['top'].set_visible(False)
axarr[0,1].spines['right'].set_visible(False)
axarr[0,1].set_yticks([-65, 0])

### Panel C ###
axarr[1,0].plot(t, phi_se*1000, 'k')
axarr[1,0].set_title('$\phi\mathrm{_{se}}$')
axarr[1,0].set_ylabel('mV')
axarr[1,0].spines['top'].set_visible(False)
axarr[1,0].spines['right'].set_visible(False)
axarr[1,0].set_ylim(-8, 8)
axarr[1,0].set_yticks([-5, 0, 5])

### Panel D ###
axarr[1,1].plot(t, np.ones(len(phi_se))*phi_de, 'k', zorder=10)
axarr[1,1].set_title('$\phi\mathrm{_{de}}$')
axarr[1,1].set_ylabel('mV')
axarr[1,1].spines['top'].set_visible(False)
axarr[1,1].spines['right'].set_visible(False)
axarr[1,1].set_ylim(-8, 8)
axarr[1,1].set_yticks([-5, 0, 5])

### Panel E ###
l1 = axarr[2,0].plot(t, Na_si-Na_si[0], zorder=10)[0]
l2 = axarr[2,0].plot(t, Na_se-Na_se[0], zorder=11)[0]
l3 = axarr[2,0].plot(t, Na_di-Na_di[0], zorder=10)[0]
l4 = axarr[2,0].plot(t, Na_de-Na_de[0], zorder=10)[0]
axarr[2,0].set_title('$\Delta\mathrm{[Na^+]}$')
axarr[2,0].set_ylabel('mM')
axarr[2,0].spines['top'].set_visible(False)
axarr[2,0].spines['right'].set_visible(False)
axarr[2,0].spines['bottom'].set_position('zero')
fig.legend([l1, l2, l3, l4], ['si', 'se', 'di', 'de'], \
    loc=(0.43,0.48), ncol=2, fontsize='small', handlelength=0.8, handletextpad=0.4, columnspacing=0.4)
axarr[2,0].set_ylim(-2.5, 1.5)
axarr[2,0].set_yticks([-2, 0])

### Panel F ###
axarr[2,1].plot(t, K_si-K_si[0], zorder=10)
axarr[2,1].plot(t, K_se-K_se[0], zorder=10)
axarr[2,1].plot(t, K_di-K_di[0], zorder=10)
axarr[2,1].plot(t, K_de-K_de[0], zorder=10)
axarr[2,1].set_title('$\Delta\mathrm{[K^+]}$')
axarr[2,1].set_ylabel('mM')
axarr[2,1].spines['top'].set_visible(False)
axarr[2,1].spines['right'].set_visible(False)
axarr[2,1].spines['bottom'].set_position('zero')
axarr[2,1].set_ylim(-1, 1.5)
axarr[2,1].set_yticks([0, 1])

### Panel G ###
axarr[3,0].plot(t, Cl_si-Cl_si[0], zorder=10)
axarr[3,0].plot(t, Cl_se-Cl_se[0], ':', zorder=11)
axarr[3,0].plot(t, Cl_di-Cl_di[0], ':', zorder=10)
axarr[3,0].plot(t, Cl_de-Cl_de[0], zorder=10)
axarr[3,0].set_title('$\Delta\mathrm{[Cl^-]}$')
axarr[3,0].set_ylabel('mM')
axarr[3,0].spines['top'].set_visible(False)
axarr[3,0].spines['right'].set_visible(False)
axarr[3,0].spines['bottom'].set_position('zero')
axarr[3,0].set_ylim(-1, 0.5)
axarr[3,0].set_yticks([-1, 0])

### Panel H ###
axarr[3,1].plot(t, Ca_si-Ca_si[0], ':', zorder=11)
axarr[3,1].plot(t, Ca_se-Ca_se[0], zorder=10)
axarr[3,1].plot(t, Ca_di-Ca_di[0], zorder=9)
axarr[3,1].plot(t, Ca_de-Ca_de[0], zorder=9)
axarr[3,1].set_title('$\Delta\mathrm{[Ca^{2+}]}$')
axarr[3,1].set_ylabel('mM')
axarr[3,1].spines['top'].set_visible(False)
axarr[3,1].spines['right'].set_visible(False)
axarr[3,1].spines['bottom'].set_position('zero')
axarr[3,1].set_ylim(-0.2, 0.1)
axarr[3,1].set_yticks([-0.2, 0])

### Panel I ###
l1 = axarr[4,0].plot(t, (E_Na_s-E_Na_s[0])*1000, zorder=10)[0]
l2 = axarr[4,0].plot(t, (E_K_s-E_K_s[0])*1000, zorder=10)[0]
l3 = axarr[4,0].plot(t, (E_Cl_s-E_Cl_s[0])*1000, zorder=10)[0]
l4 = axarr[4,0].plot(t, (E_Ca_s-E_Ca_s[0])*1000, zorder=10)[0]
axarr[4,0].set_title('$\Delta E\mathrm{_{k,s}}$')
axarr[4,0].set_ylabel('mV')
axarr[4,0].spines['top'].set_visible(False)
axarr[4,0].spines['right'].set_visible(False)
axarr[4,0].spines['bottom'].set_position('zero')
axarr[4,0].set_ylim(-2, 5)
fig.legend([l1, l2, l3, l4], ['$\mathrm{Na^+}$', '$\mathrm{K^+}$', '$\mathrm{Cl^-}$', '$\mathrm{Ca^{2+}}$'], \
    loc=(0.40,0.31), ncol=2, fontsize='small', handlelength=0.8, handletextpad=0.4, columnspacing=0.4)

### Panel J ###
axarr[4,1].plot(t, (E_Na_d-E_Na_d[0])*1000, zorder=11)
axarr[4,1].plot(t, (E_K_d-E_K_d[0])*1000, zorder=10)
axarr[4,1].plot(t, (E_Cl_d-E_Cl_d[0])*1000, zorder=10)
axarr[4,1].plot(t, (E_Ca_d-E_Ca_d[0])*1000, zorder=10)
axarr[4,1].set_title('$\Delta E\mathrm{_{k,d}}$')
axarr[4,1].set_ylabel('mV')
axarr[4,1].spines['top'].set_visible(False)
axarr[4,1].spines['right'].set_visible(False)
axarr[4,1].spines['bottom'].set_position('zero')
axarr[4,1].set_ylim(-35, 10)
axarr[4,1].set_yticks([-30, 0])

### Panel K ###
axarr[5,0].plot(t, (sigma_i-sigma_i[0])*1000, 'k:', label='$\sigma_i$')
axarr[5,0].plot(t, (sigma_e-sigma_e[0])*1000, 'k', label='$\sigma_e$')
axarr[5,0].legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='lower right', labelspacing=0.01)
axarr[5,0].set_title('$\Delta \sigma$')
axarr[5,0].set_ylabel('$\mu$S/m')
axarr[5,0].set_xlabel('time [s]')
axarr[5,0].set_xlim(0,60)
axarr[5,0].set_xticks([0, 10, 20, 30, 40, 50, 60])
axarr[5,0].set_yticks([-4, 0])
axarr[5,0].spines['top'].set_visible(False)
axarr[5,0].spines['right'].set_visible(False)

### Panel L ###
axarr[5,1].plot(t, ATP_pump, 'k:', label='pump')
axarr[5,1].plot(t, ATP_Ca, 'k', label='Ca$^{2+}$')
axarr[5,1].legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper left', labelspacing=0.2)
axarr[5,1].set_title('ATP')
axarr[5,1].spines['top'].set_visible(False)
axarr[5,1].spines['right'].set_visible(False)
axarr[5,1].set_xlabel('time [s]')
axarr[5,1].set_ylim(0,0.6e10)
axarr[5,1].set_xlim(0,60)
axarr[5,1].set_xticks([0, 10, 20, 30, 40, 50, 60])

panel = np.array([['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K', 'L']])
for i in range(0,6):
    for j in range(0,2):
        if i == 3 and j == 1 or i==4 and j==1:
            axarr[i,j].text(0.13, 1.35, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
        else:
            axarr[i,j].text(-0.1, 1.35, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

fig.align_ylabels(axarr)
plt.tight_layout()
plt.savefig('figure3.eps', dpi=600)
