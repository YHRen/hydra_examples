class MLP:
    def __init__(self, **params):
        print("\nInitializing "+self.__class__.__qualname__+": ")
        for k, v in params.items():
            print(str(k)+" : "+str(v)+"\t"+str(type(v)))
        print("="*80)
    # also supports positional and default args
    # def __init__(self, input_dim, hidden_dims, output_dim=3):
    #     self.idim = input_dim
    #     self.hdim = hidden_dims
    #     self.odim = output_dim
