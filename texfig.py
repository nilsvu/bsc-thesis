# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
#mpl.use('pgf')

default_width = 5.78853 # in inches
default_ratio = (np.sqrt(5.0)-1.0)/2.0 # golden mean
 
mpl.rcParams.update({                   # setup matplotlib to use latex for output
    "pgf.texsystem": "xetex",           # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "text.fontsize": 10,
    "title.fontsize": 10,
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": [default_width, default_width*default_ratio],     # default fig size
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
    ]
})
 
import matplotlib.pyplot as plt

 
# Simple plot
def figure(width=default_width, ratio=default_ratio, *args, **kwargs):
    fig = plt.figure(figsize=(width, width*ratio), *args, **kwargs)
    fig.set_tight_layout({
        'pad': 0
    })
    return fig
    
def subplots(width=default_width, ratio=default_ratio, *args, **kwargs):
    fig, axes = plt.subplots(figsize=(width, width*ratio), *args, **kwargs)
    fig.set_tight_layout({
        'pad': 0
    })
    return fig, axes

def savefig(filename):
    plt.savefig(filename + '.pdf')
    plt.savefig(filename + '.pgf')
