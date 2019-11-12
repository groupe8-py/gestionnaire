#DOUKOYE ELISABETH 18A864FS
class gestionnaire(personneBanque):
 def__init__(self):
     self.utilisateure=""
     self.cod1=""
     self.cod2=""
 def ajouter(self):
     self.utilisateure=input("INSEREZ VOTRE nom\n")
     self.cod1=input("INSEREZ VOTRE code\n")
     self.cod2=input("CONFIRMEZ VOTRE code\n)
     while self.cod1!=self.cod2:
       print("mots de passe est incorrect,veuilez reesayer\n")
       self.cod1=input("Entrez votre code\n")
       self.cod1=("confirmez votre code\n")
       print("votre mot de passe est créé avec succès\n")
 def modification(self):  
     print("veillez vous identifier pour la modifier votre \n")
      idem=input("veuillez entrer votre id\n")
      code=input("veuillez entrer votre code\n")
      if(idem==self.user ab=nd code==self.cod1):
      print("que vouliez vous modifier\n1- mon id\n2- mon id")
      n=input("\n")
      n=int(n)
      if n==1:
      self.user=input("veuillez entrer votre nouveau id\n")
      print("id modifier avec succès votre nouveau id est\n")
      elif n==2:
      self.cod1=input("veuillez entrer votre nouveau mot de passe\n")
      self.cod2=input("veuillez confirmer votre nouveau mot de passe\n")
         while self.cod1 != self.cod2:
           print("les nouveaux mots de passes sont different\n")
            self.cod1=input("entrer votre nouveau\n")
            self.cod2=input("confirmer votre mot de passe\n")
            print("votre mot de passe est modifié avec succès\n")
            else:
               print("option non disponible")
            else:
               print("desolé ce compte n'existe pas")
  def suprimer(self):#definition de la fonction supprimer
      print("veuillez vous identifiez pour supprimer\n")
       ide=input("entrer votre id\n")
       code=input("entrez votre mot de passe\n")
       if ide!=self.id:
           print("compte n'existe pas\n")
        elif code!=self.cod1:
           print("compte n'existe pas\n")
        else:
           self.utilisateure=""
           self.password=""
           print("votre compte a été supprimé\n")
ab=gestion()
ab.ajouter()
ab.modifier()
ab.supprimer()
