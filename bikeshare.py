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
    city = None
    month = None
    day = None

    city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
    while city not in ('chicago','new york','washington'):
        city = input('Please type in the right city!!!(chicago, new york, washington)').lower()
    print('Great! We will prepare {}\'s data for you!'.format(city.title())+'\n')
    if city == 'new york': city = 'new york city'

    data_filter = input('Would you like to filter the data by Month or Day or Both or None?').lower()
    while data_filter not in ('month', 'day', 'both','none'):
        data_filter = input('Please type the right filter! Month or Day or Both or None?').lower()
    print('We will make sure to filter by {}!'.format(data_filter.title())+'\n')
    if data_filter == 'none':
        month = 'all'
        day = 'all'
    # TO DO: get user input for month (all, january, february, ... , june)
    if data_filter  == 'month':
        day = 'all'
        month = input('Which month - January, February, March, April, May,June?').lower()
        while month not in ('january','february','march','april','may','june'):
            month = input('Please type in the right month!').lower()
        print('Just one moment...Loading the data'+'\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    if data_filter  == 'day':
        month = 'all'
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        while day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            day = input('Please type the right day!').lower()
        
        print('Just one moment...Loading the data'+'\n')
    if data_filter  == 'both':
        month = input('Which month - January, February, March, April, May, or June?').lower()
        while month not in ('january','february','march','april','may','june'):
            month = input('Please type in the right month!').lower()
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        while day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            day = input('Please type the right day!').lower()
        
        print('Just one moment...Loading the data'+'\n')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month: {}'.format(popular_month))
    print()
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week: {}'.format(popular_day_of_week))
    print()
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular hour: {}'.format(popular_hour))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_str_st = df['Start Station'].mode()[0]
    print('Most Popular Start Station: {}'.format(pop_str_st))
    print()

    # TO DO: display most commonly used end station
    pop_end_st = df['End Station'].mode()[0]
    print('Most Popular End Station: {}'.format(pop_end_st))
    print()

    # TO DO: display most frequent combination of start station and end station trip
    df['both station'] = 'Start Station: '+df['Start Station']+' , End Station: '+df['End Station']
    pop_both_st = df['both station'].mode()[0]
    print('Most Popular Start & End Station: {}'.format(pop_both_st))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_trip = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(sum_trip))
    print()
    # TO DO: display mean travel time
    avg_trip = df['Trip Duration'].mean()
    print('Average Travel time: {}'.format(avg_trip))
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type:\nSubscriber: {}'.format(user_types[0]))
    print('Customer: {}'.format(user_types[1]))
    print()

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('Gender:\nMale: {}'.format(gender[0]))
    print('Female: {}'.format(gender[1]))
    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    min_year = df['Birth Year'].min()
    max_year = df['Birth Year'].max()
    com_year = df['Birth Year'].mode()[0]
    print('The Earliest Birth Year: {}'.format(min_year))
    print('The Most Recent Birth Year: {}'.format(max_year))
    print('The Most Common Birth Year: {}'.format(com_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        want_more = input('\nWould you like to read more date result?\n \'no\' to exit!')
        if want_more.lower() == 'no':
            break

        station_stats(df)
        want_more = input('\nWould you like to read more date result?\n')
        if want_more.lower() == 'no':
            break

        trip_duration_stats(df)
        want_more = input('\nWould you like to read more date result?\n')
        if want_more.lower() == 'no':
            break
        
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
