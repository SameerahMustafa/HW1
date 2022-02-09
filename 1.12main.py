#Sameerah Mustafa
#1584330


userNum=int(input())
#here + symbol was used, for getting square of a number
#it should be multiplied with itself, not added
#hence + symbol is replaced with *
userNumSquared=userNum*userNum
#here the end is given as end=''
#so if userNumSquared is printed again
#it will be on the same line of the previous output
#so if userNumSquared is printed twice
#output will be 2525
#which is inconvenient, so end='\n'
#is better, which prints the output on next line
print(userNumSquared,end='\n')