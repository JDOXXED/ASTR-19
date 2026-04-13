#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:10:05 2026

@author: jordan
"""

class Animal:
    def __init__(self, arm_len, leg_len, num_eyes, has_tail, is_furry):
        self.arm_len = arm_len
        self.leg_len = leg_len
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
    
    def characteristics(self):
        print("Animal Characteristics:")
        print(f"Arm length: {self.arm_len}")
        print(f"Leg length: {self.leg_len}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail?: {self.has_tail}")
        print(f"Is furry?: {self.is_furry}")
        
def main():
    my_dog = Animal(1.5, 1.5, 2, True, True)
    
    my_dog.characteristics()
    
if __name__ == "__main__":
    main()
