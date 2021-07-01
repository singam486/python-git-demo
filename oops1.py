#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:33:27 2021

@author: pradeepa

__init()__ is an initializer
not a constructor

self can be compared with this in java,c++,javascript
"""

class Flight:
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No Airline Code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid Airline Code in '{number}'")
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError(f"InvalidRoute Number  '{number}'")    
        self._number = number
        self._aircraft = aircraft
        
    
    def number(self):
        return self._number
    def aircraft_model(self):
        return self._aircraft.model()
    
    
class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration= registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1,self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])
        
    

flight = Flight('SM1234',Aircraft('AI-6123','Airbus619',num_rows=22,num_seats_per_row=6))
print(type(flight))
print(flight.number())
print(flight._aircraft.seating_plan())

"""
aircraft = Aircraft('AI-6123','Airbus619',num_rows=22,num_seats_per_row=6)
print(aircraft.seating_plan())
"""