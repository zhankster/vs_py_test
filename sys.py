# import math
# import os
# import sys

import requests

# print(sys.version)
# print(sys.executable)


# def greet(who):
#     greeting = 'Hello, {}'.format(who)
#     return greeting


# print(greet('Big Bad World'))
# print(greet('Joe P'))
### Yet another comment

r = requests.get('https://bwp.dekalbal.com')
print(r.status_code)
print(r.ok)
