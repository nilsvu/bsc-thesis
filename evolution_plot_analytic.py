# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import texfig
from scipy.special import jv, yv

tex_width = 5.78853 # in inches

def h(eta, k, w, Cj=1, Cy=0):
    n = 2./(1.+3.*w)
    p = n - 1./2.
    return eta**(-p) * (Cj*jv(p, k*eta) + Cy*yv(p, k*eta))


eta = np.logspace(-5, 1, 100)

k = np.array([10, 20, 30])

plt.clf()
#fig = texfig.figure(width=tex_width)

for k_i in k:
    plt.plot(eta, h(eta, k=k_i, w=0))

plt.xscale('log')

plt.xlabel(r'scale factor \(a\)')
plt.ylabel(r'tensor perturbations \(|h|\)')

#plt.legend(loc='lower left')

#texfig.savefig('plots/' + files_prefix)
plt.show()
