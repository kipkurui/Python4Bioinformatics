<small><small><i>
Introduction to Python for Bioinformatics - available from [provide link later](test.com).

This is an adaptation of the Introdcution to Python for Maths by [Andreas Ernst](http://users.monash.edu.au/~andreas) , available from  https://gitlab.erc.monash.edu.au/andrease/Python4Maths.git. The original version was written by Rajath Kumar and is available at https://github.com/rajathkumarmp/Python-Lectures.

These notes have been amended and updated for the EANBiT Introduction to Python for Bioinfomatics by Caleb Kibet and Audrey.  
</small></small></i>

# Python-Lectures

## Introduction

Python is a modern, robust, high level programming language. It is very easy to pick up even if you are completely new to programming. 

Python, similar to other languages like matlab or R, is interpreted hence runs slowly compared to C++, Fortran or Java. However writing programs in Python is very quick. Python has a very large collection of libraries for everything from scientific computing to web services. It caters for object oriented and functional programming with module system that allows large and complex applications to be developed in Python. 

These lectures are using jupyter notebooks which mix Python code with documentation. The python notebooks can be run on a webserver or stand-alone on a computer.

To give an indication of what Python code looks like, here is a simple bit of code that defines a set $N=\{1,3,4,5,7\}$ and calculates the sum of the squared elements of this set: $$\sum_{i\in N} i^2=100$$

## Choose a Bioinformatics-centric example
```python
N={1,3,4,5,7}
print('The sum of ∑_i∈N i*i =',sum( i**2 for i in N ) )
```

    The sum of ∑_i∈N i*i = 100


## Contents

This course is broken up into a number of notebooks (chapters).

* [00](Intro-to-Python/00.ipynb) This introduction with additional information below on how to get started in running python
* [01](Intro-to-Python/01.ipynb) Basic data types and operations (numbers, strings) 
* [02](Intro-to-Python/02.ipynb) String manipulation 
* [03](Intro-to-Python/03.ipynb) Data structures: Lists and Tuples
* [04](Intro-to-Python/04.ipynb) Data structures (continued): dictionaries
* [05](Intro-to-Python/05.ipynb) Control statements: if, for, while, try statements
* [06](Intro-to-Python/06.ipynb) Functions
We may only go this far in the lecturers, but we can keep the rest for update latter on. 

* [07](Intro-to-Python/07.ipynb) Classes and basic object oriented programming
* [08](Intro-to-Python/08.ipynb) Scipy: libraries for arrays (matrices) and plotting
* [09](Intro-to-Python/09.ipynb) Mixed Integer Linear Programming using the mymip library
* [10](Intro-to-Python/10.ipynb) Networks and graphs under python - a very brief introduction
* [11](Intro-to-Python/11.ipynb) Using the numba library for fast numerical computing.
    

This is a tutorial style introduction to Python. For a quick reminder / summary of Python syntax the following [Quick Reference Card](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html) may be useful. A longer and more detailed tutorial style introduction to python is available from the python site at: https://docs.python.org/3/tutorial/


## Installation

### Loging into the web server
The easiest way to run this and other notebooks for the EANBiT course participants is to log into the Jupyter server at [https://sci-web17-v01.ocio.monash.edu.au/hub]. The steps for running notebooks are:
* Log in using the username and password assigned to you. The first time you log in an empty account will automatically be set up for you.
* Press the start button (if prompted by the system)
* Use the menu of the jupyter system to upload a .ipynb python notebook file or to start a new notebook.

### Installing 

Python runs on windows, linux, mac and other environments. There are many python distributions available. However the recommended way to install python under Microsoft Windows or Linux is to use the Anaconda distribution available at [https://www.continuum.io/downloads]. Make sure to get the Python *3.5* version, not 2.7. This distribution comes with the [SciPy](https://www.scipy.org/) collection of scientific python tools as well as the iron python notebook.

To open a jupyter lab session with anaconda installed, from the terminal run:

    jupyter lab
    
If you only need the notebook, use:

    jupyter notebook

We will use ```jupyter lab``` in this course. 

## How to learn from this resource?

Download all the  notebooks from [https://gitlab.erc.monash.edu.au/andrease/Python4Maths]. For the EANBiT course, we have initialized you Jupyter lab session with all the required resources. 

In case they are not provided, you can simply clone the GitHub repository to you jupyter lab session using the following command:

    clone 
    
Cell > All Output > Clear

This will clear all the outputs and now you can understand each statement and learn interactively.


## License
This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
