# firstword = "Bazooka"
#  secondword = "kitty"
 #example 1: manual contact with the + operator
#  print(firstword + secondword)

# #multiple argument for the print () command
# print("hello" , " geoff" , "you" , )
 # for comment all the line at the same time do (ctrl and /) at the same time 
 # becuse we dont want to have lots of number in our last out come we will use round command so it is gonna round it to 7
 #  but its not specific yet so we will add another number to say after our main number to say we want to round out from the second number after 7
initialnumber= 7.36
tottal =  round(initialnumber,2)
# we cant add the value of tottal without str because 
# we cant add a word and number toghter do by saying str we are saying to camputer print the value of tottal
print("your final tattal is " + str(tottal))
#string command 
# so the {0} is a palce holder for every thing that we give in the .format commmand and the :.2f will say to the computer 
#that we need to number after 7 in our price at the outcome and also we can chnage that .2f depend on how many numebr we want after that 7 like .4f 
#
myphrase = "your final tottal is {0:.2f}"
print(myphrase.format(tottal))