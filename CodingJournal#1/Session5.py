#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:54:56 2026

@author: jordan
"""

import numpy as np

def main():
    x_values = np.linspace(0, 2*np.pi,1000)
   
    print("x\tsin(x)")
    
    for x in x_values:
        y = np.sin(x)
        print(f"{x:.3f}\t{y:.3f}")

if __name__ == "__main__":
    main()

