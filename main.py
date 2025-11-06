"""Ce module impléménte une fonction qui
vérifie si un nombre est premier puis le test 
dans la méthode main en affichant touts les 
nombres preimers de 0 à 100
"""
from math import sqrt
#### Fonction secondaire
def isprime(p: int) -> bool:
    """retourne True si le nombre p passé en paramètre est premier
    false sinon
    """
    p = int(p)
    if p <= 1 :
        return False
    premier = True
    for div in range(2,int(sqrt(p)+1)) :
        if p%div == 0 :
            premier = False
            break
    return premier
#### Fonction principale
def main():
    """
    Test la méthode is prime en affichant touts les nombres
    premier de 0 à 100
    """
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

if __name__ == "__main__":
    main()
