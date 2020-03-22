import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('article', w=1, h=3)

fig = plt.figure()
gs = gridspec.GridSpec(3, 4)
ax0 = plt.subplot(gs[0,1:3])
ax1 = plt.subplot(gs[1,0:2])
ax2 = plt.subplot(gs[1,2:])
ax3 = plt.subplot(gs[2,0:2])
ax4 = plt.subplot(gs[2,2:])

colors = ['#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

l = []

for N in range(0,12):

    data = np.load('../data/figure4_' + str(N+1) + '.npz')

    t = data['t']/60
    phi_sm = data['phi_sm']*1000
    phi_dm = data['phi_dm']*1000
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

    if N < 6:
        ls = ':'
        zorder = 11
    else:
        ls = '-'
        zorder = 10

    l.append(ax0.plot(t, phi_sm, ls=ls, color=colors[N], zorder=zorder)[0])
    ax1.plot(t, Na_se, ls=ls, color=colors[N], zorder=zorder)
    ax2.plot(t, K_se, ls=ls, color=colors[N], zorder=zorder)
    ax3.plot(t, Cl_se, ls=ls, color=colors[N], zorder=zorder)
    ax4.plot(t, Ca_se, ls=ls, color=colors[N], zorder=zorder)


fig.legend([l[0], l[1], l[2], l[3], l[4], l[5]], ['$g\mathrm{_{Na,leak}}$', '$g\mathrm{_{K,leak}}$', '$g\mathrm{_{Cl,leak}}$', r'$\rho$', '$U\mathrm{_{kcc2}}$', '$U\mathrm{_{nkcc1}}$'], \
    loc=(0.04,0.70), title='$\downarrow 15 \%$')

fig.legend([l[6], l[7], l[8], l[9], l[10], l[11]], ['$g\mathrm{_{Na,leak}}$', '$g\mathrm{_{K,leak}}$', '$g\mathrm{_{Cl,leak}}$', r'$\rho$', '$U\mathrm{_{kcc2}}$', '$U\mathrm{_{nkcc1}}$'], \
    loc=(0.78,0.70), title=r'$\uparrow 15 \%$')


ax0.set_title('$\phi\mathrm{_{sm}}$')
ax1.set_title('$\mathrm{[Na^+]_{se}}$')
ax2.set_title('$\mathrm{[K^+]_{se}}$')
ax3.set_title('$\mathrm{[Cl^-]_{se}}$')
ax4.set_title('$\mathrm{[Ca^{2+}]_{se}}$')

ax0.set_ylabel('mV')
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_ylabel('mM')

ax1.set_xticklabels([])
ax2.set_xticklabels([])

ax0.set_xlabel('time [min]')
ax3.set_xlabel('time [min]')
ax4.set_xlabel('time [min]')

ax0.set_ylim(-71, -64)
ax0.set_yticks([-70, -65])
ax2.set_ylim(5.65, 6.30)
ax4.set_yticks([1.09994, 1.09996])
ax4.set_yticklabels(['1.09994', '1.09996'])

for ax in [ax0, ax1, ax2, ax3, ax4]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0,3)

axarr = [ax0, ax1, ax2, ax3, ax4]
panel = ['A', 'B', 'C', 'D', 'E']
for i in range(0,5):
    axarr[i].text(-0.1, 1.2, panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

fig.align_ylabels([ax1, ax3])
fig.align_ylabels([ax2, ax4])
plt.tight_layout()
plt.savefig('figure4.eps', dpi=600)
