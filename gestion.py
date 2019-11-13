#DOUKOYE ELISABETH 18A864FS
class gestionnaire(personneBanque):
    def __init__(self):
        self.run()
      
    def ajouterCompte(self):
        print('1 - compte courant')
        print('2 - compte epargne')
        self.compte = input('Quel type de compte voulez vous creer: ')
        if compte == 1:
            self.name = input('Entrez votre nom: ')
            self.password = input('Entrez votre password: ')
            return self.compte, self.name, self.password
        elif compte == 2:
            self.name = input('Entrez votre nom: ')
            self.password = input('Entrez votre password: ')
            return self.compte, self.name, self.password

    def supprimerCompte(self):
        pass

    def modifierCompte(self):
        pass

    def saveInfoEmprunt(self):
        pass

    def run(self):
        print('1- Creer un compte')
        print('2- Creer un supprimerCompte')
        print('3- Creer un modifierCompte')

        reponse = int(input('Que voulez faire: '))
        if reponse == 1:
            compte, user, password = self.ajouterCompte()
            return compte, user, password
