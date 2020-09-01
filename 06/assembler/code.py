class Code:

    @classmethod
    def toBinary(self, n, digits):    # get an integer and convert it to binary
        binint = bin(int(n))[2:]
        return binint.zfill(digits) 

    @classmethod
    def dest(self, symbol):
        dest = 0
        if 'M' in symbol:
            dest += 1
        if 'D' in symbol:
            dest += 2
        if 'A' in symbol:
            dest += 4
        return self.toBinary(dest, 3) 

