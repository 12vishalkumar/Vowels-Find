import re
st = input()
mt = re.findall(r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])', st, re.I)
print('\n'.join(mt or ['-1']))