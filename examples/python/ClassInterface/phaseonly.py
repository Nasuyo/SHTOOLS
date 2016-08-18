#!/usr/bin/env python
"""Test the phaseonly keyword."""

import matplotlib.pyplot as plt
import pyshtools
import numpy as np


def example():
    """Plot random phase and Gaussian random variable spectra."""
    ldata = 200
    degrees = np.arange(ldata+1, dtype=float)
    degrees[0] = np.inf
    power = degrees**(-1)

    clm1 = pyshtools.SHCoeffs.from_random(power, phaseonly=False)
    clm2 = pyshtools.SHCoeffs.from_random(power, phaseonly=True)

    fig, ax = plt.subplots()
    ax.plot(clm1.get_powerperdegree(), label='Gaussian coefficients')
    ax.plot(clm2.get_powerperdegree(), label='Random phase coefficients')
    ax.set(xscale='log', yscale='log', xlabel='degree l',
           ylabel='power per degree l')
    ax.grid(which='both')
    ax.legend()

    plt.show()


def main():
    example()


if __name__ == "__main__":
    main()
