import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('article', w=1, h=3)
fig, axarr = plt.subplots(5,2, sharex='col')

data = np.load('../data/figure8.npz')

t = data['t']

e_akkum_drift_e = data['e_akkum_drift_e']
e_akkum_diff_e = data['e_akkum_diff_e']
Na_akkum_drift_e = data['Na_akkum_drift_e']
Na_akkum_diff_e = data['Na_akkum_diff_e']
K_akkum_drift_e = data['K_akkum_drift_e']
K_akkum_diff_e = data['K_akkum_diff_e']
Cl_akkum_drift_e = data['Cl_akkum_drift_e']
Cl_akkum_diff_e = data['Cl_akkum_diff_e']
Ca_akkum_drift_e = data['Ca_akkum_drift_e']
Ca_akkum_diff_e = data['Ca_akkum_diff_e']

e_akkum_drift_i = data['e_akkum_drift_i']
e_akkum_diff_i = data['e_akkum_diff_i']
Na_akkum_drift_i = data['Na_akkum_drift_i']
Na_akkum_diff_i = data['Na_akkum_diff_i']
K_akkum_drift_i = data['K_akkum_drift_i']
K_akkum_diff_i = data['K_akkum_diff_i']
Cl_akkum_drift_i = data['Cl_akkum_drift_i']
Cl_akkum_diff_i = data['Cl_akkum_diff_i']
Ca_akkum_drift_i = data['Ca_akkum_drift_i']
Ca_akkum_diff_i = data['Ca_akkum_diff_i']

### Panel A1 ###
l1 = axarr[0,0].plot(t, Na_akkum_drift_i, zorder=10)[0]
l2 = axarr[0,0].plot(t, Na_akkum_diff_i, zorder=10)[0]
axarr[0,0].set_title('Axial transport ICS \n $\mathrm{Na^+}$')
axarr[0,0].set_ylabel('N')
axarr[0,0].spines['bottom'].set_position('zero')
fig.legend([l1, l2], ['drift', 'diffusion'], \
    loc=(0.37,0.81), fontsize='small', handlelength=1.2, handletextpad=0.4)

### Panel A2 ###
axarr[1,0].plot(t, K_akkum_drift_i, zorder=10)[0]
axarr[1,0].plot(t, K_akkum_diff_i, zorder=10)[0]
axarr[1,0].set_title('$\mathrm{K^+}$')
axarr[1,0].set_ylabel('N')
axarr[1,0].spines['bottom'].set_position('zero')

### Panel A3 ###
axarr[2,0].plot(t, Cl_akkum_drift_i, zorder=10)[0]
axarr[2,0].plot(t, Cl_akkum_diff_i, zorder=10)[0]
axarr[2,0].set_title('$\mathrm{Cl^-}$')
axarr[2,0].set_ylabel('N')
axarr[2,0].spines['bottom'].set_position('zero')

#### Panel A4 ###
axarr[3,0].plot(t, Ca_akkum_drift_i, zorder=10)[0]
axarr[3,0].plot(t, Ca_akkum_diff_i, zorder=10)[0]
axarr[3,0].set_title('$\mathrm{Ca^{2+}}$')
axarr[3,0].set_ylabel('N')
axarr[3,0].spines['bottom'].set_position('zero')

### Panel A5 ###
axarr[4,0].plot(t, e_akkum_drift_i, zorder=10)
axarr[4,0].plot(t, e_akkum_diff_i, zorder=10)
axarr[4,0].set_title('$\mathrm{e^+}$')
axarr[4,0].set_ylabel('N')
axarr[4,0].set_xlabel('time [s]')
axarr[4,0].set_xlim(0,30)
axarr[4,0].set_xticks([0,10,20,30])

### Panel B1 ###
l1 = axarr[0,1].plot(t, Na_akkum_drift_e, zorder=10)[0]
l2 = axarr[0,1].plot(t, Na_akkum_diff_e, zorder=10)[0]
axarr[0,1].set_title('Axial transport ECS \n $\mathrm{Na^+}$')
axarr[0,1].spines['bottom'].set_position('zero')

### Panel B2 ###
axarr[1,1].plot(t, K_akkum_drift_e, zorder=10)[0]
axarr[1,1].plot(t, K_akkum_diff_e, zorder=10)[0]
axarr[1,1].set_title('$\mathrm{K^+}$')
axarr[1,1].spines['bottom'].set_position('zero')

### Panel B3 ###
axarr[2,1].plot(t, Cl_akkum_drift_e, zorder=10)[0]
axarr[2,1].plot(t, Cl_akkum_diff_e, zorder=10)[0]
axarr[2,1].set_title('$\mathrm{Cl^-}$')
axarr[2,1].spines['bottom'].set_position('zero')

#### Panel B4 ###
axarr[3,1].plot(t, Ca_akkum_drift_e, zorder=10)[0]
axarr[3,1].plot(t, Ca_akkum_diff_e, zorder=10)[0]
axarr[3,1].set_title('$\mathrm{Ca^{2+}}$')
axarr[3,1].spines['bottom'].set_position('zero')

### Panel B5 ###
axarr[4,1].plot(t, e_akkum_drift_e, zorder=10)
axarr[4,1].plot(t, e_akkum_diff_e, zorder=10)
axarr[4,1].set_title('$\mathrm{e^+}$')
axarr[4,1].set_xlim(0,30)
axarr[4,1].set_xticks([0,10,20,30])
axarr[4,1].set_xlabel('time [s]')

# remove top and right borders
for i in range(5):
    for j in range(2):
        axarr[i,j].spines['top'].set_visible(False)
        axarr[i,j].spines['right'].set_visible(False)
        axarr[i,j].ticklabel_format(axis='y', style='sci', scilimits=(0,0))

axarr[4,1].set_xticks([0, 10, 20, 30])

panel = [['A1', 'B1'], ['A2', 'B2'], ['A3', 'B3'], ['A4', 'B4'], ['A5', 'B5']]
for i in range(5):
    for j in range(2):
        axarr[i,j].text(-0.05, 1.35, panel[i][j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

fig.align_ylabels(axarr[:,0])
plt.tight_layout()
plt.savefig('figures_pdf/figure8.pdf', dpi=300)
