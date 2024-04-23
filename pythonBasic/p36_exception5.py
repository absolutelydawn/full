#!/usr/bin/env python

def division_function(a, b):
    try:
        print(a/b)
    except TypeError as e:
        return -1
    except ZeroDivisionError as e:
        return -2
    except Exception as e:
        return -3

division_function("a", 1)
division_function(1, 0)
division_function(4, 2)

