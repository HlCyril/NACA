import numpy as np
import mod

print("Ce programme va tracer le profil symétrique d'une aile NACA")

naca = str(input("Veuillez donner les 4 chiffres de l'aile NACA sans espace (ex : 0022) : "))

corde = float(input("Donner la valeur de la corde c en mètre : "))

nombre_points = int(input("Donner une valeur entière du nombre de point souhaitée : "))

# Pourcentage d'épaisseur
t = int(naca[-2:])/100.

reponse = input("Mettez 1 si vous voulez utiliser la transformée de Glauert, sinon mettez 0 : ")
if reponse:
    theta = np.linspace(0., np.pi, nombre_points)
    xc = (1.-np.cos(theta))/2.
else:
    xc = np.linspace(0., 1., nombre_points)

yt = mod.calcul_yt(xc, t)

up = np.array([xc*corde, yt*corde])

down = np.array([xc*corde, -1*yt*corde])

# On va chercher l'épaisseur maximale
# Le profil est symétrique donc il faut juste chercher dans une des deux listes
epaisseur_max = np.max(yt)
indice_epaisseur_max = np.argmax(yt)
print("\nL'épaisseur maximale avec la discrétisation utilisée est de : ", 2*epaisseur_max)
print(f"La position de cette épaisseur est ({xc[indice_epaisseur_max]},{yt[indice_epaisseur_max]}).")
# Affichage de l'aile
mod.plot_figure(up, down, naca, corde)
