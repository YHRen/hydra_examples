class MLP:
    def __init__(self, input_dim, hidden_dims, output_dim=3):
        """
            example of showing initialization with positional arguments
        """
        print("\nInitializing "+self.__class__.__qualname__+": ")
        self.in_dim = input_dim
        self.hd_dim = hidden_dims
        self.ot_dim = output_dim
        for k, v in self.__dict__.items():
            print(k, ":", v)
        print("="*80)
