class CNN:
    def __init__(self, **params):
        print("\nInitializing "+self.__class__.__qualname__+": ")
        for k, v in params.items():
            print(str(k)+" : "+str(v)+"\t"+str(type(v)))
        print("="*80)
