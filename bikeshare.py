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
    city = ""
    while city not in ("chicago", "new york city", "washington"):
        city = input("Please choose a city from Chicago, New York City or Washington:").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in ("january", "february", "march", "april", "may", "june", "all"):
        month = input("If you would like to filter the data by month, please type a month between January and June (inclusive). If not, please type 'all'.:").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"):
        day = input("If you would like to filter the data by day, please type a day of the week (Monday, Tuesday, etc.).  If not, please type 'all.':").title()

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
    # Load the correct csv based on user selected city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns for the month and day of the week from the new 'Start Time' column
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    # filter by month if needed
    if month != 'all':
        # use the index from this list to get the integer value of the month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month
        df = df[df['Month'] == month]

    # filter by day of week if needed
    if day != 'All':
        df = df[df['Day of Week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month = months[int(df.mode()['Month'][0]) - 1]
    print("The month where the most rides started was: {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df.mode()['Day of Week'][0]
    print("The day of the week where the most rides started was: {}".format(most_common_day))

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_common_start_hour = int(df.mode()['Start Hour'][0])
    print("The hour that most rides started was: {}".format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df.mode()['Start Station'][0]
    print("The most common station users started thier trip from was: {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df.mode()['End Station'][0]
    print("The most common station users ended their trip with was: {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start Station - End Station'] = df['Start Station'] + " - " + df['End Station']
    most_common_trip = df.mode()['Start Station - End Station'][0]
    print("The most common trip occured between this start and end station: {}".format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60 / 60 /24
    print("The total time (in days) of all trips was: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean()) / 60
    print("The average time (in min) of all trips was: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_breakdown = df['User Type'].value_counts()
        print("Here is the breakdown of Users:\n {}".format(user_breakdown))
    except KeyError:
        print("This data does not contain user type data.  Skipping calculation...\n")

    # TO DO: Display counts of gender
    try:
        gender_breakdown = df['Gender'].value_counts()
        print("Here is the breakdown of Gender:\n {}".format(gender_breakdown))
    except:
        print("This data does not contain gender data.  Skipping calculation...")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()

        print("The oldest user was born in: {}".format(int(min_birth_year)))
        print("The youngest user was born in: {}".format(int(max_birth_year)))
        print("The most common birth year was: {}".format(int(most_common_birth_year)))
    except KeyError:
        print("This data does not contain birth year data.  Skipping calculation...")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(data):
    i = 0
    while True:
        see_data = input("Would you like to see 5 rows of raw data?(yes or no):").lower()
        if see_data != "yes":
            break
        else:
            print(data[i:i+5])
            i += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
