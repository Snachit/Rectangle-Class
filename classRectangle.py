class Rectangle :
    
    #def __init__(self) :
        #self.longueur = 0 
        #self.largeur = 0 
    
    def __init__(self, longeur, largeur) :
        self.longeur = longeur
        self.largeur = largeur 
        
   # def __init__(self, oldObject):
    #    self.longeur = oldObject.longeur
     #   self.largeur = oldObject.largeur
        
    def perimetre(self):
        return 2 * (self.longeur + self.largeur)
    
    def Air(self):
        return self.longeur * self.largeur

    def IsCarre(self):
        if self.longeur == self.largeur :
            return "Il s agit d un carre"
        else :
            return "il s agit pas d un carre"

    def Affichage(self):
        print("longeur:",self.longeur)
        print("largeur",self.largeur)
        print("Perimetre:",self.perimetre())
        print("Aire:",self.Air())
        print(self.IsCarre())
        
    