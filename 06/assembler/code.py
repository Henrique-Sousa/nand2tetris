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

    @classmethod
    def jump(self, symbol):
        jump = 0
        if 'G' in symbol:
            jump += 1
        if 'E' in symbol and 'N' not in symbol:
            jump += 2
        if 'L' in symbol:
            jump += 4
        if 'N' in symbol:
            jump = 5
        if symbol == 'JMP':
            jump = 7
        return self.toBinary(jump, 3)
