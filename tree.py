# Python program to draw a tree using turtle 
# Importing required modules
import turtle
import math
  
  
# Function to draw rectangle
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
  
      
# Function to draw triangle    
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
  
      
# Set the background color
screen = turtle.Screen ( )
screen.bgcolor("skyblue")
  
  
# Creating turtle object
tip = turtle.Turtle()
tip.color ("black")
tip.shape ("turtle")
tip.speed (2)
  
  
# Tree base
tip.penup()
tip.goto(100, -130)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")
  
  
# Tree top
tip.penup()
tip.goto(65, -90)
tip.pendown()
drawTriangle(tip, 90, "lightgreen")
tip.penup()
tip.goto(70, -45)
tip.pendown()
drawTriangle(tip, 80, "lightgreen")
tip.penup()
tip.goto(75, -5)
tip.pendown()
drawTriangle(tip, 70, "lightgreen")