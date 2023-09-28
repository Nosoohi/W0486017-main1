#first program , showing the use of print , variable , operators 
#and datatype

print("hello")

#Declaring a variable
pricecoffee = 3.99
# gather input from user , indicating how many cuos they want to buy 
numberofcup = input("How many cups of coffee would you like today ?")
#we need number of coffee so we have to use (int) to inform our program we mean the number of coffee so whta ever the user put in our machin it will work
taxamount = int (numberofcup) * pricecoffee * 0.15
Finaltottal = pricecoffee * int(numberofcup) + taxamount
print(taxamount)
print(Finaltottal)
msg = "your final tottal is "
print( msg + str(Finaltottal))

#second coffee shop ex
tax=1,23
toatal=8.9
grandtotal=toatal+tax
myphrase="your final total is ${0:..2f}"