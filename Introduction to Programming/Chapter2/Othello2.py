'''
Created on 12 jan. 2017

@author: tos340
'''


#constants
MILI = 1000
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_MINUTE = 60

#input
time_1 = float(raw_input('Enter the time the black player thought: '))
time_2 = float(raw_input('Enter the time the white player thought: '))

#calculate
if time_1 > time_2:
    human_thought_time_in_milisec = time_1
    computer_thought_time_in_milisec = time_2
else:
    human_thought_time_in_milisec = time_2
    computer_thought_time = time_1 
    
human_thought_time_in_seconds = human_thought_time_in_milisec / MILI

human_thought_time_hours = int (human_thought_time_in_seconds / SECONDS_IN_AN_HOUR)
human_thought_time_minutes = int((human_thought_time_in_seconds - (human_thought_time_hours * SECONDS_IN_AN_HOUR))/SECONDS_IN_A_MINUTE) 
human_thought_time_seconds = round(human_thought_time_in_seconds - (human_thought_time_hours * SECONDS_IN_AN_HOUR) - (human_thought_time_minutes * SECONDS_IN_A_MINUTE))

#output
print 'The time the human player has spent thinking is %d:%d:%d' %(human_thought_time_hours, human_thought_time_minutes, human_thought_time_seconds)