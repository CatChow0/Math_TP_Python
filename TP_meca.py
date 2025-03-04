import matplotlib.pyplot as plt
import numpy as np

### CONSTANTES
m = 0.8         # masse de l'oiseau (Kg)
g = 9.81        # constante gravitationnelle (m/s²)
k = 10          # constante de raideur du ressort (N/m)
f2 = 0.2 / m    # coeff de frottement divisé par la masse

### FONCTIONS

# Etape 1.1
def vitesse_initialle(a, l1):    # a = alpha || l1 longueur en cm
    v_eject = l1 * np.sqrt(k/m) * np.sqrt( 1 - ( m * g * np.sin(a)/(k * l1) ) ** 2)
    return v_eject

# Etape 2.1
def lancer_oiseau(a, l1):    # a = alpha || l1 longueur en cm
    v0 = vitesse_initialle(a, l1)
    timpact = (2 * v0 * np.sin(a)) / g  # Temps d'impact
    liste_t = np.linspace(0, timpact, 100)  # Liste de temps

    # Calcul des coordonnées x(t) et y(t)
    x = v0 * np.cos(a) * liste_t
    y = v0 * np.sin(a) * liste_t - 0.5 * g * liste_t**2

    return x, y

# Etape 2.2
def afficher_oiseau(a, l1):    # a = alpha || l1 = longeur en cm
    x, y = lancer_oiseau(a, l1)

    plt.plot(x, y)
    plt.title('Trajectoire de l\'oiseau')
    plt.xlabel('Position x (m)')
    plt.ylabel('Position y (m)')
    plt.grid()
    plt.tight_layout()
    plt.legend()
    plt.show()

# Etape 3.1
def afficher_balles_multiples(l1, nombres_balles):
    alphas = np.linspace(0, np.pi/2, nombres_balles)  # 11 valeurs d'alpha entre 0 et π/2

    plt.figure()
    for alpha in alphas:
        x, y = lancer_oiseau(alpha, l1)
        plt.plot(x, y, label=f'alpha = {alpha:.2f} rad')

    plt.title('Trajectoires de l\'oiseau pour différentes valeurs d\'alpha')
    plt.xlabel('Position x (m)')
    plt.ylabel('Position y (m)')
    plt.grid()
    plt.tight_layout()
    plt.legend()
    plt.show()

### INTERFACE

# Etape 1.2

#alpha_joueur_degres = float(input("Choisissez la valeur de l'angle alpha (en degrés) : "))
l1_joueur = float(input("Choisissez la longueur d'étirement du ressort (en cm) : "))
nombre_balles = int(input("Choisissez le nombre de balles à afficher : "))
print(f"Vous avez choisi l1 = {l1_joueur} cm")

#print(f"Vous avez choisi alpha = {alpha_joueur_degres}° et l1 = {l1_joueur} cm")
#alpha_joueur = 2*np.pi*alpha_joueur_degres/360
#print(f"La vitesse initiale de l'oiseau est donc de = {vitesse_initialle(alpha_joueur, l1_joueur)} cm/s")

### Affichage des résultats

#afficher_oiseau(alpha_joueur, l1_joueur)
afficher_balles_multiples(l1_joueur, nombre_balles)