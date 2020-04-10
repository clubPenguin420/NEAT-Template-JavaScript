class connectionHistory:
    def __init__(self, fromN, toN, inno, innovationNos):
        self.fromNode = fromN
        self.toNode = toN
        self.innovationNumber = inno
        self.innovationNumbers = []  #the innovation Numbers from the connections of the genome which first had this mutation
    #this represents the genome and allows us to test if another genoeme is the same
    #this is before this connection was added

        self.innovationNumbers[0:len(innovationNos)] = innovationNos[0:len(innovationNos)]


        def matches(self, genome, fromN, toN):
            if(len(genome.genes))




