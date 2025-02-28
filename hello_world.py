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
print("bonjour Le mondE".islower())

print("bonjour Le mondE".isupper())

print("BONJOUR LE MONDE".isupper())