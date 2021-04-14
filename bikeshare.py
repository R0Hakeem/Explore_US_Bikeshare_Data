import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Which City would you like to filter by (Chicago, New york city or Washington)?").lower()

    while city not in(CITY_DATA.keys()):
        print("Enter a valid city")
        city = input("Which City would you like to filter by (Chicago, New york city or Washington)?").lower()

    filter_by = input('Would you like to filter the data by month, day, both, or none? ').lower()
    while filter_by not in(['month', 'day', 'both', 'none']):
        print('Enter a valid filter')
        filter_by = input('Would you like to filter the data by month, day, both, or none? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter_by == 'month' or filter_by == 'both':
        month = input("Which month would you like to filter by (january, ... june)?").lower()
        while month not in months:
            print("Enter a valid month")
            month = input("Which month would you like to filter by (january, ... june)?").lower()
    else:
        month = 'all'





    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if filter_by == 'day' or filter_by == 'both':
        day = input("Which day would you like to filter by (sunday, ... saturday)?").title()
        while day not in days:
            print("Enter a valid day")
            day = input("Which day would you like to filter by (sunday, ... saturday)?").title()
    else:
        day = 'all'


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

    #Loading the data
    df = pd.read_csv(CITY_DATA[city])

    #Extracting month, day, hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter data by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    #filter data by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is:", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of week is:", popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common start station is:", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common end station is:", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_trip = df.groupby(['Start Station','End Station'])
    popular_trip = group_trip.size().sort_values(ascending=False).head(1)
    print("The most frequent combination of start station and end station trip is:", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_users = df['User Type'].value_counts()
    print("The counts of user types are:", counts_users)


    # TO DO: Display counts of gender
    #if city != 'washington':
    if 'Gender' in(df.columns):
        counts_gender = df['Gender'].value_counts()
        print("The counts of gender are:", counts_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        earliest_year = df['Birth Year'].min()
        print("The earliest year of birth is:", earliest_year)

        recent_year = df['Birth Year'].max()
        print("The most recent year of birth is:", recent_year)

        popular_year = df['Birth Year'].mode()[0]
        print("The most common year of birth is:", popular_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #Display 5 lines of raw data upon request by the user
def display_raw_data(df):
    raw_data = input('\nwould you like to display 5 lines of raw data? (Y/N)\n').lower()
    if raw_data in ['y','Y','yes','yeah','yup','yea']:
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            more_raw_data = input('\nwould you like to display more 5 lines of raw data? (Y/N)\n').lower()
            if more_raw_data not in ['y','Y','yes','yeah','yup','yea']:
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
