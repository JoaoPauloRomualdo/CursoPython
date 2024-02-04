""" Desafio 021

Faça um programa em python que abra e e reproduza um audio de arquivo mp3 """
import pygame
import time

pygame.init()

arquivo = 'Desafios/05/music.mp3'

pygame.mixer.music.load(arquivo)

pygame.mixer.music.play()

input()

pygame.event.wait