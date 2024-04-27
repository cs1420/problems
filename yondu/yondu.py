'''
Name: Yondu Udonta
Author: George Rudolph
Due Date: MM/DD/YYYY
Course: CS1400-000

User will input how many reavers and how much gold from keyboard.
This program will divide up units among Reavers.
The crew, not including Yondu and Peter Quill are given 3 units
for shore leave.
While the crew is gone Yondu takes 13% of the remaining gold,
Peter Quill takes 11% of the remainder after Yondu's cut.
In the morning, the rest is divided evenly among all Reavers
including Yondu and Peter.
Any remainder goes to the Pirate Benefit Fund.
Results are printed to the console.
'''


def main():
    '''
    Program starts here.
    '''
    
    '''
Project Name: Yondu Udonta (Instructor Solution)
Author: George Rudolph
Due Date: 8 May 2023
Course: CS1400-001

This version is intentionally different from previous versions
of this project.
'''

pirates = int(input('How many pirates:\n'))
units = int(input('How many units:\n'))

remainder = units - (3 * (pirates - 2))
yondu_share = round((remainder * 13) / 100, 2)
remainder -= yondu_share
peter_share = round((remainder * 11) / 100, 2)
remainder -= peter_share
crew_share = round(remainder / pirates, 2)
yondu_share += crew_share
peter_share += crew_share
print()
print(f"Yondu's share: {yondu_share:.2f}")
print(f"Peter's share: {peter_share:.2f}")
print(f"Crew's share: {crew_share + 3:.2f}")
