import random #esto hace que se importe la funcion de randomizacion ("aleatoreidad")
num = random.randint(1,9)

Pregunta = (input("Cual es tu pregunta"))

if num == 9:
    print ("Yes")
elif num == 8:
    print ("It is decidedly so.")
elif num == 7:
    print ("Without a doubt.")
elif num == 6:   
    print ("Reply hazy, try again.") 
elif num == 5: 
    print ("Ask again later.")    
elif num == 4:
    print ("Better not tell you now.")   
elif num == 3:
    print ("My sources say no.")
elif num == 2:
    print ("Outlook not so good.")
else: 
    print ("Very doubtful.")   