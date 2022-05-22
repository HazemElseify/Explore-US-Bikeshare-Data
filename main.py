import time
import pandas as pd
import numpy as np
import math
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
RealCityName = {'chicago': 1, 'washington': 1, 'new york': 1}
RealmonthName = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
                 9: 9, 10: 10, 11: 11, 12: 12}
RealdayName = {1:6, 2:0, 3:1, 4:2, 5:3, 6:4, 7:5}

def get_filters():
    """
   Asks user to specify a city, month, and day to analyze.

   Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
   """
    global city
    global month
    global day
    global res
    global res2
    global filter
    global Gcity
    city=''
    month=0
    day=0
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
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
            if(filterOption=='month'):
                day=0
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
            if(filterOption=='day'):
                month=0
            day = input("please enter the day number  from [1 to 7]\n")
            while (True and flag == 0):
                day = int(day)
                if (RealdayName.get(day) != None):
                    flag = 1
                    break
                else:
                    print("sorry you entered wrong day...please enter the day number  from [1 to 7]")
                    day = input()
        if (filterOption == 'none'):
            month=0
            day=0
            break
        if(filterOption!='day' and filterOption!='month' and filterOption!='both' and filterOption!='none'):
            print(
                "You entered wrong filter...choose to filter by [month,day,both] or not choose filter at all [none]\n")
            filterOption = input()
        if (flag == 1):
            break
    filter=filterOption
    Gcity=city
    month=int(month)
    day=int(day)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    global FlagMonth
    global FlagDay
    global FlagNone
    FlagDay = 0
    FlagMonth = 0
    FlagNone = 0
    df=pd.read_csv(CITY_DATA[city])
    df.rename(columns={"Unnamed: 0": "a"}, inplace=True)
    df.pop('a')
    if(Gcity!='washington'):
        df = df.dropna(subset=['Gender', 'Birth Year'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['WeekDay'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour
    df['SE Station'] = df['Start Station'] + ' and ' + df['End Station']
    #print("Month = ",month,type(month))
    if(month>0 and day>0):
        #print(RealdayName.get(day))
        #print(type(RealdayName.get(day)))
        df=df[(df['Month']==month) & (df['WeekDay']==RealdayName.get(day))]
        #df=df.loc[(df["Month"]==month)&(df['WeekDay']==RealdayName.get(day))]
        #print(df.head())
        FlagMonth=1
        FlagDay=1
    elif(month>0):
        df=df[(df['Month']==month)]
        FlagMonth=1
    elif(day>0):
        df = df[(df['WeekDay']==RealdayName.get(day))]
        FlagDay = 1
    if(month==0 and day==0):
        FlagNone=1

    #print("\n",month,day,city,"\n")
    return df


def time_stats(df):
    disday= {5:'Thursday', 6:'Friday', 3:'Tuesday', 2:'Monday', 4:'Wednesday', 7:'Saturday', 1:'Sunday'}
    dismonth = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                     5: 'May', 6: 'June', 7: 'July', 8: 'August',
                     9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('filter: {}\n'.format(filter))
    start_time = time.time()
    #print(FlagDay,FlagMonth,FlagNone)
    # display the most common month
    flag=0
    if(FlagNone==1 or(FlagDay==1 and FlagMonth==0)):
        if(df.empty):
            flag=1
        else:
            res = df.mode()
            res = int(res.iloc[0]['Month'])
            print('most common Month: {}'.format(dismonth.get(res)))

    # display the most common day of week
    if (FlagNone == 1 or (FlagDay == 0 and FlagMonth == 1)):
        if(df.empty):
            flag=1
        else:
            res = df.mode()
            res = str(res.iloc[0]['WeekDay'])
            print('most common day: {}'.format(disday.get(int(float(res)))))

    # display the most common start hour
    if(df.empty):
        flag=1
    else:
        res = df.mode()
        res = int(res.iloc[0]['Hour'])
        print('most common hour: {}'.format(res))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return flag
def station_stats(df):
    flag=1
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('filter: {}\n'.format(filter))
    start_time = time.time()

    # display most commonly used start station
    if (df.empty):
        flag = 1
    else:
        res = df.mode()  # both
        res = str(res.iloc[0]['Start Station'])
        print('most common Start Station: {}'.format(res))

    # display most commonly used end station
    if (df.empty):
        flag = 1
    else:
        res = df.mode()  # both
        res = str(res.iloc[0]['End Station'])
        print('most common End Station: {}'.format(res))
        # display most frequent combination of start station and end station trip
        res = df.mode()  # both
        res2 = df.count()
        res = str(res.iloc[0]['SE Station'])
        res2 = int(res2.iloc[0])
        print('most common End most common trip from start to end: {} and counts {}'.format(res, res2))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return flag

def trip_duration_stats(df):
    flag=0
    global res
    global res2
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    print('filter: {}\n'.format(filter))
    start_time = time.time()
    if (df.empty):
        flag = 1
    else:
    # display total travel time
        res = df.loc[:,['Trip Duration']].sum()  # both
        res2 = df.loc[:,['Trip Duration']].count()
        res = str(res.iloc[0])
        res2 = str(res2.iloc[0])
        print('Total Travel time in sec: {} and counts {}'.format(res, res2))
    if (df.empty):
        flag = 1
    else:
    # display mean travel time
        res = int(float(res))
        res2 = int(res2)
        res = df.loc[:,['Trip Duration']].mean()  # both
        res2 = df.loc[:,['Trip Duration']].count()
        res = str(res.iloc[0])
        res2 = str(res2.iloc[0])
        print('Total Travel time in sec: {} and counts {}'.format(res, res2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return flag


def user_stats(df):
    flag=0
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    print('filter: {}\n'.format(filter))
    start_time = time.time()
    # Display counts of user types
    if (df.empty):
        flag = 1
    else:
        res = df.loc[:,['User Type']].value_counts()  # both
        # res=str(res.iloc[0])
        print('Type of Users: {}'.format(res))
    if (Gcity != 'washington'):
        # Display counts of gender
        if (df.empty):
            flag = 1
        else:
            res = df.loc[:,['Gender']].value_counts()  # both
            # res=str(res.iloc[0])
            print('User\'s Gender: {}'.format(res))
            # Display earliest, most recent, and most common year of birth
            resMin = df.loc[:,['Birth Year']].min()  # both
            resMax = df.loc[:,['Birth Year']].max()  # both
            res = df.loc[:,['Birth Year']].mode()  # both
            res2 = df.loc[:,['Birth Year']].count()
            resMin = resMin.iloc[0]
            resMax = resMax.iloc[0]
            res = res.iloc[0]['Birth Year']
            res2 = res2.iloc[0]
            print('earliest Year: {} , most recent year: {} , most common year: {} and counts {}'.format(resMin, resMax, res,res2))
            print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return flag

def main():
    while True:
        f1=0
        f2=0
        f3=0
        f4=0
        fshow=0
        f=0
        city, month, day = get_filters()
        #print(city,month,day)
        #month=int(month)
        #day=int(day)
        #print(type(month), type(day))
        df = load_data(city, month, day)
        fshow=Showdata(df)
        f1=time_stats(df)
        f2=station_stats(df)
        f3=trip_duration_stats(df)
        f4=user_stats(df)
        f=f1|f2|f3|f4
        if(f):
            print('there is no data to analyse try another filter \'Your Data is Empty\'')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
