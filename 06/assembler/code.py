class Code:
    @classmethod
    def toBinary(self, n):    # get an integer and convert it to binary
        binint = bin(int(n))[2:]
        return binint.zfill(16) 
    

