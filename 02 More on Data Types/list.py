marvel_heros = ["spiderman","doctor strange","thor"]

dc_heros = ["batman","flash","aquaman"]

print(dc_heros[1:])
del dc_heros[0]
print(dc_heros)

dc_heros.insert(0,'batman')
print(dc_heros)

dc_heros.remove('flash')
print(dc_heros)

dc_heros.reverse()
print(dc_heros)

print(dc_heros.count('aquaman'))

print(marvel_heros+dc_heros)

