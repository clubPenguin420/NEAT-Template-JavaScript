import random as r


#a connection between 2 nodes
class connectionGene: 
    def __init__(self, fromN, toN, w, inno):
        self.fromNode = fromN
        self.toNode = toN
        self.weight = w
        self.enabled = True
        self.innovationNo = inno #each connection is given a innovation number to compare genomes

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#changes the this.weight

    def mutateWeight(self):
        rand2 = r.random() 
        if(rand2 < 0.1): #10% of the time completely change the this.weight
            self.weight = r.uniform(-1, 1)   
        else:   #otherwise change it slightly
            self.weight += (r.gauss(0, 1) / 50)

            if (self.weight > 1):
                this.weight = 1
      
            if (self.weight < -1):
                this.weight = -1

  #----------------------------------------------------------------------------------------------------------
  #returns a copy of this connectionGene  

    def clone(self, fromN, toN):
        clone = connectionGene(fromN, toN, self.weight, self.innovationNo)
        clone.enabled = self.enabled


        return clone 



