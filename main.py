# Calcule le revenu generés apres x années d'investissement en bourse
# en sachant que tu gagnes environ 7 % par mois et que tu investi une somme fixe chaque mois

#  ....... solution 12 ...........

a = int(input("Sur combien d'années souhaitez vous investir ? : "))

print(a)
m = 200 # la cotisation initiale mensuelle
b = 0   # cumul des revenus gagnés
i = 0
c = 0   # total investi
ci = 500 # somme reinvestie chaque mois
while i < a*12 :
    b = m + m*0.07
    m += m*0.07 + ci
    c = c + ci
    i += 1
    print("Bravo !!! Au {} eme mois, vous avez généré {} euros en "
          "demarrant uniquement avec 200 € et en rajoutant {} € chaque mois ...".format(i, round(b, 3), ci))
print(f"Bravo !!! Sur ces {a} derniers années, vous avez investi au total {c} euros et gagné {b:.2f} euros")
print("Bravo !!! En {} années, soit {} mois, vous avez généré {} euros...".format(a, a*12, round(b, 2)))
# {b:.2f} et round(b, 2) permettent d'afficher 2 chiffres apres la virgules du nombre {b}