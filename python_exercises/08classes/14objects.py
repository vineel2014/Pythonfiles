class Egg:
    def __init__(self, kind = "fried"): #constructor
        self.kind = kind
        
    def whatKind(self):
        return self.kind

def main():
    ratul = Egg() #object is a instance of the class
    xyz = Egg("boiled")
    print (ratul.whatKind())
    print (xyz.whatKind())

if __name__ == "__main__": main()
