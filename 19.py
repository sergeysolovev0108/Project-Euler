"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

months = {"Jan": 31,
          "Feb": 28,
          "Mar": 31,
          "Apr": 30,
          "May": 31,
          "Jun": 30,
          "Jul": 31,
          "Aug": 31,
          "Sep": 30,
          "Oct": 31,
          "Nov": 30,
          "Dec": 31}


def counting_of_sundays():
    day = 365  # days after 1 Jan 1900 year
    sunday_count = 0
    for year in range(1901, 2001):
        for x in months:
            day += 1
            if day % 7 == 0:
                sunday_count += 1
                '''Show all sundays on the first of the month'''
                print(x, year,  '№', sunday_count, day)
            day += months[x] - 1
            if year % 4 == 0 and x == "Feb":
                """show leap year"""
                # print(year, 'Leap year')
                day += 1

    print("Sundays:", sunday_count)


if __name__ == "__main__":
    counting_of_sundays()
