---
toc: true
comments: true
layout: post
title: Lab Notebook Week 10
description: Lab Notebook Week 10
type: tangibles
courses: { compsci: {week: 10 } }
---

> ###  3.12-3.13 Developing Procedures

- A procedure is a named group of programming instructions

- 2 Main Types of Procedures:
    - Procedure that returns a value of data
    - Procedure that executes a block of statements

- Name:
- Parameters:currentweather; Weather
- Algorithm (paste lines): 
    ```
    def updateweather(currentweather, weather): 
        if currentweather> weather:
            weather = currentweather
            print("today is warmer than yesterday")
        else:
            print("today is colder than yesterday")
        return currentgrade 
    
    ```
- Return Value: return currentgrade

- Calling Procedure Line: def updateweather(currentweather, weather):
(for the code)
"def updateweather(currentweather, weather): # algorithm  + calling procedure line
    if currentweather> weather:
        weather = currentweather
        print("today is warmer than yesterday")
    else:
        print("today is colder than yesterday")
    return currentgrade # return value

currentweather = 71 # parameter
weather = 66 # parameter
currentgrade = updateweather(currentweather, weather)
print("the temperature right now is", currentweather, "degrees")"
> - Classes
 eg.
 ```
class charecter:
    hight = 10
    strenght =10
    luck = 5
 ```
 - to use a specific thing from a class
 eg. charecter.hight

 ### Javascript/add dropdown menue
 
