import random
from random import randint

print('====================')
print('netnut.io Proxy Creator')
print('    By Kennyd')
print('====================')

username = raw_input('username: ')
password = raw_input('password: ')
while True:
    try:
        num = int(raw_input('amount of proxies?: ' ))
    except ValueError:
        print('Enter a number')
        continue
    else:
        break

proxy = 'salt146-us.netnut.io'
port = ':33128'
id = ':' + username + ':' + password




def prox(num,count):
    for i in range(0,num):
        newproxy = proxy.split('.')[0] + str(count) + port + id
        f = open("logs.txt", "a")
        f.write('{}\n'.format(newproxy))
        f.close()
        print(newproxy)

def randy(num):
    for i in range(0,num):
        dom = (random.randint(1,10))
        newproxy = proxy.split('.')[0] + str(dom) + port + id
        f = open("logs.txt", "a")
        f.write('{}\n'.format(newproxy))
        f.close()
        print(newproxy)



next = raw_input('random servers? yes or no: ')
if next.lower() == 'no':
    count = int(raw_input('which server? pick between 1-10: '))
    prox(num,count)
else:
    randy(num)
