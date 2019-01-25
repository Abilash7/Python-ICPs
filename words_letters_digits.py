s = 'some string'


numbers = sum(c.isdigit() for c in s)
letters   = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)

others  = len(s) - numbers - letters - spaces
print('Digits:', numbers)
print('Letters:', letters)
print('Spaces:', spaces)
print('Words:', spaces+1)
