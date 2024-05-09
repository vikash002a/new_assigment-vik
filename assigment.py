#1
def  print_messge(number):
    if number % 3 == 0 and number % 5 == 0:
       prdint("Brudite- python training")
    elif number % 3 == 0:
       print("Brudite")
    elif number % 5 == 0:
       print("Python Training")
    else:
        print(number)
        
# #2
char = input()
print(char)

dcount = 0
count = 0
for i in char:
    if i.isdigit():
        dcount = dcount + 1
    if i.isalpha():
        count = count +1
        
print(f"totalnumber: {dcount}")
print(f"totalalpha: {count}")    
        
a = int(input("enter the number"))
for i in range(1, 10):
    print_messge(i)
    
    
# # 3
physics = int(input("Enter the physics marks:"))
chemistry = int(input("Enter the chemistry marks:"))
biology = int(input("Enter the biology marks:"))
mathematics = int(input("Enter the mathematics marks:"))
computer = int(input("Enter the computer marks:"))

Totalmarks = physics+chemistry+biology+mathematics+computer
percantage = (Totalmarks/500)*100


if percantage >= 90:
   Grade = "A"
elif percantage >= 80:
   Grade = "B"
elif percantage >= 70:
   Grade = "C"
elif percantage >= 60:
   Grade = "D"
elif percantage >= 40:
   Grade = "E"
else:
    Grade = "F"
      
print(f"percantage: {percantage}%")
print(f"Grade: {Grade}")      

# #4
def sum_of_odd_numbers(start, stop):
   total = 0
   for num in range(start, stop+1):
      if num % 2 != 0:
         total += num
   return total
start = 1
stop = 10

result = sum_of_odd_numbers(start, stop)
print("sum of odd numbers between", start, "and", stop, "is", result)

# #5
def perfectnumber(num):
    total_number = 0
    for i in range(1, num):
        if num % i == 0:
            total_number = total_number+1
        return total_number == num
    
number = int(input("enter the number:"))
if perfectnumber(number):
    print(f"{number}: perfectnumber")
else:
    print(f"{number}: notperfectnumber")

# #6

def anagram(str1, str2):
  return sorted(str1)== sorted(str2)
string1 = "listen"
string2 = "silent"
   
if anagram  (string1,string2):
   print("True")
else:
   print("False")



# #7

def lcm(number1, number2):
    greater = max(number1, number2)
    smallest = min(number1, number2)
    for i in range(greater, number1*number2+1, greater):
        if i % smallest == 0:
            return i
if __name__ == '__main__':
    number1 = 12
    number2 = 18
print("lcm of", number1, "and", number2, "is", lcm(number1, number2))

# #8

Input_list =[1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency_count = {}
for item in Input_list:
    if item in frequency_count:
        frequency_count[item] +=1
    else:
        frequency_count[item] = 1
print("input_list =", Input_list)
print("frequency_count = ", frequency_count)
#9
def reverse_function(input_sentence):
    words = input_sentence.split()
    reversed_function = " " .join(reversed(words))
    return reversed_function

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_function(input_sentence)
print("output after reverse =", output_sentence)

# #10

def sum_of_digits(num):
    while num >= 10:
        temp = num
        total = 0
        while temp >0:
            total += temp % 10
            num = temp // 10
            num = total
        return total
num = 9876
result = sum_of_digits(num)
print("Sum of digits until single_digit:", result )

# #11

def reverse_number(num):
    revnum = 0
    while num>0:
        reminder = num % 10
        revnum = (revnum*10)+ reminder
        num = num // 10
    return revnum
num = 12345
revnum = reverse_number(num)
print("original number:", num)
print("reversed number:", revnum)


