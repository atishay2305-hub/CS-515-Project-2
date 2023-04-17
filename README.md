# CS-515 Project-2 Calculator Language
Group Members:
Praneeth Gubba pgubba@stevens.edu
Atishay Jain ajain70@stevens.edu
Akash Adarsh a8@stevens.edu

#Public Repo Link: 
https://github.com/atishay2305-hub/CS-515-Project-2

#estimated hours spent: The estimated amount of hours we have spent in developing was around 10 hours for each person. So a total of 30-35 hours in total were spent in developing the code and baseline functionalities and extensions of the project. Apart from this, we have given 4-5 hours per person to test the code using our custom test inputs. 

#description of how we tested: To begin with, we ensured that the test inputs specified in the project description produced the expected outputs. Next, we created a set of additional tests in a separate file called "test.txt", which we ran locally on either a Mac or Linux terminal. We used the "diff()" command to compare the expected output with the actual output. Additionally, when running tests with the separate file, we utilized the command "python bc.py < test.txt", which is only available on Linux or MacOS terminals. We included a file with custom tests that were solely based on expressions. These tests evaluated the calculator's precedence function and analyzed its performance with varying input parameters.

#bugs and issues:
For the timer class we miss interpreted the rest functionality.Was unable to define __repr__ method correctly

#resolved issue:
After looking at expected results we changed the reset functionality and after using the hint mentioned for __repr__ it was successfully executed.

#list of four extensions we have chosen:
