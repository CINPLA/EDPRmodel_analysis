import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('article', w=1, h=3)

data_EDPR_weak = np.load('../data/figure5_EDPR_weak.npz')
data_PR_weak = np.load('../data/figure5_PR_weak.npz')
data_EDPR_strong = np.load('../data/figure5_EDPR_strong.npz')
data_PR_strong = np.load('../data/figure5_PR_strong.npz')

EDPR_weak_t = data_EDPR_weak['t']
EDPR_weak_sm = data_EDPR_weak['phi_sm']
EDPR_weak_dm = data_EDPR_weak['phi_dm']

PR_weak_t = data_PR_weak['t']
PR_weak_sm = data_PR_weak['Vs']
PR_weak_dm = data_PR_weak['Vd']

EDPR_strong_t = data_EDPR_strong['t']
EDPR_strong_sm = data_EDPR_strong['phi_sm']
EDPR_strong_dm = data_EDPR_strong['phi_dm']

PR_strong_t = data_PR_strong['t']
PR_strong_sm = data_PR_strong['Vs']
PR_strong_dm = data_PR_strong['Vd']

fig, big_axes = plt.subplots(2, 1)

for ax in big_axes:
    ax.tick_params(labelcolor=(1.,1.,1., 0.0), top=False, bottom=False, left=False, right=False)
    ax.tick_params(labelcolor=(1.,1.,1., 0.0), top=False, bottom=False, left=False, right=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

big_axes[0].set_title('Original PR Model')
big_axes[1].set_title('edPR Model')

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

### Panel A ###
ax1.plot(PR_weak_t/1000, PR_weak_sm, 'k', label='soma')
ax1.plot(PR_weak_t/1000, PR_weak_dm, 'k:', label='dendrite')
ax1.set_xlim([17.70,17.74])
ax1.set_ylabel('mV')
ax1.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')

### Panel B ###
ax2.plot(PR_strong_t/1000, PR_strong_sm, 'k')
ax2.plot(PR_strong_t/1000, PR_strong_dm, 'k:')
ax2.set_xlim([10.06,10.10])
ax2.set_xticks([10.06, 10.08, 10.10])

### Panel C ###
ax3.plot(EDPR_weak_t, EDPR_weak_sm*1000, 'k')
ax3.plot(EDPR_weak_t, EDPR_weak_dm*1000, 'k:')
ax3.set_xlim([18.52,18.56])
ax3.set_ylabel('mV')
ax3.set_xlabel('time [s]')

### Panel D ###
ax4.plot(EDPR_strong_t, EDPR_strong_sm*1000, 'k')
ax4.plot(EDPR_strong_t, EDPR_strong_dm*1000, 'k:')
ax4.set_xlim([10.01,10.05])
ax4.set_xlabel('time [s]')
ax4.set_xticks([10.01, 10.03, 10.05])

for ax in [ax1, ax2, ax3, ax4]:
    ax.set_yticks([-65, 0, 20])
    ax.set_ylim(-70,25)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

axarr = [ax1, ax2, ax3, ax4]
panel = ['A', 'B', 'C', 'D']
for i in range(0,4):
    axarr[i].text(0.2, 1., panel[i], transform=axarr[i].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

fig.set_facecolor('w')
plt.tight_layout()
plt.savefig('figure5.eps', dpi=600)
