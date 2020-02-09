date = 'AB.AB.BABA'
day_number = 2
month_number = 2
year_number = 2020
month_amount_of_days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31,
                        'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
month_counter = month_number - 1
number_of_mirror_dates = 0

while year_number < 12020:
    current_month_str = list(month_amount_of_days.keys())[month_counter]
    day_number += 1
    if ((year_number % 4 == 0) and (year_number % 100 != 0)) or (year_number % 400 == 0):
        month_amount_of_days['Feb'] = 29
    else:
        month_amount_of_days['Feb'] = 28

    if day_number > month_amount_of_days[current_month_str]:
        day_number = 1
        month_number += 1
        month_counter += 1

    if month_number > len(month_amount_of_days):
        month_number = 1
        month_counter = 0
        year_number += 1

    day_number_str = f'{day_number}'
    month_number_str = f'{month_number}'
    year_number_str = f'{year_number}'
    if len(day_number_str) == 1:
        day_number_str = '0' + day_number_str
    if len(month_number_str) == 1:
        month_number_str = '0' + month_number_str

    if (day_number_str == month_number_str) and (day_number_str*2 == year_number_str[::-1]):
        print(f'{day_number_str}.{month_number_str}.{year_number_str}')
        number_of_mirror_dates += 1

print(f'The number of mirror dates till 12020 year: {number_of_mirror_dates}')


