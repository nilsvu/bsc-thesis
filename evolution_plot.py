# -*- coding: utf-8 -*-

import numpy as np
import texfig
import matplotlib.pyplot as plt
import os

tex_width = 5.78853 # in inches

bg_legend_handle = plt.Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

def legend_outside(ncol, extra_text):
    handles, labels = plt.gca().get_legend_handles_labels()
    lgd = plt.legend(handles, labels, loc='upper center', ncol=ncol, bbox_to_anchor=(-0.15, -0.3))
    import matplotlib.offsetbox as offsetbox 
    txt=offsetbox.TextArea(extra_text, textprops=dict(size=lgd.get_texts()[0].get_fontsize()))
    box = lgd._legend_box
    box.get_children().append(txt) 
    box.set_figure(box.figure)
    return lgd

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

def single_plot(files_prefix, bg_parameters, *args, **kwargs):
    plt.clf()
    fig = texfig.figure(width=tex_width)

    plot_parametric_evolution(files_prefix=files_prefix, *args, **kwargs)

    plt.xscale('log')
    plt.yscale('log')
    
    plt.xlabel(r'scale factor \(a\)')
    plt.ylabel(r'tensor perturbations \(|h|\)')
    
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles + [ bg_legend_handle ], labels + [ "for " + bg_parameters ], loc='lower left')
        
    texfig.savefig('plots/' + files_prefix)


# single_plot(files_prefix="varying_aM", bg_parameters=r"$k=0.01$, $\cT=1$", plabel=r'\alphaM', LCDM_pvalue=0)
# single_plot(files_prefix="varying_k", bg_parameters=r"$\alphaM=0$, $\cT=1$", plabel='k')
# single_plot(files_prefix="varying_cT", bg_parameters=r"$k=0.01$, $\alphaM=0$", plabel=r'\cT', LCDM_pvalue=1)
#
# single_plot(files_prefix="varying_beta", bg_parameters=r"$k=0.01$, $\alphaMnot=-1$, $\cT=1$", plabel=r'\betaexp')
#
#
# # show growing modes and slope of the amplitude
# plt.clf()
# fig = texfig.figure(width=tex_width)
#
# plot_parametric_evolution(files_prefix="growing_aM", plabel=r'\alphaM', LCDM_pvalue=0)
#
# def slope_analytic(a, alpha_M, h_0):
#     return a**(-1 - alpha_M/2.) * h_0
#
# a = np.logspace(-5, 0, 100)
#
# plt.plot(a, slope_analytic(a, alpha_M=-2, h_0=10**-4.977515978085766), ls='dotted')
# plt.plot(a, slope_analytic(a, alpha_M=-3, h_0=10**0.02414219792993043), ls='dotted')
#
# plt.xscale('log')
# plt.yscale('log')
#
# plt.xlabel(r'scale factor \(a\)')
# plt.ylabel(r'tensor perturbations \(|h|\)')
#
# handles, labels = plt.gca().get_legend_handles_labels()
# plt.legend(handles + [ bg_legend_handle ], labels + [ "for  " + r"$k=0.01$, $\cT=1$" ], loc='lower left')
#
# texfig.savefig('plots/growing_aM')
#
#
# varying both alphaM and beta
#
# plt.clf()
# fig, axes = texfig.subplots(width=tex_width, nrows=2, ncols=2, sharex=True, sharey=True)
#
# for (i, row) in enumerate([["0", "0.1"], ["0.4", "1"]]):
#     for (j, beta_str) in enumerate(row):
#         ax = axes[i][j]
#         plt.sca(ax)
#
#         plot_parametric_evolution('varying_aM0_beta_' + beta_str, ur'\alphaMnot', LCDM_pvalue=0)
#
#         ax.set_title(ur'$\beta=' + beta_str + '$')
#
#         ax.set_xscale('log')
#         ax.set_yscale('log')
#
#         if i==1:
#             ax.set_xlabel(r'scale factor \(a\)')
#         if j==0:
#             ax.set_ylabel(r'tensor perturbations \(|h|\)')
#
# lgd = legend_outside(ncol=5, extra_text="for  " + r"$k=0.01$, $\cT=1$")
#
# texfig.savefig('plots/varying_aM0_beta', additional_artists=(lgd,), bbox_inches='tight')

#
# # bimetric
#
# plt.clf()
# fig, axes = texfig.subplots(width=tex_width, nrows=2, ncols=2, sharex=True, sharey=False)
#
# for (i, row) in enumerate([["-1", "-2"], ["-3", "-4"]]):
#     for (j, aMf_str) in enumerate(row):
#         ax = axes[i][j]
#         plt.sca(ax)
#
#         plot_evolution('bimetric_aMf_' + aMf_str + '_f.csv', color='blue', label=ur'reference metric perturbations $h\ofmetr{f}(a)$')
#         plot_evolution('bimetric_aMf_' + aMf_str + '_g.csv', color='black', label=ur'physical metric perturbations $h\ofmetr{g}(a)$')
#
#         ax.set_title(ur'$\alphaMofmetr{f}=' + aMf_str + '$')
#
#         ax.set_xscale('log')
#         ax.set_yscale('log')
#
#         if i==1:
#             ax.set_xlabel(r'scale factor \(a\)')
#         if j==0:
#             ax.set_ylabel(r'tensor perturbations \(|h|\)')
#
# lgd = legend_outside(ncol=2, extra_text="for  " + r"$k=0.01$, $\alphaMofmetr{g}=0$, $\cTofmetr{g}=\cTofmetr{f}=1$, $\mofmetr{g}=\mofmetr{f}=0$, $\qofmetr{g}=1$, $\qofmetr{f}=0$")
#
# texfig.savefig('plots/bimetric', additional_artists=(lgd,), bbox_inches='tight')

single_plot(files_prefix="varying_mg", bg_parameters=r"$k=0.01$", plabel=r'\mofmetr{g}', LCDM_pvalue=0)
