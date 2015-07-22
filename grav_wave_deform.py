# -*- coding: utf-8 -*-

import numpy as np
import texfig
import matplotlib.pyplot as plt
import scipy.constants as const


def plot_particles(phi, A=0.25, ax=None, n=8, pol='+', title=None):
    if ax is None:
        ax = plt.gca()
    alpha = np.linspace(0, 2*const.pi, n+1)

    rot = 0
    if pol == 'x':
        rot = const.pi/8.

    a = A * np.sin(phi)
    xy = ((1 + a)*np.cos(alpha), (1 - a)*np.sin(alpha))
    # rotation
    R = ((np.cos(rot), np.sin(rot)), (-np.sin(rot), np.cos(rot)))
    xy = (R[0][0]*xy[0] + R[0][1]*xy[1], R[1][0]*xy[0] + R[1][1]*xy[1])
    
    xy = np.dot(R,xy)
    
    ax.scatter(xy[0], xy[1], lw=1, c='black', s=20)
    
    if title is not None:
        ax.set_title('$'+title+'$', y=1.25)
    
    extra = A+0.2
    ax.set_xlim(-1-extra, 1+extra)
    ax.set_ylim(-1-extra, 1+extra)
    ax.grid(True, alpha=0.4)
    # ax.axis('off')
    for tic in ax.xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
        tic.label1On = tic.label2On = False
    for tic in ax.yaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
        tic.label1On = tic.label2On = False
    

# tensorial deformation figure

# fig = texfig.figure(pad=1)
#
# n = 12
# m = 5
# titles = ['0', r'\frac{\pi}{2}', r'\pi', r'\frac{3\pi}{2}', r'2\pi']
# add = []
# for i in np.arange(2*m):
#     ax = fig.add_subplot(2,m,i+1, aspect='equal')
#     pol = '+'
#     j = i
#     if i >= m:
#         pol = 'x'
#         j -= m
#     if j == 0:
#         if pol == 'x':
#             poltxt = r'cross'
#         else:
#             poltxt = r'plus'
#         t = ax.text(-0.2, 0.5, r'$\h'+poltxt+'$', horizontalalignment='right', verticalalignment='center', transform=ax.transAxes)
#         add.append(t)
#     title = None
#     if i < m:
#         title = titles[j]
#     plot_particles(phi=j*2*const.pi/(m-1), n=n, pol=pol, ax=ax, title=title)
#
# texfig.savefig('plots/grav_wave_deform', additional_artists=add, bbox_inches='tight')


# paging animation

def page_plot(p, f, prefix, p_front=0, alternating=False):
    if alternating:
        f = f / 2.
        if p % 2 == 0:
            pol = '+'
            pphi = p
        else:
            pol = 'x'
            pphi = p - 3
    else:
        pol = '+'
        pphi = p

    phi = pphi * f

    plt.clf()
    fig = texfig.figure(width=1.5, ratio=1)
    ax = fig.add_subplot(111, aspect='equal')
    plot_particles(phi=phi, ax=ax, pol=pol)
    ax.axis('off')
    texfig.savefig('paging_animation/' + prefix + str(p+1+p_front))

for p in np.arange(70):
    page_plot(p=p, f=const.pi/8, prefix='alternating_', p_front=4, alternating=True)
#    page_plot(p=p, f=const.pi/8, prefix='continuous_', p_front=2)
    print(str(p+1) + ' done.')
