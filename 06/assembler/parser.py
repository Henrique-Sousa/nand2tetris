class Parser:
        
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.current_command = '\n' 
        self.advance()

    def advance(self):
        while True:
            newline = self.file.readline()
            # checks if end of file
            if newline == '':
                self.current_command = ''
                return newline 
            # skip white space and comments
            newline = newline.strip()
            if newline == '' or newline.startswith('//'):
                continue
            else:
                self.current_command = newline
                return

    def hasMoreCommands(self):
        return self.current_command != ''


