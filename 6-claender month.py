import calendar

def desplay_clander():
    year = int(input("Enter year: "))
    month = int(input("Enter the month:"))
    clender = calendar.TextCalendar(calendar.TUESDAY)
    month_calner = clender.formatmonth(year, month)
    print(month_calner)

desplay_clander()
