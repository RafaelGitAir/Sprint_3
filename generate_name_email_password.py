import random

class GenerateNameEmailPassword:	
    alphabet = [chr(i) for i in range(97, 123)]
    
    def __init__(self):
        self.name = ''
        self.email = ''
        self.password = ''
    
    def gerate_name(self):
        for _ in range(6):
            self.name += random.choice(self.alphabet)
        return self.name
    def generate_email(self, name):
        domen = ''
        for i in range(6):
            if i != 3:
                domen += random.choice(self.alphabet)
            else:
                domen += '.'
        self.email =  self.name + "@" + domen
        return self.email
    def generate_password(self):
        self.password = str(random.randrange(100000, 1000000))
        return self.password
