#python program to convert temperature between fahrenheit and celsius
#take value of temperature from user in celsius
celsius = input("Enter value of temperature in celsius: ")
#formula to convert celsius to fahrenheit
fahrenheit = float(celsius) * 1.8 + 32 
print("The value of temperature in fahrenheit is : ")
print(fahrenheit)
#take value of temperature from user in fahrenheit
fahrenheit = input("Enter value of temperature in fahrenheit: ")
#formula to convert fahrenheit to celsius 
celsius =  (float(fahrenheit) - 32 ) / 1.8
print("The value of temperature in celsius is : ")
print(celsius)
