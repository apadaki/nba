import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
   
def plot_trends(times_inter, diffs_inter, matchup, pathname, volume=0):
    times = [t/60 for t in times_inter] # scale to minutes
    diffs = diffs_inter

    fig,ax = plt.subplots()
    plt.plot(times, diffs, 'b', lw=1)

    xtrans = ax.get_xaxis_transform()
    plt.axhline(y=0, color='black', linestyle='--', alpha=0.6)
    plt.axvline(x=12*1, color='g', linestyle='--', alpha=0.3)
    plt.axvline(x=24*1, color='g', linestyle='--', alpha=0.3)
    plt.axvline(x=36*1, color='g', linestyle='--', alpha=0.3)  
    plt.axvline(x=48*1, color='g', linestyle='-', lw=2)
    plt.text(6*1,  0.01, '(Q1)', transform=xtrans, color='r', ha='center')
    plt.text(18*1, 0.01, '(Q2)', transform=xtrans, color='r', ha='center')
    plt.text(30*1, 0.01, '(Q3)', transform=xtrans, color='r', ha='center')
    plt.text(42*1, 0.01, '(Q4)', transform=xtrans, color='r', ha='center')

    ax.tick_params(labelright=True)

    x_ticks = np.arange(0, max(48, max(times)), 12)
    plt.xticks(x_ticks)

    props = dict(boxstyle='round', facecolor='w', alpha=0.5)
    ax.text(0.05, 0.95, 'avg_diff = {}'.format('%+d' % round(volume, 2)), transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

    plt.xlim(xmin=0,xmax=max(48*1, max(times)))
    plt.xlabel('in-game time elapsed (min)')
    plt.ylabel('(home-away) point differential')
    plt.title('Game Trends: {}'.format(matchup))
    plt.savefig(pathname)