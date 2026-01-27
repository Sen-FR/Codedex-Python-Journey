
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0 
Slytherin = 0 
#Question 1
answer1= (input("Do you prefer Dawn or dusk?  (1) Dawn   (2)Dusk"))
if answer1 == "1" or answer1 == "dawn":
  Gryffindor += 1
  Ravenclaw += 1
elif answer1 =="2" or answer1 == "dusk":
  Hufflepuff += 1
  Slytherin += 1
else: 
    print("Wrong input")
#Question 2 
answer2 = int(input(
    "Q2) When I’m dead, I want people to remember me as: \n"
    "1) The good \n"
    "2) The Great\n"
    "3) The wise \n"
    "4) The Bold \n"))
if answer2 == 1: 
     Hufflepuff +=2
elif answer2 == 2:
       Slytherin +=2
elif answer2 == 3:
      Ravenclaw +=2
elif answer2 == 4:
      Gryffindor +=2
else: 
    print("Wrong input")
#Question 3
answer3 = int(input("Q3) Which kind of instrument most pleases your ear? \n"
"1) The violin \n"
"2) The trumpet \n"
"3) The piano \n"
"4) The drum \n"))

if answer3 == 1: 
     Slytherin +=4
elif answer3 == 2:
       Hufflepuff +=4
elif answer3 == 3:
      Ravenclaw +=4
elif answer3 == 4:
      Gryffindor +=4
else: 
    print("Wrong input")
print("Gryffindor:", Gryffindor)
print("Ravenclaw:", Ravenclaw)
print("Hufflepuff:", Hufflepuff)
print("Slytherin:", Slytherin)
