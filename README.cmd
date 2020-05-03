# Create a local and a GItHub repository via Terminal command #

Terminal command: gitcr [REPOSITORY-NAME] ["REPOSITORY DESCRIPTION INSIDE QUOTES"]

1) Create a custom Terminal command to drive you to the correct directory and create and inialize a new local repository whose name is the first parameter of the terminal command and the description is the second.

2) The path of the directory (local repository) and the path of the python file are defined in the shell script.

3) The script also execute the "git init command" and the "git remote add origin..." using SSH key.

4) If a "index out of range" error ocurr while executing the python file, edit the file increasing the time.sleep(value). This error ocurrs because the "page.contet" didn't have time to load the current page. 



# Needed #

Python3.5:
	requests
	BeautifulSoup
	sys
	temp
