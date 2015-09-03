

# Topics: line, color, LineCollection, cmap, colorline, codex
'''
Defines a function colorline that draws a (multi-)colored 2D line with coordinates x and y.
The color is taken from optional data in z, and creates a LineCollection.

z can be:
- empty, in which case a default coloring will be used based on the position along the input arrays
- a single number, for a uniform color [this can also be accomplished with the usual plt.plot]
- an array of the length of at least the same length as x, to color according to this data
- an array of a smaller length, in which case the colors are repeated along the curve

The function colorline returns the LineCollection created, which can be modified afterwards.

See also: plt.streamplot
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib.colors import LogNorm
from matplotlib.colors import Normalize

def fixlogax(ax, a='x'):
    if a == 'x':
        labels = [item.get_text() for item in ax.get_xticklabels()]
        positions = ax.get_xticks()
        # print positions
        # print labels
        for i in range(len(positions)):
            labels[i] = '$10^{'+str(int(np.log10(positions[i])))+'}$'
        if np.size(np.where(positions == 1)) > 0:
            labels[np.where(positions == 1)[0][0]] = '$1$'
        if np.size(np.where(positions == 10)) > 0:
            labels[np.where(positions == 10)[0][0]] = '$10$'
        if np.size(np.where(positions == 0.1)) > 0:
            labels[np.where(positions == 0.1)[0][0]] = '$0.1$'
        # print positions
        # print labels
        ax.set_xticklabels(labels)
    if a == 'y':
        labels = [item.get_text() for item in ax.get_yticklabels()]
        positions = ax.get_yticks()
        # print positions
        # print labels
        for i in range(len(positions)):
            labels[i] = '$10^{'+str(int(np.log10(positions[i])))+'}$'
        if np.size(np.where(positions == 1)) > 0:
            labels[np.where(positions == 1)[0][0]] = '$1$'
        if np.size(np.where(positions == 10)) > 0:
            labels[np.where(positions == 10)[0][0]] = '$10$'
        if np.size(np.where(positions == 0.1)) > 0:
            labels[np.where(positions == 0.1)[0][0]] = '$0.1$'
        # print positions
        # print labels
        ax.set_yticklabels(labels)

def define_figure_style(mode='lines', c='w'):
    mpl.rcParams['lines.linewidth']=2.0
    mpl.rcParams['lines.color']='black'
    mpl.rcParams['text.usetex']=True
    mpl.rcParams["text.latex.preamble"].append(r'\usepackage[dvips]{graphicx}\usepackage{xfrac}\usepackage{amssymb}')
    mpl.rcParams['xtick.labelsize']=10
    mpl.rcParams['ytick.labelsize']=10
    mpl.rcParams['figure.dpi']=300
    mpl.rcParams['savefig.dpi']=300
    mpl.rcParams['legend.numpoints']=1
    mpl.rcParams['legend.fontsize']='small'
    if c=='w':
        mpl.rcParams['lines.color']='black'#	mpl.rcParams['text.usetex']=True
        mpl.rcParams['axes.edgecolor']='black'	
        mpl.rcParams['axes.labelcolor']='black'
        mpl.rcParams['text.color']='black'	
        mpl.rcParams['xtick.color']='black'	
        mpl.rcParams['ytick.color']='black'	
        mpl.rcParams['axes.facecolor']='white'
        color_list=('#CC6677','#117733','#4477AA','#DDCC77','#88CCEE','#AA4499')
        mpl.rcParams['axes.color_cycle']=color_list
        mpl.rcParams['figure.facecolor']='white'	
        mpl.rcParams['axes.labelweight']='normal'
    if c=='k':
        mpl.rcParams['lines.color']='white'        
        mpl.rcParams['axes.edgecolor']='white'	
        mpl.rcParams['axes.labelcolor']='white'	
        mpl.rcParams['text.color']='white'	
        mpl.rcParams['xtick.color']='white'	
        mpl.rcParams['ytick.color']='white'	
        mpl.rcParams['axes.facecolor']='black'
        color_list=('#809BC8','#FF6666','#64C204','#FFCC66','#FFFFCC','#FFFFFF')
        mpl.rcParams['axes.color_cycle']=color_list
        mpl.rcParams['figure.facecolor']='black'	
        mpl.rcParams['axes.labelweight']='bold'
    if mode=='lines':
        mpl.rcParams['figure.figsize']=3.375, 3.375
        mpl.rcParams['figure.subplot.top']=0.95
        mpl.rcParams['figure.subplot.right']=0.95
        mpl.rcParams['figure.subplot.bottom']=0.15
        mpl.rcParams['figure.subplot.left']=0.18
    if mode=='doublex':
        mpl.rcParams['figure.figsize']=3.375, 3.375
        mpl.rcParams['figure.subplot.top']=0.85
        mpl.rcParams['figure.subplot.right']=0.95
        mpl.rcParams['figure.subplot.bottom']=0.15
        mpl.rcParams['figure.subplot.left']=0.18
    if mode=='heatmap':
        mpl.rcParams['figure.figsize']=3.375, 3.375
        mpl.rcParams['figure.subplot.top']=0.95
        mpl.rcParams['figure.subplot.right']=0.95
        mpl.rcParams['figure.subplot.bottom']=0.05
        mpl.rcParams['figure.subplot.left']=0.05


def plot2d(data, zmin=0.01, zmax=10.0, title='', xlabel='', LogNorm = True, cb_ticks=[], cmap='Blues'):
    fig = plt.figure(figsize=(3.375, 3.75))
    grid = AxesGrid(fig, (0.01, 0.01, 0.99, 0.85),
                nrows_ncols = (1,1),
                axes_pad = 0.0,
                add_all=True,
                label_mode = "1",
                share_all = True,
                cbar_location="top",
                cbar_mode="each",
                cbar_size="5%",
                cbar_pad="0%")
    if LogNorm:
        norm = mpl.colors.LogNorm(vmin=zmin, vmax=zmax)
    else:
        norm = mpl.colors.Normalize(vmin=zmin, vmax=zmax)
    grid[0].axes.imshow(data, norm=norm, interpolation='nearest',cmap=cmap)
    cb = mpl.colorbar.ColorbarBase(grid.cbar_axes[0], cmap=cmap,
                                   norm=norm,
                                   orientation='horizontal', label=title)
    if len(cb_ticks)>0:
        cb.set_ticks(cb_ticks.astype('float'))
        temp = cb_ticks.astype('|S10')
        for i in range(len(cb_ticks)):
            temp[i] = r'$' + temp[i] + r'$'
        print temp
        cb.set_ticklabels(temp)
    cb.ax.xaxis.set_ticks_position('top')
    cb.ax.xaxis.set_label_position('top')
    grid[0].axes.set_xticks([])
    grid[0].axes.set_yticks([])
    grid[0].axes.set_xlabel(xlabel)
    grid[0].axes.set_ylabel('')
    plt.draw()

# Data manipulation:

def make_segments(x, y):
    '''
    Create list of line segments from x and y coordinates, in the correct format for LineCollection:
    an array of the form   numlines x (points per line) x 2 (x and y) array
    '''

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    return segments


# Interface to LineCollection:

def colorline(x, y, z=None, cmap=plt.get_cmap('copper'), norm=plt.Normalize(0.0, 1.0), linewidth=3, alpha=1.0):
    '''
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify a colormap, a norm function and a line width
    '''

    # Default colors equally spaced on [0,1]:
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))

    # Special case if a single number:
    if not hasattr(z, "__iter__"):  # to check for numerical input -- this is a hack
        z = np.array([z])

    z = np.asarray(z)

    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm, linewidth=linewidth, alpha=alpha)

    ax = plt.gca()
    ax.add_collection(lc)

    return lc


def clear_frame(ax=None):
    # Taken from a post by Tony S Yu
    if ax is None:
        ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    for spine in ax.spines.itervalues():
        spine.set_visible(False)

#######################
## COLORMAPS ##########
#######################

# import matplotlib.colors as mcolors
# cm_data = np.loadtxt('rstat/text/ametrine.txt')/256.
# my_cmap = mcolors.ListedColormap(cm_data, name='ametrine')
