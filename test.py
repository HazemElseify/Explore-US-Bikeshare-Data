import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


global s
s=0
print(s)
def get_filters():
    global city
    global month
    global day
    """
   Asks user to specify a city, month, and day to analyze.

   Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
   """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    RealCityName = {'chicago': 1, 'washington': 1, 'new york': 1}
    RealmonthName = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                     9: '9', 10: '10', 11: '11', 12: '12'}
    RealdayName={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7'}
    city = input("Please Enter the city...i.e(chicago,washington or new york)\n")
    while (True):
        city = city.lower()
        if (RealCityName.get(city) != None):
            break
        else:
            print("sorry you entered wrong city...Please Enter the city...i.e(chicago,washington or new york) ")
            city = input()
    # get user input for month (all, january, february, ... , june)
    filterOption = input('choose to filter by [month,day,both] or not choose filter at all [none]\n')
    while (True):
        flag = 0
        filterOption = filterOption.lower()
        if (filterOption == 'month' or filterOption == 'both'):
            month = input("please enter the month number  from [1 to 12]\n")
            while (True and flag == 0):
                month = int(month)
                if (RealmonthName.get(month) != None):
                    flag = 1
                    break
                else:
                    print("sorry you entered wrong city...please enter the month number  from [1 to 12]")
                    month = input()
        if (filterOption == 'day' or filterOption == 'both'):
            day = input("please enter the day number  from [1 to 7]\n")
            while (True and flag == 0):
                print(flag)
                day = int(day)
                print(month, type(day))
                if (RealdayName.get(day) != None):
                    flag = 1
                    break
                else:
                    print("sorry you entered wrong day...please enter the day number  from [1 to 7]")
                    day = input()
        if (filterOption == 'none'):
            break
        if(filterOption!='day' and filterOption!='month' and filterOption!='both' and filterOption!='none'):
            print(
                "You entered wrong filter...choose to filter by [month,day,both] or not choose filter at all [none]\n")
            filterOption = input()
        if (flag == 1):
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)
    return  city, month, day
city=''
month=''
day=''
city,month,day=get_filters()
print(city,month,day)