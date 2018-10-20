# Exercise 1: Exploration and Mapping

## How-To
This Git repository contains the ROS/Catkin package for lab exercise 1.

### Where to Clone
This repository should be cloned into a catkin workspace's `src/` folder. For example, `~/repos/src/` on the Leonard laptop.

### Build the Package
To build the lab-exercise-1 package, run `catkin_make` inside your catkin workspace. Note that this will also build all other packages in the given workspace. For example, run `cd ~/repos/ && catkin_make` on the Leonard laptop.

### Commit & Push from Leonard Laptop
To commit and push code changes from the Leonard laptop, the following process should be followed:
1. `git commit --author="GitHub Full Name <GitHub Email Address>" -m "A commit message"`, for example, `git commit --author="Sam Chatfield <samchatfield97@gmail.com>" -m "Changed example.py to do A instead of B"`
2. `git push` and enter your GitHub email address and password when prompted
3. The commit will then be displayed in GitHub as being "authored by \<you\>" and "committed by Leonard"

## Exercise Specification

### Objective
The objective of this exercise is to develop your ability to program the P3DX robot using ROS (and any other programming language of your choice). You will also learn to using existing ROS modules and develop components to be used in subsequent exercises.

### Task
Design and program your robot to explore the lower ground floor of the School of Computer Science. The robot should explore as much of the floor area as possible without getting stuck, and build a map of this area. You may use any techniques of your choice. The desired outcome of this task is a map of the area explored. Please remember that you will use your map of this area for the next exercise (on localization). You will also submit a two-page report on Canvas (11-point font, single-space) describing the techniques used to complete this task, along with a description of lessons learned or challenges faced while completing this task. Demos will be due in your assigned lab session on October 24 or 25.