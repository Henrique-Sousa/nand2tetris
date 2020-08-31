class Parser:
        
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.current_command = '\n' 
        self.advance()

    def advance(self):
        while True:
            newline = self.file.readline()
            if newline == '':
                self.current_command = ''
                return newline 
            newline = newline.strip()
            if newline == '' or newline.startswith('//'):
                continue
            else:
                self.current_command = newline
                return

    def hasMoreCommands(self):
        return self.current_command != ''


