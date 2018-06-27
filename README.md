# Python For Bioinformatics

Introduction to Python for Bioinformatics - available at https://github.com/kipkurui/Python4Bioinformatics.

<small><small><i>

## Attribution
This is an adaptation of the Introduction to Python for Maths by [Andreas Ernst](http://users.monash.edu.au/~andreas), available from https://gitlab.erc.monash.edu.au/andrease/Python4Maths.git. The original version was written by Rajath Kumar and is available at https://github.com/rajathkumarmp/Python-Lectures.

These notes have been greatly amended and updated for the EANBiT Introduction to Python for Bioinformatics by [Caleb Kibet](https://twitter.com/calkibet) and Audrey Mbogho. 
</small></small></i>

# Quick Introduction to Jupyter Notebooks

Throughout this course, we will be using Jupyter Notebooks. Although the HPC you will be using will have Jupyter setup, these notes are provided for you want to set it up in your Computer. 

## Introduction
The Jupyter Notebook is an interactive computing environment that enables users to author notebooks, which contain a complete and self-contained record of a computation. These notebooks can be shared more efficiently. The notebooks may contain:
* Live code
* Interactive widgets
* Plots
* Narrative text
* Equations
* Images
* Video

It is good to note that "Jupyter" is a loose acronym meaning Julia, Python, and R; the initial languages supported by Jupyter. 

The notebook can allow a computational researcher to create a reproducible documentation of their research. As Bioinformatics is datacentric, use of Jupyter Notebooks increases research transparency, hence promoting open science. 

## First Steps

### Installation

1. [Download Anaconda](https://www.anaconda.com/download/) for your specific OS to your home directory
    - Linux: `wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh`
    - Mac: `curl https://repo.anaconda.com/archive/Anaconda3-5.2.0-MacOSX-x86_64.sh`
2. Run:
    - `bash Anaconda3-5.2.0-Linux-x86_64.sh`
    - `bash Anaconda3-5.2.0-MacOSX-x86_64.sh`
3. Follow all the prompts: if unsure, accept defaults
4. Close and re-open your terminal
5. If installation is successful, you should see a list of installed packages with
    - `conda list`
If the command cannot be found, you can add Anaconda bin to path using:
    ` export PATH=~/anaconda3/bin:$PATH`

For reproducible analysis, you can [create a conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html) with all the Python packages you used.

    `conda create --name my-env python jupyter`
    
To activate the conda environment:
    `source activate myenv`

Having set-up conda environment, you can install any package you need using pip. 

`conda install jupyter`
`conda install -c conda-forge jupyterlab`

or by using pip

`pip3 install jupyter`

Then you can easily launch it using:

`jupyter notebook` or `jupyter lab`

NB: We will use jupyter lab in the training. 


A Jupyter notebook is made up of a number of cells. Each cell can contain Python code. You can execute a cell by clicking on it and pressing `Shift-Enter` or `Ctrl-Enter` (execute without moving to the next line). 

    
### Further help

To learn more about Jupyter notebooks, check [the official introduction](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb) and [some useful Jupyter Tricks](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/). 

Book: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf

# Python for Bioinformatics

## Introduction

Python is a modern, robust, high-level programming language. It is very easy to pick up even if you are completely new to programming. 

Python, similar to other languages like Matlab or R, is interpreted hence runs slowly compared to C++, Fortran or Java. However, writing programs in Python is very quick. Python has a very large collection of libraries for everything from scientific computing to web services. It caters for object-oriented and functional programming with a module system that allows large and complex applications to be developed in Python. 

These lectures are using Jupyter notebooks which mix Python code with documentation. The python notebooks can be run on a web server or stand-alone on a computer.


## Contents

This course is broken up into a number of notebooks (lectures).
### Session 1
* [00](Intro-to-Python/00.ipynb) This introduction with additional information below on how to get started in running python
* [01](Intro-to-Python/01.ipynb) Basic data types and operations (numbers, strings) 
* [02](Intro-to-Python/02.ipynb) String manipulation 
### Session 2
* [03](Intro-to-Python/03.ipynb) Data structures: Lists and Tuples
* [04](Intro-to-Python/04.ipynb) Data structures (continued): dictionaries
* [05](Intro-to-Python/05.ipynb) Control statements: if, for, while, try statements
### Session 3
* [06](Intro-to-Python/06.ipynb) Functions
* [07](Intro-to-Python/07.ipynb) Scripting with python
* [08](Intro-to-Python/08.ipynb) Data Mungling with Pandas
* [09](Intro-to-Python/09.ipynb) Introduction to NumPy


### Advanced notebooks
I will add an advanced Python for Bioinformatics notebook, for the curious participants. This will introduce the use of Bioinformatics-specific python packages.


This is a tutorial style introduction to Python. For a quick reminder/summary of Python syntax, the following [Quick Reference Card](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html) may be useful. A longer and more detailed tutorial style introduction to python is available from the python site at: https://docs.python.org/3/tutorial/


## Installation

### Login into the web server
The easiest way to run this and other notebooks for the EANBiT course participants is to log into the Jupyter server. The steps for running notebooks are:
* Log in using the username and password assigned to you. The first time you log in an empty account will automatically be set up for you.
* Press the start button (if prompted by the system)
* Use the menu of the jupyter system to upload a .ipynb python notebook file or to start a new notebook.

### Installing 

Python runs on Windows, Linux, Mac and other environments. There are many python distributions available. However, the recommended way to install python under Microsoft Windows or Linux is to use the Anaconda distribution available at [https://www.continuum.io/downloads]. Make sure to get the Python *3.5* version, not 2.7. This distribution comes with the [SciPy](https://www.scipy.org/) collection of scientific python tools as well as the iron python notebook.

## How to learn from this resource?

Download all the notebooks from [https://github.com/kipkurui/Python4Bioinformatics]. For the EANBiT course, we have initialized you Jupyter lab session with all the required resources. (Confirm this has been set up before the course)

In case they are not provided, you can simply clone the GitHub repository to you jupyter lab session using the following command:

clone https://github.com/kipkurui/Python4Bioinformatics.git

Cell > All Output > Clear

This will clear all the outputs and now you can understand each statement and learn interactively.

## How to Contribute

To contribute, fork the repository, make some updates and send me a pull request. 

Alternatively, you can open an issue. 

## License
This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
