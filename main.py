# Employee_schedule_generator
import random

employee_list = ['Diego','Gabi','Letycia','Stella','Kobe','Sugar','Raymond','Americo']
days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
schedule = {}
shifts = ['7-3','9-5','10-3.1','10-3.2','11-7','3-9','5-9.1','5-9.2']

if len(employee_list) >= len(shifts):
    for day in days_of_week:
        day_schedule = {}
        employee_list_copy = employee_list[:]
        for shift in shifts:
            empl_list_pos = random.randint(0, len(employee_list_copy) - 1)
            day_schedule[shift] = employee_list_copy[empl_list_pos]
            del employee_list_copy[empl_list_pos]
        schedule[day] = day_schedule
    for day in schedule:
        print(day,schedule[day])
else:
    print('not enough employees')