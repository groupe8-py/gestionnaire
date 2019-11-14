#DOUKOYE ELISABETH 18A864FS
class Gestionnaire:
   def __init__(self):
      self.id = ""
      self.password1 = ""
      self.password2 = ""
   def ajout(self): 
      self.id = input("veuilleez entrer votre id\n") 
      self.password1 = input("veuillez entrer votre mot de passe\n") 
      self.password2 = input("veuillez confirmer votre mot de passe\n") 
      while self.password1 != self.password2: 
          print("les mots de passe sont different veuiller reessayer\n")
          self.password1 = input("veuillez entrer votre mot de passe\n")
          self.password2 = input("veuillez confirmer votre mot de passe\n")
      print("votre compte a ete creer avec succes\nid : {}\nmot de passe : {}\n".format(self.id, self.password1))
   def suprim(self):  #defini la fonction suprimer
       print("veuillez vous identifier pour supprimer votre compte\n")
       ide = input("entrer votre id\n")
       code = input("entre votre mot de passe\n")
       if ide != self.id and code != self.password1:
          print("compte n'existe pas \n")
       else: 
          print("vouliez vous vraiment supprimer votre compte ?\noui = 1 et non = 2\ncet operation est irreversible\n")
          ab = input()
          ab = int(ab)
          if ab == 1:
             self.id = ""
             self.password1 = ""
             print("votre compte a ete suprimee avec success\n")
          elif ab == 2:
             print("vous avez annuler la suppression de votre compte\n")
          else:
             print("choix non dispo vous etes un blageur...AUREVOIR")
   def modif(self):
       print("veillez vous identifier pour modifier votre compte\n")
       iden = input("entrer votre id\n")
       cod = input("entrer votre code\n")
       if (iden == self.id and cod == self.password1):
          print("Bienvenu dans le menu modifier modifier\n1- mon id\n2- mon mot de passe\n")
          n = input("\n")
          n = int(n)
          if n == 1:
             self.id = input("entrer votre nouveau id\n")
             qw = input("entrer votre mot de passe pour confirmer\n")
             if qw == password1:
                print("id modifier avec sucess votre nouveau id est\n", self.id)
             else:
                print("mot de passe incorrect")
          elif n == 2:
             self.password1 = input("entrer votre nouveau mot de passe\n")
             self.password2 = input("veuillez confirmer votre nouveau mot de passe\n")
             while self.password1 != self.password2:
                print("les nouveuax mots de passe sont different veuiller reessayer\n")
                self.password1 = input("entrer votre nouveau mot de passe\n")
                self.password2 = input("confirmer votre nouveau mot de passe\n")
             print("votre mot de passe a ete modifier avec succes\nvotre nouveau mot de passe est:\n", self.password1)
          else:
             print("option non disponible") 
       else:
          print("desole ce compte n'existe pas\n")   
ab = Gestion()
sorti = 0
while sorti == 0:
   print("quel operation vouliez vous effectuer ?\n1- ajouter un compte\n2- supprimer mon compte\n3- modifier mon compte\n")
   n = input()
   n = int(n)
   if n == 1:
      ab.ajout()
   elif n == 2:
      ab.suprim()
   elif n == 3:
      ab.modif()
   else:
      print("commande non valide")
   print("taper 0 pour continuer ou n'importe quel chiffre pour quitter\n")
   sorti = input()
   sorti = int(sorti)
