#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 1/23/25
#Project #: 2
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.
firstName = 'Kory' #My First Name
print('Hello, my name is ' + firstName) #Print my first name

school = 'Utah Valley University' #My school
print('I go to ' + school) #Print my school

credits = 3 #Credits per class
classes = 6 #Classes per semester
totalcredits = credits * classes #Total Credits per Semester

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalcredits) + ' credits') #Prints how many credits per semester

print('I would like to save money by taking this many credits.') #Common Sense

maxCredits = 12 #Maximum Credits to save money
costPerClass = 350 #Cost per Class
classFee = 20 #Fee for each class

totalCostPerSemester = (totalcredits - maxCredits) / credits * costPerClass + (classFee * ((totalcredits - maxCredits) / credits)) #The total cast per semester

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.') #Prints the ammount saved per semester

totalCostPerYear = totalCostPerSemester * 3 #The total cost per year

print('That is a wopping $' + str(totalCostPerYear) + ' a year!') #Prints the total cost per year

print('This was a very informative and worth while Python assignment!') #Common Sense
