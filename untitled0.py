# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:12:44 2022

@author: Johan
"""
import datetime

d = datetime.date

list = []

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
        
    def __str__(self):
        return 'Avtalen {self.tittel} finner sted ved {self.sted}, starter {self.starttidspunkt} og varer i {self.varighet} timer.'.format(self=self)
        
while True:
    try:
        tittel = input('Tittel på avtale: ')
        sted = input('Hvor er avtalen?: ')
        starttidspunkt = int(input('Skriv inn tid i dette formatet HHMM: '))
        varighet = int(input('Skriv inn varighet som et heltall i timer: '))
        break
    except ValueError:
        print('Bruk kun tall for å skrive starttidspunkt.')
      

for obj in list:
    obj.__str__
    print(obj)
            
    

avtale_1 = Avtale(tittel, sted, starttidspunkt, varighet)

print(avtale_1)

