#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:53:45 2017

@author: mikuchera
"""


import numpy as np
import time
import os

students = ["Greg", "Andrew", "Julian", "Josh", "Ella", "Henry", "Christina", \
"Alex", "Andrew", "Sam", "Martha", "Cliff", "Laura", "Esteban", "Zach", "Nancy", \
"Jack", "Brooke"]

print("there are", len(students), "students in the class. They are:")
for student in students:
    print(student, end=",   ")

students_per_group = 2

num_groups = len(students) / students_per_group

print("\n\nThere are",num_groups, "groups in the class.")

np.random.shuffle(students)

for i in range(0,int(num_groups)):
    print("\ncomputer ",i,": ",students[i*students_per_group],"and" ,students[i*students_per_group+1],end=" ")
  #  print(students[i*students_per_group],"and " ,students[i*students_per_group+1] )

if(len(students)%students_per_group != 0):
    print("and" ,students[-1])

    
    
    
input("\n\nPress `Enter` when ready to start pair programming:")
inp_min = input('How much time do the students have in minutes? ')
minutes = float(inp_min)
tot_time = minutes * 60
inp_turn = input('How much time is one turn in minutes?')
one_turn = float(inp_turn)*60
print("\nStart coding!")
for t in range(0,int(tot_time/one_turn)):
    time.sleep(one_turn)
    print("Time to switch roles!")
    os.system('say "Switch roles!"')