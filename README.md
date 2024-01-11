## Inventory Management System

1) Install Python version 3.11

2) Create a new virtual environment - inventory_env using the following command:
	python -m venv inventory_env
	
3) Activate the virtual environment using the following command:
	inventory_env\Scripts\activate
	
4) Install the required libraries using requirements.txt file using the following command:
	pip install -r requirements.txt
	
5) To build this application as a package, create setup.py file. It contains information about the package, such as its name, version, dependencies, and instructions for installing it.
Run the following command for it's execution:
	python setup.py install

6) Create .gitignore file. The files we add in it are any files that do not need to get committed. You may not want to commit them for security reasons or because they are local to you and therefore unnecessary for other developers working on the same project as you.

7) Create the project structure such as src folder - init file, log file, exeception file and folders related to notebook activities.

8) Execute the following command to run any cell within python notebook else you will get error while ruuning those cells:
	pip install ipykeren
	
9) While running the cells in python notebook, select the environment relavent to your project.