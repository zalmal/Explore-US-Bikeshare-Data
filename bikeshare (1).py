import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city=input('Would you like to see data for Chicago, New York, or Washington? ' ).lower()
    while city !='chicago' and city !='new york' and city != 'washington':
        print(city,'not a valid answer.Please enter Chicago, New York, or Washington')
        city=input('Would you like to see data for Chicago, New York, or Washington? ' ).lower()


    Filter= input('Would you like to filter the data by month, day,both or not at all? ')
    while Filter!='month' and Filter !='day' and Filter !='not at all' and Filter != 'both':
        print(Filter,'not a valid please enter {month}, {day},{both} or {not at all}.') 
        Filter= input('Would you like to filter the data by month, day,both or not at all? ')
    # get user input for month (all, january, february, ... , june)
    if Filter =='month':
        month=input('Which month - January, February, March, April, May, or June?').lower()
        day = 'all'
        while month!='january' and month!='february' and month!='march' and month!='april' and month!='may' and month!= 'june':
            print(month,'not valid plese enter January, February, March, April, May, or June')
            month=input('Which month - January, February, March, April, May, or June?').lower()
            

    if Filter =='day':
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').title()
        month = 'all'
        while day!='Monday' and day!='Tuesday' and day!='Wednesday' and day!='Thursday' and day!='Friday' and day!='Saturday' and day!='Sunday':
            print(day,'not valid answer plese enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')
            day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').title()
    
    if Filter =='not at all':
        month = 'all'
        day = 'all'
    if Filter == 'both':
        month=input('Which month - January, February, March, April, May, or June?').lower()
        while month!='january' and month!='february' and month!='march' and month!='april' and month!='may' and month!= 'june':
            print(month,'not valid plese enter January, February, March, April, May, or June')
            month=input('Which month - January, February, March, April, May, or June?').lower()
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').title()
        while day!='Monday' and day!='Tuesday' and day!='Wednesday' and day!='Thursday' and day!='Friday' and day!='Saturday' and day!='Sunday':
            print(day,'not valid answer plese enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')
            day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').title()
            
        
    
    print('-'*40)
    return city, month, day# TO DO: get user input for city (chicago, new york city, washington). HINT: Use 


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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month']==month] 
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframePl
        df = df[df['day_of_week'] ==day.title()]

    return df





def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    

    print('the most common month(s):\n',df['month'].mode(),'\n')# display the most common month


    print('the most common day(s) of week:\n',df['day_of_week'].mode(),'\n')
    df['hour'] = df['Start Time'].dt.hour# display the most common day of week


    print('the most common Start Hour(s):\n',df['hour'].mode(),'\n')# display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total Travel Time:',df['Trip Duration'].sum(),'seconds')# display total travel time


    print('Mean Travel Time:',df['Trip Duration'].mean(),'seconds')# display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most commonly used start station(s):\n',df['Start Station'].mode().to_string(index=False),'\n')# display most commonly used start station


    print('The most commonly used end station(s):\n',df['End Station'].mode().to_string(index=False),'\n')# display most commonly used end station


    df['rout']=df['Start Station']+'--'+df['End Station']
    print('The most frequent combination(s) of start station and end station trip:\n',df['rout'].mode().to_string(index=False),'\n')# display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('Counts of user types: \n',df['User Type'].value_counts(),'\n')# Display counts of user types


    try:
       print('Counts of gender: \n',df['Gender'].value_counts(),'\n')
    except:
        print('sorry! Washington datset has no user gender information') # Display counts of gender


    try:
        print('Earliest year of birth: ',df['Birth Year'].min())
        print('Most recent year of birth: ',df['Birth Year'].max())
        print('Most common year of birth: ',df['Birth Year'].mode())
    except:
        print('sorry! Washington datset has no user year of birth')# Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart !='yes' and restart !='no':
            print('please type in yes or no')
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
