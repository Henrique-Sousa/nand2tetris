class Code:

    compTable = {
        '0'     :   '101010',
        '1'     :   '111111',
        '-1'    :   '111010',
        'D'     :   '001100',
        'A'     :   '110000',
        '!D'    :   '001101',
        '!A'    :   '110001',
        '-D'    :   '001111',
        '-A'    :   '110011',
        'D+1'   :   '011111',
        'A+1'   :   '110111',
        'D-1'   :   '001110',
        'A-1'   :   '110010',
        'D+A'   :   '000010',
        'D-A'   :   '010011',
        'A-D'   :   '000111',
        'D&A'   :   '000000',
        'D|A'   :   '010101'
    }

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

    @classmethod
    def comp(self, symbol):
        comp = '0'
        if 'M' in symbol:
            symbol = symbol.replace('M', 'A')
            comp = '1'
        comp += self.compTable[symbol]
        return comp

