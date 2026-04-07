#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:50:59 2026

@author: jordan
"""

def f(x):
    return x**3 + 8

def main():
    x = 9
    print(f(x))
    if (f(x) >29):
        print("Yay!")

if __name__ == "__main__":
    main()