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


#2356. Number of Unique Subjects Taught by Each Teacher
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range(len(teacher)):
        t_id = teacher['teacher_id'][i]
        sub_id = teacher['subject_id'][i]
        if t_id not in mydictionary:
            mydictionary[t_id] = set()  # Key as teacher_id and value as empty set
        mydictionary[t_id].add(sub_id)
    
    result = []
    for key, value in mydictionary.items():
        result.append([key, len(value)])
    
    return pd.DataFrame(result, columns=['teacher_id', 'cnt'])

#Alternative
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(['teacher_id']) ['subject_id'].nunique().reset_index()
    return df.rename(columns = {'subject_id':'cnt'})


#596. Classes More Than 5 Students
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    mydictionary = {}
    for i in range (len(courses)):
        subject = courses['class'][i]
        if subject not in mydictionary:
            mydictionary[subject] = 0
        mydictionary[subject] += 1
    result = []
    for key,value in mydictionary.items():
        if value >= 5:
            result.append([key])
    return pd.DataFrame(result, columns = ['class'])


#Short sol
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(['class']).size().reset_index(name = 'count')
    df = df[df['count'] >= 5]
    return df[['class']]

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(['class'])['student'].nunique().reset_index(name = 'count')
    df = df[df['count'] >= 5]
    return df[['class']]

#Instead of nunique , we can use count()
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(['class']).nunique().reset_index()
    df = df[df['student'] >= 5]
    return df[['class']]

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(['class']).count().reset_index()
    df = df[df['student'] >= 5]
    return df[['class']]


