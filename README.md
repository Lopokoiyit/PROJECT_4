# Project: Sudoku Solver 
**A web app that could read Sudoku puzzle from an image and provide solutions, with the final work could be accessible in [LINK](xxxxxxxxxxxxxxxxxx).**
<BR>This group project is prepared for Monash Data Analytics Bootcamp, with the purpose to demystify machine learning. The topic is chosen as handwritten digital recognition is a popular & beginner-friendly topic in machine learning and deep learning.
## What is Sudoku?
<img align="left" width="100" height="100" src="https://github.com/JasonDButt/project-4-group-5/blob/main/other/sudoku.png">
“In a classic Sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub grids that compose the grid contain all of the digits from 1 to 9, as displayed at the left” (https://en.wikipedia.org/wiki/Sudoku).
<br>
<br>

## Key Project Tools
The below outlines programs included in this project. 
<p align="center">
  <img width="460" height="300" src="https://github.com/JasonDButt/project-4-group-5/blob/main/other/strcuture.JPG">
</p>

### 1.1	Flask App
Flask app was designed to follow the flow shown below. One thing needs mentioning is as the accuracy rate of model is not 100%, so in the solution page, function for user to check and amend change has been designed through the form group from html.
<p align="center">
  <img width="460" height="300" src="https://github.com/JasonDButt/project-4-group-5/blob/main/other/flask.png">
</p>

### 1.2	Model Training & Image Reading
We are using the code [here](https://machinelearningprojects.net/sudoku-solver/) to read the image and reference its model training process.
<br>The primary dataset used is MNIST, and a network architecture of CNN is chosen. 

### 1.3	Solve Sudoku
A backtracking algorithm is used to develop the python script of solving Sudoku, with the below diagram showing the process: 
<p align="center">
  <img src="https://github.com/JasonDButt/project-4-group-5/blob/main/other/sudoku solver.png">
</p>
