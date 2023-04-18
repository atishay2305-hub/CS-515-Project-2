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
We faced issues with increment and decrement operators when they are multiple operators. dealing with multiple assignment operators was not implemented correctly at beginning. Keywords check and variable name check was giving a error.

#resolved issue:
All these issues have resolved after developing variety of text cases and making code changes to work on them. Changing regular expressions thorughly helped in achieving this.

#list of four extensions we have chosen:
1) Op= , we implemented this  extension which is used to apply the operation to the first variable and second one and store the result in first operator itself . operator can be all implemented operators even 
2) We implemented relational operators which are used to compare two variables,numbers,expressions etc.,
3) We implemented boolean operations and also having op= we also implemented &&= ||=
4) Comment parsing is the last extension we implemented.We handled both inline commands and multiple line commands
