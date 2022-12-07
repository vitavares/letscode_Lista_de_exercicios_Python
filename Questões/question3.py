'''Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.'''

import math
raio = float(input('Qual o raio do círculo ?  '))
area = round(math.pi * (raio ** 2))
print('A área deste círculo é ', area)