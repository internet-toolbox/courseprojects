print("This is a simple test written in Python")

ans = input("Are you ready to start the test? y/n: ")
score = 0
total_q = 10

if ans.lower() == "y":
    
    firstquestion = input("What is the biggest country in the world?")
    if firstquestion.lower() == "russia":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    secondquestion = input("What is the smallest country in the world?")
    if secondquestion.lower() == "vatican city":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    thirdquestion = input("What is the longest river in the world?")
    if thirdquestion.lower() == "river nile" or "nile river" or "nile":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    forthquestion = input("What is the capital of France?")
    if forthquestion.lower() == "paris":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    fifthquestion = input("What is the capital of Japan?")
    if fifthquestion.lower() == "tokyo":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    sixthquestion = input("What is the biggest continent in the world?")
    if sixthquestion.lower() == "asia":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    seventhquestion = input("What is the capital of Arizona?")
    if seventhquestion.lower() == "phoenix":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    eighthquestion = input("What is the capital of Denmark?")
    if eighthquestion.lower() == "copenhagen":
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    ninthquestion = input("How many countries are in the world?")
    if ninthquestion == 195:
        score += 1
        print("correct")
    else:
        print("Wrong")
        
    ninthquestion = input("How many countries are in Europe?")
    if ninthquestion == 44:
        score += 1
        print("correct")
    else:
        print("Wrong")
    
print ("Your score is" , score , "out of" , total_q)

input("Press any key to exit the program")
