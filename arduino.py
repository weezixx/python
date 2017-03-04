import sys
import os
import serial
import time

ser = serial.Serial("COM3",timeout=1)

# print(ser)

#while 1:
#   code = input("Code à envoyer à l'Arduino: ")
#   ser.write(code.encode('utf-8'))
maliste = []
inventaire = open("C:/Users/Kevin/Desktop/ie/tfe/code/python/magasin.txt",'r')

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

print("nom : ",nom,"\nx :" ,coord_x ,"\ny :", coord_y)
ser.write(coord_x.encode('utf-8'))
ser.write(b' ')
#time.sleep(1)
ser.write(coord_y.encode('utf-8'))
ser.write(b'\n')











