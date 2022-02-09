#Sameerah Mustafa
#1584330

service1_cost = 0
service2_cost = 0
# Output a menu of automotive services
# and the corresponding cost of each service.
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
# Prompt the user for two services from the menu.
service1 = input('Select first service:\n')
service2 = input("Select second service:")

print('\n')
print("Davy's auto shop invoice")
print('')

dic = {"Oil change": "35", "Tire rotation": "19", "Car wash": "7", "Car wax": "12"}
total = 0

if service1 == "Oil change":
    service1_cost = 35

elif service1 == "Tire rotation":
    service1_cost = 19

elif service1 == "Car wash":
    service1_cost = 7

elif service1 == "Car wax":
    service1_cost = 12

elif service1 == "-":
    service1 = "No service"

if service2 == "Oil change":
    service2_cost = 35

elif service2 == "Tire rotation":
    service2_cost = 19

elif service2 == "Car wash":
    service2_cost = 7

elif service2 == "Car wax":
    service2_cost = 12

elif service2 == "-":
    service2 = "No service"


print("Service 1: " + service1 + ', ' + '$' + str(service1_cost))

print("Service 2: " + service2 + ', ' + '$' + str(service2_cost))
print()
print("Total: $" + str(service1_cost + service2_cost))