import re

batRegex = re.compile(r'Bat(wo)?man|')
mo = batRegex.search('The advetures of Batman')
print(mo.group())