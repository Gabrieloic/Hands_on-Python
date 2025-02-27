# Hands_on-Python


******     Intro a Python et exercices    ******

```bash

## Commandes de bases pour commencer 

#instantie une variable et on l'affiche
  mot = "Cameroun" 
  print (len(mot))
  Age = 45
  print(int(Age))

#lit la valeur d'une variable saisie au clavier et l'affiche
  nom =input('donnez votre nom : ')
  prenom =input('donnez votre prenom : ')
  print ('vous etes ' + nom + ' ' + prenom + ' !')

#affiche le type d'un element
  print (type('YES'))

#cree une boucle simple
  for i in range(5):
      print(i)

# differentes operations sur une liste
  nombre =[4,6,90,12,1.5]
  print (sum(nombre))
  print (max(nombre))
  print (min(nombre))
  print (sorted(nombre))
```

## Exercices partie 1

```bash

##Ennoncé Exo 1

1: demander au user son nom
2: on lui souhaite la bienvenu avec son nom
3: on lui demande son age 
4: on convertir son age
5: on affiche son age dans 100 ans
6: on cree une liste de nombre et on affiche le plus grand et la somme totale

## Solution Exo 1

# 1: nom et prenom du user
  nom =input ('veuillez saisir votre nom svp : ')
  prenom =input ('veuillez saisir votre prenom svp : ')

# 2: on affiche son nom
  print ('Bienvenue Mr ' + nom +' ' + prenom +' veuillez vous installer')

# 3: on demande son age et on fais un calcul pour le futur
  age =int(input('quelle est votre age ? '))
  age_futur= age+100

# 4: son age dans 100 ans
  print('dans 100 ans Mr ' + nom + ' aura ' +str(age_futur)+ ' ans et ne sera plus tres jeune' )

# 5: on cree une liste de nombre
  phrase = input('veuillez ecrire un truc pour compter le nombre de caracteres : ')
  print('il y a dans cette phrase ' + str(len(phrase)) + ' caracteres en tout . ')

# 6: afficher le plus grand nombre
  num = [3,90,345,2,0.4,23,45677]
  print('le plus petit nombre est : ' +str(min(num)))
  print('le plus grand nombre est : ' +str(max(num)))
  print('la somme des nombres est : ' +str(sum(num)))
  print('classement par ordre croissant: ' +str(sorted(num)))
  print(type(num))
```

# ****** Les Variables et Types de donnees ******

```bash
# Une variable est un espace memoire dans lequel on stocke des donnees

