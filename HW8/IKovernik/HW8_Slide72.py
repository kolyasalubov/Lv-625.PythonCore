class Human:

    species="Homosapiens"

    @staticmethod
    def staticmetod():
        print("arbitrary message")


    def __init__(self,name):
        self.name=name

    def welcomemsg(self):
        print("Hello, "+self.name)

    def spicesinfo(self):
        print(self.name+" species is "+self.species)



igor=Human("Igor")
igor.welcomemsg()
igor.spicesinfo()
igor.staticmetod()


