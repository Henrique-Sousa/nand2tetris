import re

class Parser:
        
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.current_command = '\n' 
        self.advance()

    def __del__(self):
        self.file.close()

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

    def getCommandType(self):
        if self.current_command.startswith('@'):
            return 'A'
        else:
            return 'C'

    def isSymbol(self):
        return bool(re.search('[A-Za-z]', self.current_command)) and self.getCommandType() == 'A'

    def address(self):
        if self.getCommandType() == 'A':
            return self.current_command.strip('@')
        else:
            return None

    def dest(self):
        if self.getCommandType() == 'C':
            if '=' in self.current_command:
                return self.current_command.split('=')[0]
            else:
                return ''

    def comp(self):
        if self.getCommandType() == 'C':
            command = self.current_command.split('//')[0].strip()
            if '=' in command:
                partial = command.split('=')[1]
            else:
                partial = command
            return partial.split(';')[0]

    def jump(self):
        if self.getCommandType() == 'C':
            if ';' in self.current_command:
                return self.current_command.split(';')[1]
            else:
                return ''
        
