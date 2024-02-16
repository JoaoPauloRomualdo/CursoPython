""" 
Desafio 018

Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo """
import math

angulo = float(input('Digite o angulo que você deseja calcular : '))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print(f'O angulo digitado foi {angulo}')

print(f'O seno do angulo {angulo} sera : {seno:.2f}')

print(f'o seu cosseno do angulo {angulo} sera : {cosseno:.2f}')

print(f'a tangente do angulo {angulo} sera : {tangente:.2f}')
