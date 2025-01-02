from datetime import date, timedelta
# start on a Monday
trueInitialDate = date(2024,12,23)

initialDate = trueInitialDate
print("PR Start Date,PR End Date,Monday,Check Date")
while (initialDate.year < 2026):
    # Start Date is a Monday, End Date is the Sunday 13 days later, Monday is the last day for timesheet changes, Check date is the following Friday
    startDate = initialDate
    endDate = initialDate + timedelta(days=13)
    mondayDate = endDate + timedelta(days=1)
    checkDate = mondayDate + timedelta(days=4)
    print(startDate.strftime("%m/%d/%Y") + "," + endDate.strftime("%m/%d/%Y") + ","
          + mondayDate.strftime("%m/%d/%Y") + "," + checkDate.strftime("%m/%d/%Y"))
    # add 14 days to start again
    initialDate += timedelta(days=14)