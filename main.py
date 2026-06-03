import os
chemin = "/Users/the-dogfather/PycharmProjects/Hands_on-Python"
nouveau = os.path.join(chemin, "dossier", "sous-dossier")
os.removedirs(nouveau)
print(nouveau)