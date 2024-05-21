#1741. Find Total Time Spent by Each Employee
#Long way
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    dictionary= {}
    for i in range (len(employees)):
        emp_id = employees['emp_id'][i]
        day = employees['event_day'][i]
        in_time = employees['in_time'][i]
        out_time = employees['out_time'][i]
        if(day, emp_id) in dictionary:
            dictionary[(day,emp_id)] += out_time - in_time
        else:
            dictionary[(day,emp_id)] = out_time - in_time
    result = []
    for (day, emp_id), total_time in dictionary.items():
        result.append([day, emp_id, total_time])

    return pd.DataFrame(result, columns=['day', 'emp_id', 'total_time'])


# #Another way
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day','emp_id']) ['total_time'].sum().reset_index()
    employees.rename({'event_day': 'day'}, axis =1, inplace = True)
    return employees


#511. Game Play Analysis I
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range(len(activity)):
        p_id = activity['player_id'][i]
        e_date = activity['event_date'][i]
        if p_id in mydictionary:
            if e_date < mydictionary[p_id]:
                mydictionary[p_id] = e_date
        else:
            mydictionary[p_id] = e_date
    
    result = []
    for key, value in mydictionary.items():
        result.append([key, value])
    
    return pd.DataFrame(result, columns=['player_id', 'first_login'])

#Efficient way
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(['player_id']) ['event_date'].min().reset_index()
    return df.rename(columns = {'event_date': 'first_login'})


import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by=['event_date']).drop_duplicates(['player_id'])
    return df[['player_id', 'event_date']].rename(columns = {'event_date':'first_login'})

