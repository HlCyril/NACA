import numpy as np
import matplotlib.pyplot as plt


def calcul_yt(xc, t):
    """
    Parameters
    ----------
    xc : ndarray
        distribution des points
    t : float
        pourcentage d'épaisseur.

    Returns
    -------
    yt : ndarray
        demi-épaisseur
    """
    return 5*t*(0.2969*np.sqrt(xc)-0.1260*xc-0.3516*np.power(xc, 2)+0.2843*np.power(xc, 3)-0.1036*np.power(xc, 4))


def plot_figure(up, down, naca, corde):
    """
    Parameters
    ----------
    up : ndarray
        points de l'extrados
    down : ndarray
        points de l'intrados
    naca : string
        numéros de l'aile
    corde : float
        valeur de la corde

    Returns
    -------
    NONE
    """
    fig, ax = plt.subplots()

    ax.plot(up[0], up[1], label='Extrados', color='orange', linestyle='solid')

    ax.plot(down[0], down[1], label='Intrados', color='blue', linestyle='solid')

    ax.legend(loc='upper right')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Aile NACA{naca}, pour une corde de {corde}m")
    ax.grid()

    plt.show()
