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
 - eg.
 ```
class charecter:
    hight = 10
    strenght =10
    luck = 5
 ```
 - to use a specific thing from a class
 eg. charecter.hight

### Libraries

- Libraries that we use:
    - Pandas
    - Numpy
    - requests
    - Pillow
    - Matplotlib
    - Tenserflow
    - Scikit-Learn
- library: is a collection of pre-written code, functions, and modules that extend the language's capabilities. Essential for simplifying and accelerating the development process, as they provide a wide range of tools and functions for various purposes.
 equests - Simplifies working with HTTP servers, including 'request'-ing data from them, and recieving it
- Pillow: Simplifies image processing
Pandas: Simplifies data analysis & manipulation
- Numpy : Vastly quickens functionality of arrays up to 50 times faster than regular python list
Scikit-Learn : Implements machine learning models and statistical modelling
Tensorflow : Data automation, model tracking, performance monitoring, and model retraining
- Matplotlib : Creates static, animated, and interactive visualizations in Python
> #### Pandas
    - This code utilizes pandas in the DataFrame form to organize the data in to a table with the categories on the horizontal axis and their values on the vertical. Pandas creates a way for the user to organize data in a much simpler form and in different styles depending on what the user wants

> #### TensorFlow
    - The provided code demonstrates a basic example of linear regression using TensorFlow and Keras. It begins by importing the necessary libraries, TensorFlow and NumPy. It then generates a synthetic dataset with 1000 samples, where the input features are random, and the target values are computed as a linear combination of the input features with added noise. A data pipeline is set up using TensorFlow, which includes shuffling and batching the data for efficient processing. A simple linear regression model is defined using Keras, consisting of one dense layer. The model is compiled with the Adam optimizer and mean squared error as the loss function. It is then trained on the synthetic data for ten epochs. After training, the model is used to make predictions on new data points, and the predictions are printed to the console. This code provides a basic illustration of how to perform a simple machine learning task with TensorFlow, from data generation to model training and prediction.

> #### Matplotlib
    - The provided Python code demonstrates the basic usage of Matplotlib, a popular library for creating data visualizations. In this example, we start by importing the Matplotlib's pyplot module, often aliased as plt. We define some sample data as lists for the X and Y values. Then, we create a figure and an axis object using plt.subplots(). Next, we plot the data points on the graph with ax.plot(x, y) and set a label for the line. We also add labels for the X and Y axes and set a title for the plot. To provide context for the plot, we include a legend with the label we set earlier. Finally, plt.show() is called to display the graph. When you run this code, it will generate a simple line plot displaying the data points with appropriate labels, a title, and a legend, making it a clear and informative visualization.

### Simulation
- A simulation, in context of computer science, is a digital representation of a situation in the real world.
- bubble sort: a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which means the list is sorted.
- quick sort: It divides the array into smaller sub-arrays and recursively sorts them. It's generally more efficient than Bubble Sort for larger lists.
