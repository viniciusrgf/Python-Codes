ref = open("atp_matches_2017.csv", 'r', encoding = 'utf8')
l = []
hard = {}
clay = {}
grass = {}
c = 0
for linha in ref:
    campo = linha.split(",")[2]
    name = linha.split(",")[10].replace('"', '')
    if name not in hard:
        hard[name] = 1
    if name not in grass:
        grass[name] = 1
    if name not in clay:
        clay[name] = 1
    if campo == 'Hard':
        hard[name]+=1
    if campo == 'Clay':
        clay[name]+=1
    if campo == 'Grass':
        grass[name]+=1
duro = max(hard,key = lambda k: hard[k])
grama = max(grass,key = lambda k: grass[k])
cimento = max(clay,key = lambda k: clay[k])
print('grama',grama,'com um total de vitorias',grass[grama])
print('cimento',cimento,'com um total de vitorias',clay[cimento])
print('duro',duro,'com um total de vitorias', hard[duro])