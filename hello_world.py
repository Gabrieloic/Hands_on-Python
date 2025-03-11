# Intro a Python et exercices

# **************     Commandes de bases pour commencer       ***************************

#mot = "Cameroun"
#print (len(mot))
#nom =input('donnez votre nom : ')
#prenom =input('donnez votre prenom : ')
# print ('vous etes ' + nom + ' ' + prenom + '!')

#print (type('YES'))

#Age = 45
#print(int(Age))

#for i in range(5):
#    print(i)

#nombre =[4,6,90,12,1.5]
#print (sum(nombre))
#print (max(nombre))
#print (min(nombre))
#print (sorted(nombre))


# exo 1

# 1: demander au user son nom
# 2: on lui souhaite la bienvenu avec son nom
# 3: on lui demande son age 
# 4: on convertir son age
# 5: on affiche son age dans 100 ans
# 6: on cree une liste de nombre et on affiche le plus grand et la somme totale

#Solution

# 1: nom du user
#nom =input ('veuillez saisir votre nom svp : ')
#prenom =input ('veuillez saisir votre prenom svp : ')

# 2: on affiche son nom
#print ('Bienvenue Mr ' + nom +' ' + prenom +' veuillez vous installer')

# 3: on demande son age
#age =int(input('quelle est votre age ? '))
#age_futur= age+100

# 4: son age dans 100 ans
#print('dans 100 ans Mr ' + nom + ' aura ' +str(age_futur)+ ' ans et ne sera plus tres jeune' )

# 5: creer une liste de nombre
#phrase = input('veuillez ecrire un truc pour compter le nombre de caracteres : ')
#print('il y a dans cette phrase ' + str(len(phrase)) + ' caracteres en tout . ')

# 6: afficher le plus grand nombre
#num = [3,90,345,2,0.4,23,45677]
#print('le plus petit nombre est : ' +str(min(num))) #affiche
#print('le plus grand nombre est : ' +str(max(num)))
#print('la somme des nombres est : ' +str(sum(num)))
#print('classement par ordre croissant: ' +str(sorted(num)))
#print(type(num))

# ******************** Les Variables et Types de donnees *******************

# Une variable est un espace memoire dans lequel on stocke des donnees

#les differents types de variables que nous avons
#nom = 'gab'
#age = 27
#taille =1.80
#majeur = True
#nombre = [2,45,42,98]
#print(type(nom))
#print(type(age))
#print(type(taille))
#print(type(majeur))
#print(type(nombre))

# conditions

#age= int(input('saisis ton age: '))
#if age >18:
#    print('tu es majeur')
#elif age ==18:
#    print('tu viens de passer le cap, bienvenu chez les adultes')
#else:
#   print('tu es mineur')

# les boucles 

# for
# for i in range(6):
#     print('hello ' +str(i))

# while
# compteur = 1 

# while compteur <=10:
#     print(compteur)
#     compteur +=1 
# la boucle incrementer compteur de 1 A chaque tour et tant que compteur n'aura pas atteint 10 il continuera
# et affichera le resultat
# si on ne rajoute pas l'incrementation on cree ainsi une boucle infinie et il va afficher 1 sans s'arreter
    

#les listes

# fruits= ['pommes','banane','poires']
# position     0         1        2
# sachant que les positions commencent par 0
# print(fruits[1]) 

# pour rajouter un element dans la liste
# fruits.append('goyave')
# print(fruits)

# pour supprimer un element de la liste
# fruits.remove('pommes')
# print(fruits)

# on peut aussi parcourir les elements d'une liste
# for test in fruits:
#     print(test)
# et il nous liste le resultat en dehors de la liste

# les fonctions personalisees

# on cree la fonction
# def direbonjour(nom):
#     print('bonjour ' + nom)


# nom =input('entrer le nom 1 : ')
# nom_2 =input('entrer le nom 2 : ')

# on peut appeler la fonction a n'importe quel moment
# direbonjour(nom)
# direbonjour(nom_2)

# on cree une autre fonction de calcul
# def somme(a, b):
#     return a + b

# salaire_1= int(input('quel est le salaire 1 ? '))
# salaire_2= int(input('quel est le salaire 2 ? '))

# resultat = somme(salaire_1, salaire_2)
# print(resultat)


# exercice

# 1: on demande un nombre au user
# 2: on verifie si le nombre est paire ou impaire mod
# 3: on affiche tous les nombres de 1 jusqu'à ce nombre
# 4: on ajoute tout ces nombres dans une liste et on l'affiche
# 5: on cree une fonction qui affiche bonjour 'i' nombre de fois 

#1
# nombre =int(input('veuillez saisir un nombre : '))

# 2
# est-il paire ? soit le reste de lq division du nombre par 2

# if nombre%2==0: 
#     print("c'est un nombre paire")
# else:
#     print("c'est un nombre impaire ")

# 3 : on affiche tous les nombres de 1 jusqu'à ce nombre

# for i in range(nombre):
#     print(i+1)

# 4 : on ajoute tous ces nombres dans une liste et on l'affiche
# list = []
# for i in range(nombre):
#     list.append(i+1)
# print(list)

# 5: on cree une fonction qui affiche bonjour 'i' nombre de fois 
# def bonjour_i_fois(bjr):
#     print('bonjour '+ str(i+1) + ' fois ')

# for i in range(nombre):
#     bonjour_i_fois(i)


# Manipuler les chaines de caracteres

# met toute la chaine en majuscule
# print("bonJOur".upper())
# met toute la chaine en minuscule
# print("bonJOur".lower())
# met la premiere lettre du premier mot en majuscule
# print("bonJOur".capitalize())
# met toute les premires lettres de chaque mot en majuscule
# print("bonJOur".title())
# remplace une chaine par ce que nous voulons
# print("bonjour tout le monde".replace("jour", "soir"))

# 
# on peut aussi verifier le type d'une chaine avec les differentes methodes
# print("bonjour Le mondE".islower())
# va retourner false parce que toute la chaine n'est pas lower
# print("bonjour Le mondE".isupper())
# va retourner False parce que toute la chaine n'est pas upper
# print("BONJOUR LE MONDE".isupper())
# # va retourner True parce que toute la chaine verifier la condition

# Les Dictionnaires
# un dico permet d'associer des cles et des valeurs

# on cree un dico de cette facon
# personne = {
#     "nom" : "Gabriel",
#     "age" : 29,
#     "ville": "Paris"
# }
# print(personne["nom"])

# on peut modifier une cle en lui donnant un autre valeur
# ce qui va ecraser la premiere
# personne ["age"] = 33
# print(personne["age"])

# on peut aussi ajouter un nouvel element
# personne["email"] = "contact@dogfather.com"
# print(personne["email"])

# pour parcourir tout le contenu d'un dictionnaire on fait une boucle

# for cle, valeur in personne.items():
#     print(f"{cle} : {valeur}")

# le " f " permet d'interpreter tout ce qui est dans la methode print comme una variable ou une expression

# on a ca en resultat
# nom : Gabriel
# age : 33
# ville : Paris
# email : contact@dogfather.com

# les tuples

# les tuples c'est une liste qui est imuable c.a.d qui ne peut pas etre modifie une fois creee
# ce qui peut etre interessant pour securiser des donnees et empecher des modifications excessives
# comme par exemple des cles API, on prefere les mettre dans un tuple plutot qu'une liste

# prenom = ("Samuel", "lucas", "Romain","Gabriel")
# print(prenom[2])
# etant donne que les id des elements se comptent a partir de 0, on peut donc afficher le 3 eme element ainsi


# ecrire dans des fichiers

# pour le faire on utilise la methode "open"

# with open("mon_fichier_test.txt", "w") as fichier:
#     fichier.write("Salut la famille, ceci est la premiere ligne de mon fichier rajoutee avec la methode open sur Python")

# le " w " qu'on met dans la syntaxe permet de dire qu'on va ecrire, mais s'il y a deja du contenu
#  dans le fichier il sera ecrase
# Aussi avec la methode open, si le fichier n'existe pas, il sera cree dans le meme dossier que 
# notre script Python


# Pour ajouter du contenu dans un fichier sans supprimer l'existant
# cette fois c'est avec la lettre " a "
# with open("mon_fichier_test.txt", "a") as fichier:
#     fichier.write("\nCeci est la nouvelle ligne que je rajoute dans mon fichier")


# Lire un fichier 

# with open("mon_fichier_test.txt", "r") as fichier:
#     contenu = fichier.read()
#     print(contenu)
# le " r " ici est mis pour read et donc avec cette methode on affiche tout le contenu d'un fichier
# dans le terminal un peut comme une commande cat sur linux


# Gerer les erreurs

# prenons un cas on demande a un user de donner un nombre au clavier mais au lieu d'un nombre il met
# une lettre, automatiquement python va me retourner une erreur
# Il faut donc un moyen de dire au user qu'il a fait une erreur en ne mettant pas le bon type demande

# nombre = int(input("donner moi un nombre : "))
# print("le triple de votre nombre est :", nombre*3)

# jusqu'ici on est bon si le user met un chiffre, 
# mais si le user met une lettre a la place on aura cette erreur
# Python/hello_world.py
# donner moi un nombre : ret
# Traceback (most recent call last):
#   File "/Users/the-dogfather/Documents/Devops/Hands_on-Python/hello_world.py", line 289, in <module>
#     nombre = int(input("donner moi un nombre : "))
# ValueError: invalid literal for int() with base 10: 'ret'
# l'erreur dit que le valeur entree n'est pas du meme type que celle attendue
# dans ce cas pour la resourdre on utilise la methode " try except "

# try:
#     nombre = int(input("donner moi un nombre : "))
#     print("le triple de votre nombre est :", nombre*3)
# except ValueError:
#     print("Attention vous n'avez pas taper un nombre valide !!!!! ")


# Importer des modules et bibliotheques

# import math
# print(math.sqrt(25))
# on importe la biblio math pour faire le calcul de la racine caree

# on peut importe une simple fonction d'une bibliothe plutot que la bibliotheque entiere

# from random import randint
# print(randint(1,45)) 
# cette fonction me permet de generer un nombre aleatoire entre la selection que je specifie

# on peut aussi importer des modules supplementaires qui ne sont pas presentes nativement par defaut sur python 

# on peut intaller une nouvelle bibliotheque depuis notre cli en dehors de l'interpreteur python
# requests est une lib qui permet d'envoyer des requettes vers un site web histoire de tester la connexion
#  en fonction de la reponse
# error 200 : Ca veut dire que le site est atteignable
# error 404 : des chances que le site n'existe plus ...etc 

# import requests
# reponse = requests.get("https://www.google.com")
# print(reponse.status_code)


# Exercice

# 1: on cree un dico avec ( nom, age, ville)
# 2: on ecris le dico dans un fichier txt
# 3: utiliser try except pour eviter des erreurs 
# 4: on lit et affiche le contenu de notre fichier
# 5: on demande d'utiliser un module pour donner un chiffre aleatoire

# Solution 

# 1: on cree un dico avec ( nom, age, ville)

# on cree le dico
# personne = {
#     "nom": "Lydie",
#     "prenom": "sam",
#     "age": 25,
#     "email": "sam_lydie@mugiwara.op",
#     "ville": "Nice"
# }
# on affiche en balayant tous les elements 
# for cle, valeur in personne.items():
#     dico = print(f"{cle} : {valeur}")

# 2: on ecris le dico dans un fichier txt
# 3: utiliser try except pour eviter des erreurs, dans le cas ou le fichier est inexistant

# try:
#     with open("mon_fichier_2.txt", "w") as fichier:
#         for cle, valeur in personne.items():
#             fichier.write(f"{cle} : {valeur} \n")
#     print("\nc'est dans la boite !!! \n ")
# except Exception as e:
#     print("aie aie aie probleme !!! ")

# 4: on lit et affiche le contenu de notre fichier

# try:
#     with open("mon_fichier_3.txt", "r") as fichier:
#         print(fichier.read())
# except FileNotFoundError:
#     print("aie aie aie le fichier n'existe pas !!\n ")

# 5: on demande d'utiliser un module pour donner un chiffre aleatoire

# from random import randint
# print("nombre aleatoire entre 1 et 90 : ", randint(1,90))


# a = "pyth"
# print(a[-4])
# print("mon_fichier.txt".endswith(".txt"))

chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_liste = chaine.split(", ")
chaine_liste.sort()
print(chaine_liste)
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)