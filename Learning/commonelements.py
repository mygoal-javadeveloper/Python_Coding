
females = set(['marge', 'maude', 'lisa', 'maggie', 'edna' ])
Simpsons = set(['homer', 'marge', 'bart', 'lisa', 'maggie'])
commonelements = set(females&Simpsons)
print(commonelements)
commonelements_a = set([x for x in females if x in Simpsons])
print(commonelements_a)
