# Take inputs of sets, reps, and weight and return total output for exercise
# Store total output of exercsie in a log to reference next time(workout)
# Access exercises to find the last total output from the previous workout and the 
# reps, sets, and weight used 


import csv
from csv import DictWriter
import pandas as pd

#This is for the headers of the columns
field_names = ['Exercise', 'Sets', 'Weight', 'Reps', 'Total Output']

#This class is to display the data
class DisplayDF:
    def __init__(self):
        df = pd.read_csv('exercise_list.csv')
        print(df)

#This class is to change the data of already exisitng exercsies    
class ChangeData:
    def __init__(self, name):
        self.name = name
        keyed_sets = int(input("New Sets: "))
        keyed_weight = int(input("New Weight: ")) 
        keyed_reps = int(input("New Reps: "))
        df = pd.read_csv('exercise_list.csv')
        df.loc[df["Exercise"]==self.name, "Sets"] = keyed_sets
        df.loc[df["Exercise"]==self.name, "Weight"] = keyed_weight
        df.loc[df["Exercise"]==self.name, "Reps"] = keyed_reps
        df.to_csv("exercise_list.csv", index=False)    
        Calculate(name, keyed_sets, keyed_weight, keyed_reps)
        df = pd.read_csv('exercise_list.csv')
        print(df)

        # This will prompt to be taken back to the beginning or to add another set 
        answer = input("Would you like to change the data again or return to the main menu? Type Change/Main")
        if answer == 'Change':
            ChangeData(name)
        elif answer == 'Main':
            Prompt()

# This class is for every exercise to be added to the CSV
class Exercise:
    def __init__(self, name):
        key_name = name
        key_sets = int(input("Sets: "))
        key_weight = int(input("Weight: ")) 
        key_reps = int(input("Reps: "))
        df = pd.read_csv('exercise_list.csv')
        df.loc[name, "Exercise"] = key_name
        df.loc[name, "Sets"] = key_sets
        df.loc[name, "Weight"] = key_weight
        df.loc[name, "Reps"] = key_reps
        df.to_csv('exercise_list.csv', mode='w', index=False, header=True)
        Calculate(key_name, key_sets, key_weight, key_reps)
        df = pd.read_csv('exercise_list.csv')
        print(df)
        # This will prompt to be taken back to the beginning or to add another set
        answer = input("Would you like to change the data again or return to the main menu? Type Change/Main")
        if answer == 'Change':
            ChangeData(key_name)
        elif answer == 'Main':
            Prompt()

# This class is for calculating total outputs and adding it to the csv
class Calculate:
    def __init__(self, name, sets, weight, reps):
        df = pd.read_csv('exercise_list.csv')
        total_output = (sets * weight * reps)
        df.loc[df["Exercise"]==name, "Total Output"] = total_output
        df.to_csv('exercise_list.csv', mode='w', index=False, header=True)

# This will take user inputs to navigate between eexercsies and to create new ones
class Prompt:
    def __init__(self):
        with open('exercise_list.csv', 'r') as exercises:
            reader = csv.DictReader(exercises, fieldnames=field_names)
            answer = input("Would you like to create an exercise or modify an existing one? Enter Modify/Create:")
            if answer == 'Create':
                name = input('Exercise:')
                for row in reader:
                    if row['Exercise'] == name:
                        exercises.close()
                        ChangeData(name)
                    elif row['Exercise'] != name:
                        exercises.close()
                        Exercise(name)
            elif answer == 'Modify':
                Modify()

#This class is for directing the user after they type Modify, allowing them to choose a exercsie to modify
class Modify:
    def __init__(self):
        answer = input("Which exercise would you like to modify?")
        #with open('exercise_list.csv', 'r') as exercises:
            #reader = csv.reader(exercises)
        df = pd.read_csv('exercise_list.csv')  
        df.loc[df["Exercise"]==answer, "Exercise"] = answer
        ChangeData(answer)
        
DisplayDF()            
Prompt()