#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
import colors
from matplotlib import gridspec

red = ["#e85c47"]
orange = ["#fdbe6e"]
green = ["#7dcca4"]
blue = ["#4173b3"]

beta = [0.8,0.5,0.1]

for i,c in enumerate(beta):
        red.append(colors.get_alpha_hex(red[0],beta[i]))
        orange.append(colors.get_alpha_hex(orange[0],beta[i]))
        green.append(colors.get_alpha_hex(green[0],beta[i]))
        blue.append(colors.get_alpha_hex(blue[0],beta[i]))
        
blue[1] = 'None'

#Make a line indicating the value at which operational
#entanglement converges at +- infinity interaction strength.
xNEG = np.linspace(-10,-100,1000)
xPOS = np.linspace(10,100,1000)
exactNEG = xNEG - xNEG + 14/15*np.log(2)
exactPOS = xPOS - xPOS + np.log(2)

with plt.style.context('../IOP_large.mplstyle'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files

    #14 particles
    
    datFileNEG_M28N14 = 'EOPA28F14l14a2NEG.dat'
    dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)
    
    datFile_M28N14 = 'EOPA28F14l14a2.dat'
    data_M28N14 = np.loadtxt(datFile_M28N14)
    
    #Load energies (can choose them arbitrarily from any of the .dat files)
    energiesNEG_M28N14 = dataNEG_M28N14[:,0]
    energies_M28N14 = data_M28N14[:,0]

    #Save Operational Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables
    #11 particles
    
    #Spatial Von Neumann
    s1NEG_M28N14spatial = dataNEG_M28N14[:,2]
    s1_M28N14spatial = data_M28N14[:,2]

    #Operational Von Neumann
    s1NEG_M28N14 = dataNEG_M28N14[:,3]
    s1_M28N14 = data_M28N14[:,3]
    
    #Operational 2nd Renyi
    s2NEG_M28N14 = dataNEG_M28N14[:,5]
    s2_M28N14 = data_M28N14[:,5]
    
    #Operational (S_op^(5)) 2nd Renyi
    s2NEG_M28N14op5 = dataNEG_M28N14[:,8]
    s2_M28N14op5 = data_M28N14[:,8]
    
    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(1, 2)

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    #ax1 = fig.add_subplot(221)
    ax1.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point
    ax1.plot(energiesNEG_M28N14, s1NEG_M28N14spatial, 'o',  label=r'$S_{1}$', markersize = 3, markerfacecolor = red[1], markeredgewidth = '0.25', color=red[0])
    ax1.plot(energiesNEG_M28N14, s1NEG_M28N14, 'o', label=r'$S_{1}^{\rm{op}}$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color=orange[0])
    ax1.plot(energiesNEG_M28N14, s2NEG_M28N14, 'o',  label=r'$S_{2}^{\rm{op}}$', markersize = 3, markerfacecolor = green[1], markeredgewidth = '0.25',color=green[0])
    ax1.plot(energiesNEG_M28N14, s2NEG_M28N14op5, 'o', label=r'$S_{2}^{\rm{op}(5)}$', markersize = 3, markerfacecolor = blue[1], markeredgewidth = '0.25',color=blue[0])
    ax1.set_xlim(-energies_M28N14[-1], -energies_M28N14[0])
    ax1.set_ylim(0,3.45)
    #ax1.set_ylabel(r'$S_{\alpha}^{\rm{op}}(\ell)$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.set_xlabel(' ')
    
    #Legend
    lgnd = plt.legend(loc=(0.03,0.38),fontsize=7,handleheight=2, frameon=False)

    #lgnd.get_title().set_fontsize(7)
    #lgnd.get_title().set_position((0.01,0))

    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    #ax2 = fig.add_subplot(222)
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')
    ax2.plot(energies_M28N14, s1_M28N14spatial, 'o',  label=r'$1, S_{\alpha}$', markersize = 3, markerfacecolor = red[1], markeredgewidth = '0.25', color=red[0])
    ax2.plot(energies_M28N14, s1_M28N14, 'o', label=r'$1, S_{\alpha}^{\rm{op}}$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color=orange[0])
    ax2.plot(energies_M28N14, s2_M28N14, 'o',  label=r'$2, S_{\alpha}^{\rm{op}}$', markersize = 3, markerfacecolor = green[1], markeredgewidth = '0.25',color=green[0])
    ax2.plot(energies_M28N14, s2_M28N14op5, 'o', label=r'$2, S_{\alpha}^{\rm{op}(5)}$', markersize = 3, markerfacecolor = blue[1], markeredgewidth = '0.25',color=blue[0])
    ax2.text(0.05,3.1,r'$N=14$')
    ax2.set_xlim(energies_M28N14[0], energies_M28N14[-1])
    ax2.set_ylim(0,3.45)
    ax2.set_xscale('symlog', linthreshx = 0.000001)
    plt.xlabel(r'$V/t$',x=0)

    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('operationalEntanglementEntropiesN14.pdf', transparent=False)
    plt.show()
