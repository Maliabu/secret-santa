#total number of input must be 9 store in x
#names must be lowercase sensitive
#array of people store in y
import random
import smtplib, ssl
import getpass

y = ["ududus", "joan", "amia", "jeremy", "cathy", "baba", "prossy", "martin", "mummy"]
z = ["ududus", "joan", "amia", "jeremy", "cathy", "baba", "prossy", "martin", "mummy"]
emails = ["giramiapatricia61@gmail.com"]

# port = 587
# password = getpass.getpass("type your password and press enter: ")

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("giramiapatricia61@gmail.com", password)
#choice names must be lower case stored in z
#therefore z equals y
x = len(y)
p = len(z)

random.shuffle(z)
random.shuffle(y)
for i,j in zip(z,y):
    def censor(text, j):
        return  text.replace(j, '*' * len(j))
    while i==j:
        random.shuffle(z)
        random.shuffle(y)
    print (censor(i+" has picked "+j, j))
    

    
