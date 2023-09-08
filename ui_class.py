import tkinter as tk
from tkinter import filedialog
import pickle
import os
from utils_class import Regularize
import constants

#Tkinter object creation
root = tk.Tk()
root.title("File Upload and Export")
# UI geometry width x height + locationx + locationy
root.geometry('1024x656+15+15')
#Regularize class object creation
rglr = Regularize()

def submit_values():
    var1 = var1_entry.get()
    if var1:
        constants.Start = float(var1)
    else:
        pass
    var2 = var2_entry.get()
    if var2:
        constants.Stop = float(var2)
    else:
        pass
    var3 = var3_entry.get()
    if var3:
        constants.sampling_interval = float(var3)
    else:
        pass

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        rglr.do_task(file_path)
    else:
        print("No file selected.")
    

def add_list_box():

    listbox.delete(0, tk.END) #Clearing the listbox before displaying
    with open('temporary_my_set.pkl', 'rb') as file:
        loaded_set = pickle.load(file)
    for col in loaded_set:
        listbox.insert(tk.END, col)

def export_csv():
    directory_path = filedialog.askdirectory()
    if directory_path:
        file_path = f"{directory_path}/exported_dataframe_{rglr.Start}m_to_{rglr.Stop}m_sampling_{rglr.sampling_interval}m.csv"
        rglr.export_fn(file_path)
        print("DataFrame exported to:", file_path)
        delete_temporary_files()
    else:
        print("Export cancelled.")

def delete_temporary_files():
    files = ['temporary_out_data.csv','temporary_my_set.pkl']
    for file in files:
        os.remove(file)

# Create Entry widgets for the three variables
#Var 1 for Start deppth
var1_label = tk.Label(root, text="Start depth (in meters):")
var1_label.pack()
var1_entry = tk.Entry(root)
var1_entry.insert(0,constants.Start)
var1_entry.pack()
# VAr 2 for stop depth
var2_label = tk.Label(root, text="Stop depth (in meters):")
var2_label.pack()
var2_entry = tk.Entry(root)
var2_entry.insert(0,constants.Stop)
var2_entry.pack()
# VAr 3 for stop depth
var3_label = tk.Label(root, text="Sampling interval (in meters):")
var3_label.pack()
var3_entry = tk.Entry(root)
var3_entry.insert(0,constants.sampling_interval)
var3_entry.pack()

# Button to get the variable values
submit_values_button = tk.Button(root, text="Submit values / Change values", command=submit_values)
submit_values_button.pack()



# File upload button
upoad_button = tk.Button(root, text="Upload Files one by one", command=upload_file)
upoad_button.pack(pady=30)

# Update listbox button
check_items_button = tk.Button(root, text="Check the columns inserted:", command=add_list_box)
check_items_button.pack()
# Create a Listbox to display the items
listbox = tk.Listbox(root)
listbox.pack()

# Create a button to export the DataFrame as CSV
export_button = tk.Button(root, text="Export CSV", command=export_csv)
export_button.pack(pady=30)

# Start the Tkinter main loop
root.mainloop()