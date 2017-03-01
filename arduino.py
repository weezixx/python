import sys
import os
#import serial

#ser = serial.Serial("COM3",timeout=1)

# print(ser)

#while 1:
#   code = input("Code à envoyer à l'Arduino: ")
#   ser.write(code.encode('utf-8'))
maliste = []
inventaire = open("C:/Users/Kevin/Desktop/ie/tfe/code/python/magasin.txt",'r')

#Comment mettre a jour mon code sur github via pycharm ??????

nom = ""
coord_x = 0
coord_y = 0

pieces = inventaire.readlines()

inventaire.close()

requete = input("Que désirez vous ?")


for piece in pieces:
    maliste = piece.split(" ")

    if (maliste[0] == requete):

        nom = maliste[0]
        coord_x = maliste[1]
        coord_y = maliste[2]

print(nom, coord_x , coord_y)









