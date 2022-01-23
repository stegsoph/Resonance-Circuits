from distutils.spawn import find_executable
import matplotlib.pyplot as plt
import numpy as np

def init_plot_style():
    """Initialize the plot style for pyplot.
    """
    plt.rcParams.update({'figure.figsize': (4, 3)})
    plt.rcParams.update({'figure.dpi' : 150 })
    plt.rcParams.update({'lines.linewidth': 4})
    plt.rcParams.update({'lines.markersize': 10})
    plt.rcParams.update({'lines.markeredgewidth': 2})
    plt.rcParams.update({'axes.labelpad': 20})
    plt.rcParams.update({'xtick.major.width': 1.5})
    plt.rcParams.update({'xtick.major.size': 5})
    plt.rcParams.update({'xtick.minor.size': 10})
    plt.rcParams.update({'ytick.major.width': 1.5})
    plt.rcParams.update({'ytick.major.size': 10})
    plt.rcParams.update({'ytick.minor.size': 30})
    plt.rcParams.update({'text.usetex': False})

    # for font settings see also https://stackoverflow.com/questions/2537868/sans-serif-math-with-latex-in-matplotlib
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'font.family': 'sans-serif'})
    
    # this checks if the necessary executables for rendering latex are included in your path; see also
    # https://matplotlib.org/stable/tutorials/text/usetex.html
    if find_executable('latex') and find_executable('dvipng') and find_executable('ghostscript'):
        plt.rcParams.update({'text.usetex': True})
        plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath,amssymb,amsfonts,amsthm}' + \
                                              r'\usepackage{siunitx}' + \
                                              r'\sisetup{detect-all}' + \
                                              r'\usepackage{helvet}' + \
                                              r'\usepackage{sansmath}' + \
                                              r'\sansmath'
    
def plot_arr_style(f1,f2,f_r,vf):
        
        arr="<|-|>"
        if (f1==vf.min()):
            if (f2>=vf.max()):
                arr="-"
            else:
                arr="<|-"
        elif (f1>vf.min()) & (f2>=vf.max()):
                arr="-|>"
                
        dict_ = dict(lw=3, arrowstyle=arr,
                     mutation_scale=20, color='darkslategrey')
        return dict_
