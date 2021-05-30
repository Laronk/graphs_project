# Graphs project
College assignment for graph theory class

## Setup

### 1. Install Python version 3.8.5:

```sh
# for debian based linux system
$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt-get update

$ sudo apt install python3.8

$ python3.8 -V
# last command should yield "Python 3.8.5"
```

### 2. Install pip - a package manager for Python

```sh
# for Debian based Linux system
$ apt install python3-pip
```

### 3. Install necessary python packages using pip

### There are two ways to go about this.

The first is to install the required packages from the `requirements.txt` file. This is the faster option, but due to system differences, some problems might arise. They shouldn't, but they might.
### 3.a Install necessary python packages using pip

```sh
# in repository root
$ pip3 install -r requirements.txt
```

The second option is to install all the required packages manually. I list all the packages in this single command.

### 3.b Install necessary python packages using pip

```sh
# in the repository root
$ pip3 install networkx matplotlib numpy
```

## Project structure

```sh
.
├── Dijkstra’s algorithm
│   ├── algorithm
│   │   ├── dijkstra.py # my algorithm implementation
│   │   └── __init__.py
│   ├── algorithm analysis.md # analitical part of the practical aspect of the assignment 
│   ├── test_dataset.json # test graphs in incidence matrix form
│   ├── test_images
│   │   └── # tests output folder - graph drawings
│   └── test.py # main file - tests file
├── Jan_Karpiuk.json # assignment original file
├── Jan_Karpiuk_proj.docx # assignment instructions
├── LICENSE # license file
├── README.md # setup instructions, 
└── requirements.txt # required python packages
```

## Run tests

### In order to check the validity of my Dijkstra's algorithm implementation:

### 1. Run all tests, use the command:

```sh
$ python Dijkstra’s\ algorithm/test.py
```

 > Successful tests should yield:

```sh
..
------------------------------------------------------------
Ran 2 tests in 2.576s

OK
```

### 2. Add graphs to be tested

Tests take the `test_dataset.json` file as a testing dataset.

In order to test more graphs, update the `test_dataset.json` file with new graph data in form of an incidence matrix

### 3. Lastly, you can go to `test_images` folder and view the test results

Each file is named according to the test in with it was created with the test number added at the end.

* `test_dijkstra_path_0.png` - __first__ graph image for test validating algorithm's dijkstra path calculation

* `test_dijkstra_path_length_5.png` - __sixth__ graph image for test validating algorithm's dijkstra path length calculation

Each file contains the image of a tested graph with Dijkstra's path marked in red for a particular test case.

## Read my analysis on Dijkstra's algorithm real-world applications - file `algorithm analysis.md`