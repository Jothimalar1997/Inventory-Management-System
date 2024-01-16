## Inventory Management System

### Guidelines
	
	### Install Python version 3.11
	
	### Project Structure:
		1) inventory_env -  Virtual environment
			-> Create a new virtual environment - inventory_env using the following command:
				python -m venv environment_name  -> Here the environment_name is inventory_env
		
			-> Activate the virtual environment using the following command:
				environment_name\Scripts\activate  -> Here inventory_env\Scripts\activate
		
		2) requirements.txt
			Install the required libraries using requirements.txt file using the following command:
				pip install -r requirements.txt
		
		3) setup.py
			-> To build this application as a package, create setup.py file. It contains information about the package, such as its name, version, dependencies, and instructions for installing it.
			-> Run the following command for it's execution:
				python setup.py install
	
		4) .gitignore file
			 The files we add in it are any files that do not need to get committed. You may not want to commit them for security reasons or because they are local to you and therefore unnecessary for other developers working on the    same project as you.
			
		5) noteboook folder - Research work related to projects
			-> Execute the following command to run any cell within python notebook else you will get error while ruuning those cells:
				pip install ipykernel
			-> While running the cells in python notebook, select the environment relavent to your project.
		
		6) src folder -> Contains all the files and data used for project execution.
			-> It consists of data folder(Inventory Data), logger file, exception file, streamlit file used for UI purpose, utils file containing python code
			-> It consists of data folder(Inventory Data), logger file, exception file, __init__.py file, streamlit file used for UI purpose, utils file containing python code
			-> __init__.py is a special Python file that is used to indicate that the directory it is in should be treated as a Python package.It is only used to initialize the package when it is imported, and the contents of the file are executed as part of the import process.This file is typically empty, but it can be used to perform initialization tasks for the package, such as setting variables or defining submodules.The __init__.py file is required for the package to be importable, and it is used by the import system to find and load the package when it is imported.
	
	### Front User Interface:
		1) For the frontend user interface, install streamlit using the following command:
			pip install streamlit
		2) To run the streamlit python file, use the following commands:
			streamlit run filename.py -> Here streamlit run streamlit.py
