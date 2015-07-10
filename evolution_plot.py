# -*- coding: utf-8 -*-

import numpy as np
import texfig
import matplotlib.pyplot as plt
import os

tex_width = 5.78853 # in inches

def plot_evolution(filename, **kwargs):
    data = np.loadtxt('data/' + filename, delimiter=",")
    a = 10**data[:,0]
    h = 10**data[:,1]

    plt.plot(a, h, **kwargs)
    

def plot_parametric_evolution(files_prefix, plabel, LCDM_pvalue=None):
    
    for filename in os.listdir("data"):
        if filename.startswith(files_prefix + '_'):
            pvalue_str = filename.replace(files_prefix + '_', '').replace('.csv', '')
            pvalue = float(pvalue_str) if '.' in pvalue_str else int(pvalue_str)
            isLCDM = LCDM_pvalue is not None and pvalue == LCDM_pvalue
                        
            label = "$" + plabel + "=" + str(pvalue) + "$"
            options = {
                'label': label,
            }
            if isLCDM:
                label += " ($\Lambda$CDM)"
                options['color'] = 'black'
                options['lw'] = 2

            plot_evolution(filename, **options)

def single_plot(files_prefix, *args, **kwargs):
    plt.clf()
    fig = texfig.figure(width=tex_width)

    plot_parametric_evolution(files_prefix=files_prefix, *args, **kwargs)

    plt.xscale('log')
    plt.yscale('log')
    
    plt.xlabel(r'scale factor \(a\)')
    plt.ylabel(r'tensor perturbations \(|h|\)')
    
    plt.legend(loc='lower left')
    
    texfig.savefig('plots/' + files_prefix)


single_plot(files_prefix="varying_aM", plabel=r'\alphaM', LCDM_pvalue=0)
single_plot(files_prefix="varying_k", plabel='k')
single_plot(files_prefix="varying_cT", plabel=r'\cT', LCDM_pvalue=1)

single_plot(files_prefix="varying_beta", plabel=r'\betaexp')

# show growing modes and slope of the amplitude
plt.clf()
fig = texfig.figure(width=tex_width)

plot_parametric_evolution(files_prefix="growing_aM", plabel=r'\alphaM', LCDM_pvalue=0)

def slope_analytic(a, alpha_M, h_0):
    return a**(-1 - alpha_M/2.) * h_0

a = np.logspace(-5, 0, 100)

plt.plot(a, slope_analytic(a, alpha_M=-2, h_0=10**-4.977515978085766), ls='dotted')
plt.plot(a, slope_analytic(a, alpha_M=-3, h_0=10**0.02414219792993043), ls='dotted')

plt.xscale('log')
plt.yscale('log')

plt.xlabel(r'scale factor \(a\)')
plt.ylabel(r'tensor perturbations \(|h|\)')

plt.legend(loc='lower left')

texfig.savefig('plots/growing_aM')


# varying both alphaM and beta

plt.clf()
fig, axes = texfig.subplots(width=tex_width, nrows=2, ncols=2, sharex=True, sharey=True)

for (i, row) in enumerate([["0", "0.1"], ["0.4", "1"]]):
    for (j, beta_str) in enumerate(row):
        ax = axes[i][j]
        plt.sca(ax)

        plot_parametric_evolution('varying_aM0_beta_' + beta_str, ur'\alphaMnot', LCDM_pvalue=0)

        ax.set_title(ur'$\beta=' + beta_str + '$')

        ax.set_xscale('log')
        ax.set_yscale('log')

        if i==1:
            ax.set_xlabel(r'scale factor \(a\)')
        if j==0:
            ax.set_ylabel(r'tensor perturbations \(|h|\)')

texfig.savefig('plots/varying_aM0_beta')


# bimetric

plt.clf()
fig, axes = texfig.subplots(width=tex_width, ratio=1, nrows=2, ncols=1, sharex=True, sharey=False)

for (i, aMf_str) in enumerate(["-3", "-4"]):
    ax = axes[i]
    plt.sca(ax)

    plot_evolution('bimetric_aMf' + aMf_str + '_g.csv', label=ur'physical metric perturbations $h\ofmetr{g}(a)$', color='black')
    plot_evolution('bimetric_aMf' + aMf_str + '_f.csv', label=ur'reference metric perturbations $h\ofmetr{f}(a)$', color='blue')

    ax.set_title(ur'$\alphaMofmetr{f}=' + aMf_str + '$')

    ax.set_xscale('log')
    ax.set_yscale('log')

    if i==1:
        ax.set_xlabel(r'scale factor \(a\)')
    ax.set_ylabel(r'tensor perturbations \(|h|\)')

texfig.savefig('plots/bimetric')
