"""
    UTILIZANDO MODULOS EM PYTHON
    
São funcionalidades que conseguimos implantar dentro de nossas aplicaçoes em python

import : ele importa todas as funcionalidades que existe dentro da biblioteca que vc deseja trazer

from DOCE import PUDIM : ele ja traz especificamente uma unica função que vc quer utilizar no caso da explicação vai na biblioteca DOCE e vai importar apenas a funcionalidade PUDIM , nesse coso economizamos mais memoria em nossas aplicações  

"""

""" 
#match e uma biblioteca de operações matematicas
import match

#ele vai importar apenas a lib sqrt
from match import sqrt """

import random
from math import sqrt, floor

n1 = int(input('Digite um numero'))
#quando vc importa somente uma funcionalidade nao precisa referenciar o nome da biblioteca
raiz = sqrt(n1)

print(f'a raiz de {n1} = {floor(raiz)}')

num = random.randint(1, 300)

print(num)

import emoji

print(emoji.emojize('OLA MUNDO !! :four_leaf_clover:'))