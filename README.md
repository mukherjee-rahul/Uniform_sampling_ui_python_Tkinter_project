# Uniform_sampling_ui_python_Tkinter_project
Helps to resample irregular sampled data to a regular sampled data by doing linear interpolations.
UI is built on Tkinter library, which comes preintalled with python.

ui_class.py is the main file.
Keep the three files i.e. contants.py, ui_class.py and utils_class.py in same directory/folder.
Execute 'ui_class.py' through python, it will open up the ui window.
You can run the ui_class.py' script file from your fav IDE as well.
It was tested in vscode and also you can execute the script from command prompt:

**To execute in command propmpt of windows**:
Note: You need to have 'python' installed in your computer. To check if it is installed, simply open
command prompt and type command:
python or python3
It should start python interpreter in command line.

First locate to the files where you saved the 3 scripts (contants.py, ui_class.py and utils_class.py)
You can use cd to change directory. Then after you have reached the folder/directory where the 3 files
are located; simply type the command in command prompt:

python ui_class.py

The above command should start your UI.
It was tested in python version: Python 3.10.0

**About the UI**
It contains Start, Stop and sampling_interval. It is to be entered by the user

After that you can upload a csv file which should have two columns: first one should be the index column in my case it was Depth
There must be column name as well.( Sample data 'Caliper.csv' is provided) to understand the format of the file
Then you can check the columns with the button and finally export the resampled file.
