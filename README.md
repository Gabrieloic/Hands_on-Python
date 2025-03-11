## Hands_on-Python


### ******    1: Intro et Exercices    ******

```bash

# Commandes de bases pour commencer 

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

### ******   Exercice 1    ******

```bash

#Ennoncé Exo 1

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

### ******  2: Les Variables et Types de donnees ******

```bash
# Une variable est un espace memoire dans lequel on stocke des donnees

#les differents types de variables que nous avons
  nom = 'gab'
  age = 27
  taille =1.80
  majeur = True
  nombre = [2,45,42,98]
  print(type(nom))
  print(type(age))
  print(type(taille))
  print(type(majeur))
  print(type(nombre))
#Voici le resultat que nous avons a la sortie
  <class 'str'> string = chaine de caractere
  <class 'int'> integer = entier
  <class 'float'> reel
  <class 'bool'> boolean = Vrai ou Faux
  <class 'list'> liste = peut contenir des entiers, chaines et reel
```

### ****** 3: Les Conditions  ******

```bash

## if , else if

# le code s'applique si la condition est remplie

# on peut directement convertir en entier la valeur recue au clavier
    age= int(input('saisis ton age: '))
    if age >=18:
        print('tu es majeur')
    else:
        print('tu es mineur')

# ou alors on peut la convertir dans la syntaxe de la condition

    age= input('saisis ton age: ')
    if int(age) >=18:
        print('tu es majeur')
    else:
        print('tu es mineur')

# on peut rajouter un else if ( elif) et pour faut bien surveiller les conditions
# car dans les syntaxes precedentes on a mis 'age >=18'

    age= int(input('saisis ton age: '))
    if age >18:
        print('tu es majeur')
    elif age ==18:
        print('tu viens de passer le cap, bienvenu chez les adultes')
    else:
        print('tu es mineur')

# les operateurs de comparaison
    ' == ' egal à
    ' != ' different de
    ' >= ' superieur ou egal
    ' <= ' inferieur ou egal
    ' > '  superieur strictement
    ' < '  inferieur strictement
```

### ****** 4: Les Boucles  ******

 ```bash
## For et While

# for permet de repeter une occurence un 'i' nombre de fois
    for i in range(6):
        print('hello ' +str(i))

#while
  compteur = 1 
  while compteur <=10:
      print(compteur)
      compteur +=1 
# la boucle incrementer compteur de 1 A chaque tour et tant que compteur
# n'aura pas atteint 10 il continuera et affichera le resultat
# Si on ne rajoute pas l'incrementation on cree ainsi une boucle infinie et il va afficher 1 sans s'arreter
```    

### ******  5: Les listes  ******

```bash
# Une liste permet de stocker plusieurs variables dans une seule

  #position     0        1      2
    fruits= ['pommes','banane','poires']
    print(fruits[1]) 
# sachant que les positions commencent par 0

# pour rajouter un element dans la liste
    fruits.append('goyave')
    print(fruits)
# le resultat devient
    ['pommes', 'banane', 'poires', 'goyave']

# pour supprimer un element de la liste
    fruits.remove('pommes')
    print(fruits)
# le resultat devient
    ['banane', 'poires', 'goyave']

# on peut aussi parcourir les elements d'une liste
    for test in fruits:
        print(test)
# et il nous liste le resultat en dehors de la liste
    pommes
    banane
    poires
    goyave
```

### ******  6: Les Fonctions personalisées  ******

```bash

# Une fonction personalisée permet d'eviter de repeter le code et mieux s'organiser

#on cree la fonction
    def direbonjour(nom):
        print('bonjour ' + nom)

    nom =input('entrer le nom 1 : ')
    nom_2 =input('entrer le nom 2 : ')

# on peut appeler la fonction a n'importe quel moment
    direbonjour(nom)
    direbonjour(nom_2)
# le resultat affiché
    bonjour (valeur_nom_1)
    bonjour (valeur_nom_2)

# on peut egalement creer une  fonction de calcul

    def somme(a, b):
        return a + b

# on demande de saisir des informations afin de les additioner
    salaire_1= int(input('quel est le salaire 1 ? '))
    salaire_2= int(input('quel est le salaire 2 ? '))
    
    resultat = somme(salaire_1, salaire_2)
    print(resultat)
```

### ******   Exercice 2    ******

```bash

# 1: on demande un nombre au user
# 2: on verifie si le nombre est paire ou impaire mod
# 3: on affiche tous les nombres de 1 jusqu'à ce nombre
# 4: on ajoute tout ces nombres dans une liste et on l'affiche
# 5: on cree une fonction qui affiche bonjour 'i' nombre de fois 


## Correction

# 1: on demande un nombre au user
    nombre =int(input('veuillez saisir un nombre : '))

# 2: on verifie si le nombre est paire ou impaire mod
# est-il paire ? soit le reste de lq division du nombre par 2

    if nombre%2==0: 
        print("c'est un nombre paire")
    else:
        print("c'est un nombre impaire ")

# 3: on affiche tous les nombres de 1 jusqu'à ce nombre
    
    for i in range(nombre):
        print(i+1)

# 4: on ajoute tout ces nombres dans une liste et on l'affiche

    list = []
    for i in range(nombre):
        list.append(i+1)
    print(list)

# 5: on cree une fonction qui affiche bonjour 'i' nombre de fois 
    def bonjour_i_fois(bjr):
        print('bonjour '+ str(i+1) + ' fois ')
    
    for i in range(nombre):
        bonjour_i_fois(i)
```

### ******   Manipuler les chaines de caracteres    ******

```bash


# met toute la chaine en majuscule
  print("bonJOur".upper())
# met toute la chaine en minuscule
  print("bonJOur".lower())
# met la premiere lettre du premier mot en majuscule
  print("bonJOur".capitalize())
# met toute les premires lettres de chaque mot en majuscule
  print("bonJOur".title())  
# remplace une chaine par ce que nous voulons
  print("bonjour tout le monde".replace("jour", "soir"))

# la methode split permet de supprimer un element d'une chaine et de creer une liste avec le reste 
  print("1, 2, 3, 4, 5, 6, 7".split(","))
# on obtient
  ['1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7']

# on peut mettre les parametres que nous souhaitons enlever
  print("1, 2, 3, 4, 5, 6, 7".split(", "))
# on obtient
  ['1', '2', '3', '4', '5', '6', '7']

# join quant a lui creer une chaine de caractere et peut rajouter des elements que nous souhaitons
# ici on met en parametre la sortie du split precedent 
#soit le resultat  ['1', '2', '3', '4', '5', '6', '7']
  print(".".join("1, 2, 3, 4, 5, 6, 7".split(", ")))
#on obtient
  1.2.3.4.5.6.7

 Join et Split sont des methodes qu'on utilise uniquement sur des chaines de caracteres



# on peut aussi verifier le type d'une chaine avec les differentes methodes

  print("bonjour Le mondE".islower())
# va retourner False parce que toute la chaine n'est pas lower

  print("bonjour Le mondE".isupper())
# va retourner False parce que toute la chaine n'est pas upper

  print("BONJOUR LE MONDE".isupper())
## va retourner True parce que toute la chaine verifier la condition

```

### ******   Les Dictionnaires    ******

```bash

# un dico permet d'associer des cles et des valeurs

# on cree un dico de cette facon

    personne = {
        "nom" : "Gabriel",
        "age" : 29,
        "ville": "Paris"
    }
# on affiche une cle 
    print(personne["nom"])

#on peut modifier une cle en lui donnant un autre valeur, ce qui va ecraser la premiere et l'age sera desormais " 33 "

    personne ["age"] = 33
    print(personne["age"])

# on peut aussi ajouter un nouvel element

    personne["email"] = "contact@dogfather.com"
    print(personne["email"])

# pour parcourir tout le contenu d'un dictionnaire on fait une boucle

    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")
# on a ca en resultat
    nom : Gabriel
    age : 33
    ville : Paris
    email : contact@dogfather.com

# le " f " permet d'interpreter tout ce qui est dans la methode print comme una variable ou une expression

```

### ******   Les Tupples    ******

```bash

# les tuples c'est une liste qui est imuable c.a.d qui ne peut pas etre modifie une fois creee
# ce qui peut etre interessant pour securiser des donnees et empecher des modifications excessives
# comme par exemple des cles API, on prefere les mettre dans un tuple plutot qu'une liste

    prenom = ("Samuel", "lucas", "Romain","Gabriel")
    print(prenom[2])
# en resultat on a
    Romain
# etant donne que les id des elements se comptent a partir de 0, on peut donc afficher le 3 eme element ainsi


```

### ******   Ecrire dans un fichier    ******

```bash


# pour le faire on utilise la methode "open"

    with open("mon_fichier_test.txt", "w") as fichier:
        fichier.write("Salut la famille, ceci est la premiere ligne de mon fichier rajoutee avec la methode open sur Python")

# le " w " qu'on met dans la syntaxe permet de dire qu'on va ecrire, mais s'il y a deja du contenu
#  dans le fichier il sera ecrase
# Aussi avec la methode open, si le fichier n'existe pas, il sera cree dans le meme dossier que notre script Python

```

### ******   Ajouter du contenu dans un fichier    ******

```bash

# Pour ajouter du contenu dans un fichier sans supprimer l'existant
# cette fois c'est avec la lettre " a "

    with open("mon_fichier_test.txt", "a") as fichier:
        fichier.write("\nCeci est la nouvelle ligne que je rajoute dans mon fichier")

# en prenant soin de mettre le " \n " pour passer a la ligne


```

### ******   lire un fichier    ******

```bash

    with open("mon_fichier_test.txt", "r") as fichier:
        contenu = fichier.read()
        print(contenu)

# le " r " ici est mis pour read et donc avec cette methode on affiche tout le contenu d'un fichier
# dans le terminal un peu comme avec une commande " cat " sur linux

```

### ******   Gestion des erreurs    ******

```bash

# prenons un cas ou on demande a un user de donner un nombre au clavier mais au lieu d'un nombre il met
# une lettre, automatiquement python va me retourner une erreur
# Il faut donc un moyen de dire au user qu'il a fait une erreur en ne mettant pas le bon type demande

    nombre = int(input("donner moi un nombre : "))
    print("le triple de votre nombre est :", nombre*3)

# jusqu'ici on est bon si le user met un chiffre, le resultat lui donnera le triple de son chiffre
# mais si le user met une lettre a la place on aura cette erreur
    Python/hello_world.py
    donner moi un nombre : ret
    Traceback (most recent call last):
      File "/Users/the-dogfather/Documents/Devops/Hands_on-Python/hello_world.py", line 289, in <module>
        nombre = int(input("donner moi un nombre : "))
    ValueError: invalid literal for int() with base 10: 'ret'
# l'erreur dit que le valeur entree n'est pas du meme type que celle attendue
# dans ce cas pour la resourdre on utilise la methode " try except "

    try:
        nombre = int(input("donner moi un nombre : "))
        print("le triple de votre nombre est :", nombre*3)
    except ValueError:
        print("Attention vous n'avez pas taper un nombre valide !!!!! ")

# Cette commande va afficher une erreur a l'ecran invitant le user a recommencer

```

### ******   Importer des bibliotheques ou modules   ******

```bash


    import math
    print(math.sqrt(25))
# on importe la biblio math pour faire le calcul de la racine caree

# on peut importe une simple fonction d'une bibliothe plutot que la bibliotheque entiere

    from random import randint
    print(randint(1,45))
# cette fonction me permet de generer un nombre aleatoire entre la selection que je specifie

# on peut aussi importer des modules supplementaires qui ne sont pas presentes nativement par defaut sur python 


# on peut intaller une nouvelle bibliotheque depuis notre cli en dehors de l'interpreteur python
# requests est une lib qui permet d'envoyer des requettes vers un site web histoire de tester la connexion en fonction de la reponse
# error 200 : Ca veut dire que le site est atteignable
# error 404 : des chances que le site n'existe plus ...etc 

# l'installation de cette lib se fait avec la commande suivante
    python3 -m pip install requests

# on va tester si on a access a google
    import requests
    reponse = requests.get("https://www.google.com")
    print(reponse.status_code)
# le resultat est
    200 # c.a.d que le site est accessible depuis notre code

```

### ******   Exercice 3  ******

```bash

# 1: on cree un dico avec ( nom, age, ville)
# 2: on ecris le dico dans un fichier txt
# 3: utiliser try except pour eviter des erreurs 
# 4: on lit et affiche le contenu de notre fichier
# 5: on demande d'utiliser un module pour donner un chiffre aleatoire

# Solution 

# 1: on cree un dico avec ( nom, age, ville)

# on cree le dico
    personne = {
        "nom": "Lydie",
        "prenom": "sam",
        "age": 25,
        "email": "sam_lydie@mugiwara.op",
        "ville": "Nice"
    }
# on affiche en balayant tous les elements 
    for cle, valeur in personne.items():
        dico = print(f"{cle} : {valeur}")

# 2: on ecris le dico dans un fichier txt
# 3: on utilise try except pour eviter des erreurs

    try:
        with open("mon_fichier_2.txt", "w") as fichier:
            for cle, valeur in personne.items():
                fichier.write(f"{cle} : {valeur} \n")
        print("\nc'est dans la boite !!! \n ")
    except Exception as e:
        print("aie aie aie probleme !!! ")

# 4: on lit et affiche le contenu de notre fichier

    try:
        with open("mon_fichier_3.txt", "r") as fichier:
            print(fichier.read())
    except FileNotFoundError:
        print("aie aie aie le fichier n'existe pas !!\n ")

# 5: on demande d'utiliser un module pour donner un chiffre aleatoire

    from random import randint
    print("nombre aleatoire entre 1 et 90 : ", randint(1,90))
    

# Si on veut trier une liste on peut le faire de cette facon

    # on a la chaine suivante
        chaine = "Pierre, Julien, Anne, Marie, Lucien"
    # on commence par isoler chaque element en supprimant le separateur:
        chaine_liste = chaine.split(", ")
    # puis on trie la liste qu'on desormais
        chaine_liste.sort()
        print(chaine_liste)
    # Une fois trie, on les rassemble avec la methode join  
        chaine_en_ordre = ", ".join(chaine_liste)
        print(chaine_en_ordre)
        print(2*152)
in
```
