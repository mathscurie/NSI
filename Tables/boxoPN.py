#!/usr/bin/env python
# coding: utf-8

liste=['GildasB','LeonB','FabianBYB','AlexandreD','KelyanD','IlanG','CarlaL','MelvinL','ThibaultL','EliottL',
      'AxelM','MarionM','EmmaNV','JosephN','EstebaneP','RomainP','SimonRL','LilianR']

from random import random

def creeFichier(eleve):
    nomFichier='boxo'+eleve+'.csv'
    sortie=open(nomFichier,'w')
    entree=open('boxo.csv','r')
    lignes=entree.readlines()
    sortie.write(lignes[0])
    for numero in range(1,len(lignes)):
        if random()<0.8:
            sortie.write(lignes[numero])
    sortie.close()
    entree.close()

for n in liste: 
    creeFichier(n)


