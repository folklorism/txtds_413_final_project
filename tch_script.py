import re
import pandas as pd

filepath_of_text='tch.txt'
tch_full_text = open(filepath_of_text, encoding="utf-8").read()

tch_lowercase = tch_full_text.lower()
tch_split = tch_lowercase.split()
    
# using regex to get karen & martha and their associated 
# scenario/verb 

# . --> any character
# * --> zero or more
# ? --> stop ASAP
# .*? --> grabs all the chars beore the opening and closing ()
karen_pattern = r"(karen\.?).*?\((.*?)\)"
martha_pattern = r"(martha\.?).*?\((.*?)\)"
karen_scenario_result = re.findall(karen_pattern, tch_lowercase)
martha_scenario_result = re.findall(martha_pattern, tch_lowercase)

# just counting how much times & printing the mentions of 
# karen and martha in a count

karen_mention = 0
martha_mention = 0

for text in tch_split:
    if text.startswith("karen"):
        karen_mention += 1
    if text.startswith("martha"):
        martha_mention += 1

print("Karen mentions: ", karen_mention)
print("Martha mentions: ", martha_mention)

# creating a DF for the char and assocaited verbs

col_names = ['Name', 'Scenario']

karen_df = pd.DataFrame(karen_scenario_result, columns=col_names)
martha_df = pd.DataFrame(martha_scenario_result, columns=col_names)
print(karen_df)
print(martha_df)

#exporting and saving the csv files
karen_df.to_csv('karen_scenarios.csv', sep='\t', encoding='utf-8', index=False, header=True)
martha_df.to_csv('martha_scenarios.csv', sep='\t', encoding='utf-8', index=False, header=True)