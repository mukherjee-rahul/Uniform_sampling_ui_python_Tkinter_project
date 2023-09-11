import numpy as np
import pandas as pd
import os
import pickle
import constants


class Regularize:

    def __init__(self) -> None:
        pass

    def do_task(self,file_path,csv_separator=','):
        self.data = pd.read_csv(file_path,delimiter=csv_separator)
        self.X= self.data.columns[0]
        #self.X = str.upper(self.X)
        self.Y=self.data.columns[1]

        #Store columns to file
        # Save the set to a file
        if os.path.exists("temporary_my_set.pkl"): #Check if temporary_my_set.pkl exist in the working directory
            with open('temporary_my_set.pkl', 'rb') as file:
                loaded_set = pickle.load(file)
            loaded_set.add(self.Y) # Append new columns 
            with open('temporary_my_set.pkl', 'wb') as file:
                pickle.dump(loaded_set,file) # Dump the appended set to the file temporary_my_set.pkl
        else:
            with open('temporary_my_set.pkl', 'wb') as file:
                pickle.dump({self.Y}, file)
        
        self.Start = constants.Start
        self.Stop = constants.Stop
        self.sampling_interval = constants.sampling_interval
        self.limits = [self.data[self.X].min(), self.data[self.X].max()]
        print(self.limits)

        #Check for out file existence
        if os.path.exists("temporary_out_data.csv"): #Checks if temporary_out_data.csv exists in working directory or not
            self.out_df = pd.read_csv('temporary_out_data.csv')
        else:
            depth = np.arange(self.Start,self.Stop,self.sampling_interval)
            self.out_df = pd.DataFrame({self.X:depth})
        
        def linear_interpolate(data,sampling_interval=0.4):
            interpolated_data = np.interp(self.out_df[self.X],data[self.X],data[self.Y],right=-999.25,left=-999.25)
            interpolated_data[interpolated_data==-999.25] = np.nan
            Y_new = interpolated_data
            return Y_new
        
        self.out_df[self.Y] = linear_interpolate(self.data,self.sampling_interval)
        self.out_df.to_csv('temporary_out_data.csv',index=False)

    def export_fn(self,export_file_path):
        self.export_file_path = export_file_path
        self.out_df.to_csv(self.export_file_path,index=False)
