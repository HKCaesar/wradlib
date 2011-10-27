#-------------------------------------------------------------------------------
# Name:        vis_example
# Purpose:
#
# Author:      heistermann
#
# Created:     26.10.2011
# Copyright:   (c) heistermann 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wradlib.vis as vis


if __name__ == '__main__':

    import numpy as np
    testdata = np.loadtxt('data/polar_dBZ.dat')
    vis.polar_plot(testdata, title='Reflectivity (dBZ)')

