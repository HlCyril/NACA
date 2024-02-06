# 1. Description
Ce code a pour objectif de tracer le profil d'une aile NACA symétrique du stype 00XX.
# 2. Entrée
L'utilisateur doit fournir dans la console la série de 4 chiffre de l'aile, la corde souhaité, le nombre de points pour le tracer, ainsi que le choix du type de distribution pour la répartition des points.
# 3. Structure
Le programme est composé d'un fichier principal à exécuter et d'un module contenant les fonctions. Il faut au préalable installer numpy ainsi que matplotlib sur sa machine.

Le fichier principal cherchera l'épaisseur maximale ainsi que ses coordonnées.
# 4. Fonctions
Il y a 2 fonctions : 
- calcul_yt qui prend en argument xc et t qui sont respectivement la répartition des points et le pourcentage d'épaisseur. Cette fonction calcul les points yt associées à xc ;
- plot_figure qui prend en argument les points de l'extrados, up ; les points de l'intrados, down ; les 4 chiffres de l'aile, naca et la corde, corde. Cette fonction affiche la figure de l'aile.