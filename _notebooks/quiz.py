#imports the libary
import getpass, sys 
#defines the function
#promt is the questions
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg
#variables
questions = 7
correct = 0
#into words
print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test?")
#question 1
# The user input is stored in the variable rsp
# if rsp is import then your correct
rsp = question_with_response("What command is used to include other functions that were previously developed?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

#question 2
rsp = question_with_response("What command is used to evaluate correct or incorrect response in this example?")
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

#question 3
rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

#question 4
rsp= question_with_response("What key word in python defines a function?")
if rsp == "def":
    print(rsp+ " is correct!")
    correct += 1
else:
    print(rsp+ " is incorrect!")

#question 5
rsp= question_with_response("What key word turns a variable into a string?")
if rsp == "str":
    print(rsp+ " is correct!")
    correct += 1
else:
    print(rsp+ " is incorrect!")

#question 6
rsp= question_with_response("what command stores what the user types?")
if rsp == "input":
    print(rsp+ " is correct!")
    correct += 1
else:
    print(rsp+ " is incorrect!")

#question 7
rsp= question_with_response("what command is followed b 'if'?")
if rsp == "else":
    print(rsp+ " is correct!")
    correct += 1
else:
    print(rsp+ " is incorrect!")

# the value in the variable correct is divided by the value in the variable question and then multiplied by 100
# this value is saved in the variable percentage
percentage = correct/questions *100

#getpass.getuser() takes the user name  and str converts the variable correct into a string
#this is the same with the variable question
print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
print("or " + str(percentage) +"%")
# To show the percentage, the calculated value in the variable "percentage" then convert into a string 