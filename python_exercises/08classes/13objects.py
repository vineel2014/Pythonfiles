class Egg:
    def __init__(self, kind): #constructor
        self.kind = kind
        print ("init called")
        
    def whatKind(self):
        return self.kind

def main():
    ratul = Egg("omelette") #object is a instance of the class
    xyz = Egg("boiled") #object is a instance of the class
    print (ratul.whatKind())
    print (xyz.whatKind())
    


if __name__ == "__main__": main()
