#program description and requirment
# Write a program that allows the user to enter the number of hours they worked this week and the dollar amount they make per hour. 
# ■Use these values to calculate the amount of money they made this week. 
# ■If the # of hours exceeds 40 in a week, include the amount of overtime pay they made in the total. 
# ■Overtime pays time-and-a-half (1.5X) the usual hourly wage, and only apply to the # of hours worked over 40. 

# set up the variable (normal weekly work hour)
normweekwork = 40

#set up the inputs to get the hours they worked and the their hourly inocme  
worktime = float(input("Enter the number of hours you have worked in a week: "))
payment = float(input("Enter your hourly income in dollar: "))

# if statement calculates if the worker , has worked 40 hours or less (normal work week)
if worktime <= normweekwork:
  weekincome= worktime * payment
  print("you have worked {0} hours for {1} dollars/hour and your weekly wage is {2}".format(worktime , payment , weekincome))

#if statement calculates if the worker , has worked more than 40 hours/week with the extra calculations for the hours above 40 (1.5 x normal payments) and print the total
else :
  overpay = worktime - normweekwork
  extrapay = overpay * (1.5 * payment)
  totalpayment = extrapay + (normweekwork * payment)
  print("you have worked more than 40 hours({0} hours) for {1} dollars/hour and extra 1.5x payment for {2} hours ,  your weekly wage is {3}" .format(worktime , payment , overpay ,totalpayment))


  