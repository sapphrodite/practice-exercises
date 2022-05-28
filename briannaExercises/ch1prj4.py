# Brianna Albergaria
# Python Exercises

# Chapter 1 - Project 4
# The German mathematician Gottfried Leibniz developed the following method
# π/4 = 1 – 1/3 + 1/5 – 1/7 + …
# to approximate the value of π:
# Write a program that allows the user to specify the number of iterations used in
# this approximation and displays the resulting value.

###############################################################################

n = int(input("Enter the number of iterations: ")) # prompt user for input
toggleSign = 1 # initialize sign toggle variable
piEstimate = 0 # initialize current estimate for pi

for i in range(1,n): # for loop that iterates n times (defined by user)
    piEstimate += toggleSign * 4/(2*i-1) # add sum to previous estimate
    toggleSign *= -1 # toggle sign for each iteration

print(f"The estimate for pi using {n} iterations is {piEstimate}.") # print