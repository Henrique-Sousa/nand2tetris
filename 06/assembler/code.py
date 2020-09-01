class Code:

    @classmethod
    def toBinary(self, n, digits):    # get an integer and convert it to binary
        binint = bin(int(n))[2:]
        return binint.zfill(digits) 

