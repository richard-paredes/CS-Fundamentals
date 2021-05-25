# Homework 1
### Author: Richard Paredes
### UHID: 1492535
### Course: COSC4370


## Directory contents:
- report.pdf: detailed report for HW1
- hw1.cpp: source code for program
- hw1.exe: executable file for program (on Windows)
- circle.ppm: program output file
- guidelines.pdf: HW1 guidelines and requirements
- reading.pdf: supplemental reading for HW1

## To build and execute the program
Navigate to the directory containing hw1.cpp, then execute the following commands in the terminal: 

#### For Windows:
> Build command: g++ hw1.cpp -o hw1.exe

> Execute command: hw1.exe 350
> * Note: the 350 marks the window size, since the radius of the semi-circles are predefined in the homework guidelines


## Program output:
- circle.ppm: a single image file containing a 350 x 350 (variable based on arguments) pixel canvas, with two semicircles. One semicircle is of radius 150 in the plane y >= 0. The second semicircle is of radius 100 in the plane x >= 0.