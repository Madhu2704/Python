# Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit.
import collections


def log(msg=""):
    print(f"-----------------{msg}-----------------------")


dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thru'}

log('combining two dicts')
res = collections.ChainMap(dict1, dict2)

print(res.maps, '\n')
print(f'keys:{list(res.keys())}')
print(f'keys:{list(res.values())}')

log()

log("Iterating into Dict")
for key, val in res.items():
    print(f'{key}:{val}', '\n')
log()

log("Finding Key in dict")
print(f'{"day1" in res}')
log()

log("Updating the new element to dict")
dict1['day1'] = 'Sun'
print(res)
log()
