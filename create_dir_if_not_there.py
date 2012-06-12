# Script Name		: create_dir_if_not_there.py
# Author				: Craig Richards
# Created				: 09th January 2012
# Last Modified		: 
# Version				: 1.0
# Modifications		: 

# Description			: Checks to see if a directory exists in the users home directory, if not then create it

import os												# Import the OS module
home=os.path.expanduser("~")				# Set the variable home by expanding the users set home directory
print home												# Print the location
if not os.path.exists(home+'/testdir'):		# Check to see if the directory exists
  os.makedirs(home+'/testdir')					# If not create the directory, inside their home directory