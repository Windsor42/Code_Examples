import datetime

def get_user_donsas():
    user_input = input("Do you want to add any upcoming donsas (y/n)?: ")
    donsas = []
    if user_input.lower() == 'y':
        donsa_count = int(input("How many donsas do you want to add?: "))
        for i in range(donsa_count):
            donsa_str = input(f"Enter donsa {i + 1} in the format 'YYYY-MM-DD': ")
            donsa = datetime.datetime.strptime(donsa_str, '%Y-%m-%d').date()
            donsas.append(donsa)
    return donsas

def get_training_days(start_date, end_date, holidays, weekends, donsas):
    delta = end_date - start_date
    training_days = []
    for i in range(delta.days + 1):
        day = start_date + datetime.timedelta(days=i)
        if day.weekday() >= 5:  # weekdays are from 0 (Monday) to 4 (Friday)
            continue
        if day in holidays or day in donsas:
            continue
        if weekends and day.weekday() in [5, 6]:
            continue
        training_days.append(day)
    return len(training_days)

if __name__ == '__main__':
    start_date_str = input("Enter the start date in the format 'YYYY-MM-DD': ")
    end_date_str = input("Enter the end date in the format 'YYYY-MM-DD': ")
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    holidays = [
    # Fixed holidays
    datetime.date(2023, 1, 1), # New Year's Day
    datetime.date(2023, 7, 4), # Independence Day
    datetime.date(2023, 12, 25), # Christmas Day
    datetime.date(2024, 1, 1), # New Year's Day
    datetime.date(2024, 7, 4), # Independence Day
    datetime.date(2024, 12, 25), # Christmas Day
    datetime.date(2025, 1, 1), # New Year's Day
    datetime.date(2025, 7, 4), # Independence Day
    datetime.date(2025, 12, 25), # Christmas Day
    datetime.date(2026, 1, 1), # New Year's Day
    datetime.date(2026, 7, 4), # Independence Day
    datetime.date(2026, 12, 25), # Christmas Day
    datetime.date(2027, 1, 1), # New Year's Day
    datetime.date(2027, 7, 4), # Independence Day
    datetime.date(2027, 12, 25), # Christmas Day
    # Variable holidays
    datetime.date(2023, 1, 2), # New Year's Day (observed)
    datetime.date(2023, 1, 16), # Martin Luther King Jr. Day
    datetime.date(2023, 2, 20), # Presidents' Day
    datetime.date(2023, 5, 29), # Memorial Day
    datetime.date(2023, 7, 4), # Independence Day (observed)
    datetime.date(2023, 9, 4), # Labor Day
    datetime.date(2023, 10, 9), # Columbus Day
    datetime.date(2023, 11, 11), # Veterans Day
    datetime.date(2023, 11, 23), # Thanksgiving Day
    datetime.date(2023, 12, 25), # Christmas Day (observed)
    datetime.date(2024, 1, 2), # New Year's Day (observed)
    datetime.date(2024, 1, 15), # Martin Luther King Jr. Day
    datetime.date(2024, 2, 19), # Presidents' Day
    datetime.date(2024, 5, 27), # Memorial Day
    datetime.date(2024, 7, 4), # Independence Day (observed)
    datetime.date(2024, 9, 2), # Labor Day
    datetime.date(2024, 10, 14), # Columbus Day
    datetime.date(2024, 11, 11), # Veterans Day
    datetime.date(2024, 11, 28), # Thanksgiving Day
    datetime.date(2024, 12, 25), # Christmas Day (observed)
    datetime.date(2025, 1, 2), # New Year's Day (observed)
    datetime.date(2025, 1, 20), # Martin Luther King Jr. Day
    datetime.date(2025, 2, 17), # Presidents' Day]

    # if you need to add more holidays or permanently include a DONSA simply copy the above format in the blank space above
    # make sure the indenting stays consistant!
    ]
    
    weekends = True
    donsas = get_user_donsas()
    num_training_days = get_training_days(start_date, end_date, holidays, weekends, donsas)
    print(f"Number of training days: {num_training_days}")
