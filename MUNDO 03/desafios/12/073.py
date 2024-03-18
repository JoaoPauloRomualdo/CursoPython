""" 
Desafio 73

Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato de futebol , na ordem de colocação. Depois mostre:
    * Apenas os 5 primeiros colocados
    * Os ultimos 4 colocados da tabela
    * Uma lista com times em ordem alfabética
    * Em que posição na tabela esta o time da chepecoense. """


clubes = (
    'PALMEIRAS',
    'GRÊMIO', 
    'ATLÉTICO-MG',
    'FLAMENGO',
    'BOTAFOGO',
    'RED BULL BRAGANTINO',
    'FLUMINENSE',
    'ATHELETICO-PR',
    'INTERNACIONAL',
    'FORTALEZA',
    'SÃO PAULO',
    'CUIABÁ',
    'CORINTHIANS',
    'CRUZEIRO',
    'VASCO',
    'BAHIA',
    'SANTOS',
    'GOIÁS',
    'CORITIBA',
    'AMÉRICA-MG'
)
clubes_indexados = tuple(enumerate(clubes, start=1))
print('-='*30)
print()
print('CINCO PRIMEIROS COLOCADOS')
print()
print(clubes[:5])#Lista com os 5 primeiros colocados
print()
print('-='*30)

print()
print('QUATROS ULTIMOS CLUBES')
print()
print(clubes[-4:])#Lista com os 4 ultimos clubes 
print()
print('-='*30)

print()
print('LISTA DOS CLUBES EM ORDEM ALFABÉTICA')
print()
print(f'{sorted(clubes)}')#Lista com times em ordem alfabética
print()
print('-='*30)

for pos,i in clubes_indexados:
    print(f'{pos} - {i}') 
get_clube = str(input('Digite qual clube você deseja saber sua colocação : ')).upper()[:    3]
for pos, clube in clubes_indexados:
    if get_clube in clube:
        print(f'O clube {clube} está na posição {pos}.')