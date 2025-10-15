# №3
import random
digits = random.choices('12345678',k=3)
letters = random.choices('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',k=3)
symbols = random.choices('!@#$%^&*',k=2)
len = digits + letters + symbols
random.shuffle(len)
password = ''.join(len)
print(password)
