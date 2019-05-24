### ENVIROMENT VARIABLES
# Author: Filip.Lukovic
# E-mail: lukovicy@gmail.com

### OVERVIEW
# This simple piece of code is writen for practicing purposes, where I wanted to see what are the enviroment variables that ubuntu 18.04 LTS uses.
# There are two ways to acomplish that, for which I'm using bash and python.
# NOTE: Bash is being used throw Python!

# Adding necessary modules
import os
import subprocess
import time


### BASH VARIANT
# This is the easiest working variant with bash, without printing the resaults in Python, but loging them to external file
set_time_date = time.strftime('%d-%m-%Y')
new_file = "printenv-results-" + "'(" + set_time_date + ")'"
bash_Command = "printenv >> " + os.environ['HOME'] + "/Downloads/" + new_file # >> is used to overwrite everythings that was being writen to the file 'printenv-results'
output = subprocess.check_output(['bash','-c', bash_Command])


### PYTHON VARIANT
# Seeing the first list that contains all enviroment variables in linux
book_list = list(os.environ)
print("This is the list of available enviroment variables under the module 'os.environ':")
print(book_list)

# Counting the number of elements in the list
print("This is the number of available enviroment variables under the module 'os.environ':")
print(str(count))

# pojedinacne linux varijable sa njihovim vrednostima
print("These are all available enviroment variables under the module 'os.environ' with their values:")
for i in book_list:
	print(i + " = " + os.environ[i])