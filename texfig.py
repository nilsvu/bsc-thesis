# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
mpl.use('pgf')

default_width = 5.78853 # in inches
default_ratio = (np.sqrt(5.0)-1.0)/2.0 # golden mean
 
mpl.rcParams.update({
    "text.usetex": True,                # use inline math for ticks
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,               # don't setup fonts from rc parameters
    "font.family": "serif",             # use serif/main font for text elements
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "text.fontsize": 10,
    "title.fontsize": 8,
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": [default_width, default_width*default_ratio],     # default fig size
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        r"\newcommand{\alphaM}{{\alpha_{\mathrm{M}}}}", # commands defined in document
        r"\newcommand{\alphaMnot}{{\alpha_{\mathrm{M}0}}}",
        r"\newcommand{\cT}{{c_{\mathrm{T}}}}",
        r"\newcommand{\betaexp}{\beta}",
        r"\newcommand{\ofmetr}[1]{_#1}",
        r"\newcommand{\alphaMofmetr}[1]{\alphaM\ofmetr{#1}}",
        r"\newcommand{\mofmetr}[1]{m\ofmetr{#1}}",
        r"\newcommand{\cTofmetr}[1]{\cT\ofmetr{#1}}",
        r"\newcommand{\qofmetr}[1]{q\ofmetr{#1}}",
    ],
})

import matplotlib.pyplot as plt

 
# Simple plot
def figure(width=default_width, ratio=default_ratio, pad=0, *args, **kwargs):
    fig = plt.figure(figsize=(width, width*ratio), *args, **kwargs)
    fig.set_tight_layout({
        'pad': pad
    })
    return fig
    
def subplots(width=default_width, ratio=default_ratio, *args, **kwargs):
    fig, axes = plt.subplots(figsize=(width, width*ratio), *args, **kwargs)
    fig.set_tight_layout({
        'pad': 0
    })
    return fig, axes

def savefig(filename, *args, **kwargs):
    plt.savefig(filename + '.pdf', *args, **kwargs)
    plt.savefig(filename + '.pgf', *args, **kwargs)
