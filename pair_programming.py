#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

pair programming code for in-class activities.



@author: M.P. Kuchera
@date: 1.29.2018
@brief: randomly assigns partners to tables and does the pair-programming
        timing.
"""


import numpy as np
import time
import os
import sys

# global variables
students = ["Michelle Kuchera", "Jack Taylor", "Anthony Kuchera", "Alex Karbo", "Maggie Perry", \
            "Matt Perry", "Zuri Brandt", "Mark Newman", "Paul Tipler"]


def main():
    
    print("there are", len(students), "students in the class. They are:")
    for student in students:
        print(student, end=",   ")
    
    students_per_group = 2
    
    num_groups = len(students) / students_per_group
      
    print("\n\nThere are",num_groups, "groups in the class.")
    
    np.random.shuffle(students)
    
    for i in range(0,int(num_groups)):
        print("\nTable ",i+1,": ",students[i*students_per_group],"and" ,students[i*students_per_group+1],end=" ")
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
    os.system('say "Start Coding!"')
    
    for t in range(0,int(tot_time/one_turn)):
        time.sleep(one_turn)
        print("Time to switch roles!")
        sys.stdout.flush()
        os.system('say "Switch roles!"')
    
    time.sleep(one_turn)
    print("Time is up")
    sys.stdout.flush()
    os.system('say Time is up. ')
if __name__ == "__main__":
    main()
    