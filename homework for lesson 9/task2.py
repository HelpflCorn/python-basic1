# Task 2

# The sys module.

#  The “sys.path” list is initialized from the PYTHONPATH environment variable. 
# Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
# Run some interactive tests to find it out.

import sys
print(sys.path)

sys.path.append('/home/illia/Documents/python-basic1') #this should add a directory to system path and let python import from this directory
print(sys.path)
from task08_07 import digit_check #this was imported successfully

sys.path.remove('/home/illia/Documents/python-basic1')  #this should remove the directory

print(sys.path)