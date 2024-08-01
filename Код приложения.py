import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import joblib
import easygui
import tkinter as tk
from tkinter import *
from tkinter import messagebox



def main():
       input_file = easygui.fileopenbox()
       input_file=pd.read_csv(input_file)
       mkb1_values=pd.read_csv("mkb1_values.csv")
       mkb2_values=pd.read_csv("mkb2_values.csv")
       crit_values=pd.read_csv("crit_values.csv")
       Pmu_values=pd.read_csv("Pmu_values.csv")

       input_file=pd.merge(input_file,mkb1_values, on=('MKB1'), how = "left")
       input_file=pd.merge(input_file,mkb2_values, on=("MKB2"), how = "left")
       input_file=pd.merge(input_file,crit_values, on=("Crit"), how = "left")
       input_file=pd.merge(input_file,Pmu_values, on=("PMU"), how = "left")
       input_file.fillna(0, inplace=True)
       X = pd.DataFrame(input_file, columns=[ 'Days', 'Prof', 'MKB1_id', 'MKB2_id', 'Sex', 'Age', 'Month', 
              'PMU_id', 'Crit_id', 'Result', 'Paysum'])


       loaded_model = joblib.load( "model.joblib")
       input_file['Exp'] = loaded_model.predict(X)
       input_file.to_csv("Результат.csv", index=False)
       window.destroy()

window = Tk()
window.title("Отбор перспектиных случаев на ЭКМП")
window.geometry('400x300')
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
cal_btn = Button(
   frame,
   text='Выбрать файл',
   command=main
)
cal_btn.grid(row=5, column=2)

window.mainloop()