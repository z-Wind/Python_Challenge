# http://www.pythonchallenge.com/pc/return/disproportional.html
__author__ = 'chihchieh.sun'

import xmlrpc.client

phonebook = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(list(phonebook.system.listMethods()))

print(phonebook.phone('Bert').lower())