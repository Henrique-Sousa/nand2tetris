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

    def getCommandType(self):
        if self.current_command.startswith('@'):
            return 'A'
        else:
            return 'C'

    def number(self):
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
            if '=' in self.current_command:
                partial = self.current_command.split('=')[1]
            else:
                partial = self.current_command.split('=')[0]
            return partial.split(';')[0]

    def jump(self):
        if self.getCommandType() == 'C':
            if ';' in self.current_command:
                return self.current_command.split(';')[1]
            else:
                return ''
        
