
help(round(-2.01))

""" Тройные кавычки документируют, что делает функция или просто добавляет описание оной"""

print(1, 2, 3, sep=' < ')

# '\n' is the newline character - it starts a new line

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',max(100, 51, 14),'Which number is the biggest modulo 5?',max(100, 51, 14, key=mod_5),
    sep='\n',)