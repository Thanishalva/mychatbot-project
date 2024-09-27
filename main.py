
import random
import pyttsx3
import pyjokes
AI=pyttsx3.init()
speed=AI.getProperty('rate')
AI.setProperty('rate',speed-50)
possible_command_values1=["addition","sum","add","plus","subtraction","subtract","minus","divide","division","remainder","quotient","product","multiplication","percentage","modulo","maths","math","mathematics","mathematic","problems","solution"]
possible_joke_values=["jokes","joke","funny","funniest","laugh","sad","low","dull","mood"]
possible_game_values=["game","entertatinment","entertain","games","stone paper scissor","stone","paper","scissor","rock","play","gaming","challenge","fun","playtime","playtime","interactive","puzzle","competetion","score","quest","levels","stratergy","leaderboard","achievement","multiplayer","playthrough","simulation","bored"]
#gae this function name wspeech which helps to indicate that this function reads and writes text
def wspeech(text):
    print(text)
    AI.say(text)
    AI.runAndWait()
#just to speak
def speech(text):
    AI.say(text)
    AI.runAndWait()

def jokes():
    
    joke=pyjokes.get_joke()
    return joke
def check_validation(cmd,all_values):
    count=0
    for items in all_values:
        if items in cmd:
            count+=1
    if count!=0:
            pass
    else:
        
        wspeech("SORRY I DID NOT UNDERSTAND YOUR COMMAND.")
        
def create_table(n):
        #yes_or_no=["yes","ye","yeah",'please',"for sure","okay","ok","done","alright","please","no","naah","na","dont"]
        write=False
        res=""
        for i in range(1,11):
            res+=f"{n}X{i}={n*i}\n"
        speech("DO YOU WANT ME TO WRITE THE TABLE IN A SEPERATE FILE?")
        
        while(True):
            try:
                ask=input("DO YOU WANT ME TO WRITE THE TABLE IN A SEPERATE FILE?").lower()
            except ValueError:
                try_again()
            else:
                if "ye" in ask or "please" in ask or "for sure" in ask or "ok" in ask and "done" in ask or "allright" in ask or "alright" in ask :
                    with open(f"table_of_{n}.txt","w") as f:
                        f.write(res)
                        wspeech(f"THE TABLE OF NUMBER {n} HAS BEEN SUCCESSFULLY WRITTEN IN THE FILE : table_of_{n}.txt")
                        break
                elif "no" in ask or "na" in ask or "dont" in ask or "never" in ask:
                    wspeech(f"HERE IS THE TABLE OF NUMBER {n}:")
                    print(res)
                    break
                else:
                    try_again()

def games(USER):
    list=["ROCK ","PAPER","SCISSOR"]
    validationlist1=[1,2,3]
    AI=pyttsx3.init()
    user_points=0
    computer_points=0
    i=0
    print("*"*117)
    print("\t\t\t\tWHO EVER GETS 3 POINTS FIRST WINS!")
    print("*"*117)
    speech("WHO EVER GETS 3 POINTS FIRST WINS!")
    
    speech("ENTER  1 FOR ROCK. 2 FOR PAPER AND  3 FOR SCISSOR :")
    
    while  (user_points<3 and  computer_points<3):
        while(i<1):
            if computer_points==2 and user_points==2:
                wspeech("BE EXTREMELY CAREFUL WHILE CHOSING, AS BOTH YOU AND COMPUTER HAVE 2 POINTS, ONE BAD CHOICE AND YOU WILL LOSE THE GAME")
                i+=1
            else:
                break
    #USER SELECTS
        try:
            user_num=int(input("ENTER YOUR CHOICE[1 FOR ROCK,2 FOR PAPER,3 FOR SCISSOR ]: "))
        except ValueError:
            try_again()
        else:
            if user_num not in validationlist1 :
                wspeech("PLEASE ENTER  A VALID NUMBER!")
            if user_num==1:
                user_choice=list[0]
            elif user_num==2:
                user_choice=list[1]
            elif user_num==3:
                user_choice=list[2]
            #COMPUTER SELECTS
            computer_num=random.randint(1,3)
            if computer_num==1:
                comp_choice=list[0]
            elif computer_num==2:
                comp_choice=list[1]
            elif computer_num==3:
                comp_choice=list[2]
            #RESULT
            if user_num==computer_num:
                wspeech("ITS A DRAW")
                print(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif user_num==1 and computer_num==2:
                wspeech(f"{USER} SELECTED {list[0]} AND COMPUTER SELECTED {list[1]}!! COMPUTER WINS")
                computer_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif user_num == 1 and computer_num == 3:
                wspeech(f"{USER} SELECTED {list[0]} AND COMPUTER SELECTED {list[2]}!! {USER} WINS")
                user_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif user_num == 2 and computer_num == 1:
                wspeech(f"{USER} SELECTED {list[1]} AND COMPUTER SELECTED {list[0]}!! {USER} WINS")
                user_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif user_num == 3 and computer_num == 2:
                wspeech(f"{USER} SELECTED {list[2]} AND COMPUTER SELECTED {list[1]}!! {USER} WINS")
                user_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif computer_num == 1 and user_num == 3:
                wspeech(f"{USER} SELECTED {list[2]} AND COMPUTER SELECTED {list[0]}!! COMPUTER WINS")
                computer_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif computer_num == 2 and user_num == 1:
                wspeech(f"{USER} SELECTED {list[0]} AND COMPUTER SELECTED {list[1]}!! COMPUTER WINS")
                computer_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
            elif computer_num == 3 and user_num == 2:
                wspeech(f"{USER} SELECTED {list[1]} AND COMPUTER SELECTED {list[2]}!! COMPUTER WINS")
                computer_points+=1
                wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
    if computer_points==3:
        wspeech("COMPUTER WON !!BETTER LUCK NEXT TIME :( ")
        wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
    elif user_points==3:
        wspeech("CONGRATULATIONS!!! YOU WON :)")
        wspeech(f"{USER}:{user_points}\tCOMPUTER:{computer_points}")
        

def math():
    possible_user_values=["addition","sum","add","plus","subtraction","subtract","minus","divide","division","remainder","quotient","product","multiplication","percentage","modulo"]
    sum=0

    diff=0
    
    tex="WHICH MATHEMATIC CALCULATION DO YOU WANT TO PERFORM?"
    speech(tex)
    ask_user=input(tex)
    if ask_user.isupper:
        user_input=ask_user.lower()
    else:
        user_input=ask_user
    # for iterate in range(len(possible_user_values)):
    for i in range(len(possible_user_values)):
        if i<3 and i!=3:
            if possible_user_values[i] in user_input or user_input==possible_user_values[i]:
                text1="ADDITION OF HOW MANY NUMBERS?"
                speech(text1)
                ask_number=int(input(text1))
                for length in range(1,ask_number+1):
                    text2=f'ENTER NUMBER {length}:'
                    speech(text2)
                    numbers=float(input(text2))
                    sum+=numbers
                
                return f"SUM OF THE GIVEN NUMBERS ARE: {sum}"
        elif(i>=3 and i<7):
            if possible_user_values[i] in user_input or user_input==possible_user_values[i]:
                wspeech("SURE! I CAN HELP YOU WITH SUBTRACTING TWO NUMBERS:")
                
                num1=float(input("ENTER NUMBER 1:"))
                num2=float(input("ENTER NUMBER 2:"))
                diff=num2-num1
                return f"DIFFERENCE OF THE GIVEN NUMBERS ARE:{diff}"
        elif (i>=7 and i<11):
            if possible_user_values[i] in user_input or user_input==possible_user_values[i]:
                wspeech("SURE! I CAN HELP YOU WITH DIVISION:")
                speech("ENTER NUMBER 1:")
                num1=float(input("ENTER NUMBER 1:"))
                speech("ENTER NUMBER 2:")
                num2=0
                while (num2==0):
                    num2=float(input("ENTER NUMBER 2:"))
                    if num2==0:
                        wspeech('DENOMINATOR MUST NOT BE EQUAL, PLEASE ENTER NUMBER 2 AGAIN!')

                div=num2/num1
                return f"RESULT OF THE DIVISION IS :{div}"
        elif(i>=11 ):
            if possible_user_values[i] in user_input or user_input==possible_user_values[i]:
                wspeech("SURE! I CAN HELP YOU WITH MULTIPLICATION:")
                speech("ENTER NUMBER 1:")
                num1=float(input("ENTER NUMBER 1:"))
                speech("ENTER NUMBER 2:")
                num2=float(input("ENTER NUMBER 2:"))
                prod=num1*num2
                return f"RESULT OF THE MULTIPLICATION  IS :{prod}"
            else:
                return "SORRY I DID NOT UNDERSTAND YOUR COMMAND."
            
def table(number):
    for i in range(1,11):
        res+=f"{number}X{i}={number*i}\n"
def create_multiple_tables(n1,n2):
    res=""
    write=False
    speech("DO YOU WANT ME TO WRITE THE TABLEs IN  SEPERATE FILES?")
    ask=input("DO YOU WANT ME TO WRITE THE TABLE IN SEPERATE FILES?").lower()
    yes_or_no=["yes","ye","yeah",'please',"for sure","okay","ok","done","alright","please"]
    for each in yes_or_no:
        if each in ask:
            write=True
        else:
            pass
    if write==True:
        for n in range(n1,n2+1):
            for i in range(1,11):
                res+=f"{n}x{i}={n*i}\n"
                
            with open(f"table_of_{n}.txt","w") as f:
                f.write(res)
            if i==10:
                res=""
        wspeech("THE TABLES HAVE BEEN SUCCESFULLY STORED.PLEASE CHECK THE FOLDER!")
    elif write==False:
        for n in range(n1,n2+1):
            for i in range(1,11):
                res+=f"{n}x{i}={n*i}\n"
            wspeech(f"table of {n} is :")
            print(res)
            if i==10:
                res=""
def try_again():
    wspeech("SORRY I DID NOT UNDERSTAND YOUR COMMAND. PLEASE TRY AGAIN")               


def main():
    speech("PLEASE ENTER YOUR NAME:")
    name=input("PLEASE ENTER YOUR NAME: ")
    speech(f"HELLO {name}, i'am your chatbot.")
    allvalues=["table"]
    while True:
        speech(" how can i help you?")
        command=input(f"HELLO {name}, HOW CAN I HELP YOU?: ").lower()
        for each_values in possible_command_values1:
            allvalues.append(each_values)
            if each_values in command:
                wspeech("I SEE THAT YOU WANT A HELP FROM ME WITH MATHEMATICS! I CAN FOR SURE HELP YOU WITH BASIC MATHEMATIC CALCULATIONS!")
                a=math()
                wspeech(a)
                break
            
        for each_values in possible_joke_values:
            allvalues.append(each_values)
            if each_values in command:
                
                speech("I CAN TELL A FUNNY  JOKE FOR YOU TO LIGHTEN UP YOUR MOOD !")
                
                jk=0
                while (jk!=1):
                    b=jokes()
                    wspeech(b)
                    speech("IF YOU WANT ME TO SAY ANOTHER JOKE THEN ENTER ANY NUMBER, AND IF YOU DONT WANT ANOTHER JOKE THEN CLICK 1")
                    
                    another_joke=int(input("IF YOU WANT ME TO SAY ANOTHER JOKE THEN ENTER ANY NUMBER, AND IF YOU DONT WANT ANOTHER JOKE THEN CLICK 1:  "))
                    if another_joke==1:
                        jk=1
                else:
                    break
                
                        
                    
        
        for each_value in possible_game_values:
            allvalues.append(each_value)
            if each_value in command:
                wspeech("WE CAN PLAY A QUICK GAME OF ROCK PAPER SCISSOR TO KEEP YOU ENTERTAINED, DO YOU WANT TO PLAY?:  ")
                keep_asking=True
                while(keep_asking==True):
                    try:
                        ans=input("YES OR NO").lower()
                    except:
                        try_again()
                    else:
                        if "yes" in ans:
                            speech("THE GAME WILL BE PLAYED AMONG THE USER AND THE COMPUTER. IN THIS GAME USER SELECTS EITHER ROCK, PAPER OR SCISSOR.  COMPUTER WILL ALSO SELECT ANY OF THESE RANDOMLY")
                            games(name)
                            keep_asking=False
                            break
                        elif "no" in ans:
                            wspeech("NO PROBLEM, LET ME KNOW IF YOU NEED ANY ASSISTANCE FROM ME!")
                            keep_asking=False
                            break
                        else:
                            try_again()
                
        if "table" in command :
            speech("I CAN FOR SURE HELP YOU WITH CREATING MULTIPLICATION TABLE! ENTER NUMBER 1 FOR MULTIPLICATION TABLE OF SINGLE NUMBER.  OR ENTER 2 FOR MULITPLICATION TABLES OF A RANGE OF NUMBERS!!!!")
            z=0
            while(z==0):
                try:
                    varn=int(input(" ENTER NUMBER 1 FOR MULTIPLICATION TABLE OF SINGLE NUMBER OR ENTER NUMBER 2 FOR MULTPLICATION TABLES OF A RANGE OF NUMBERS: "))
                except ValueError:
                    try_again()
                else:
                    z+=1
                
            if varn==1:
                speech("PLEASE ENTER THE NUMBER OF HWICH YOU WANT MULTIPLICATION TABLE OF :")
                repeat=True
                while (repeat==True):
                    try:
                        num=int(input("PLEASE ENTER THE NUMBER OF WICH YOU WANT MULTIPLICATION TABLE OF :"))
                    except ValueError:
                        try_again()
                    else:
                        create_table(num)
                        repeat=False
            elif varn==2:
                repeat=True
                while repeat==True:
                    speech("PLEASE ENTER THE STARTING RANGE:")
                    try:
                        num1=int(input("PLEASE ENTER THE STARTING RANGE NUMBER:"))
                    except ValueError:
                        try_again()
                    else:
                        repeat_2=True
                        while(repeat_2==True):
                            speech("PLEASE ENTER THE ENDING RANGE:")
                            try:
                                num2=int(input("PLEASE ENTER THE ENDING RANGE NUMBER:"))
                            except ValueError:
                                try_again()
                            else:
                                create_multiple_tables(num1,num2)
                                repeat_2=False
                                repeat=False
            else:
                check_validation(command,allvalues)


        if "thank" in command:
            wspeech("GLAD I COULD ASSIST!")
        else:
            check_validation(command,allvalues)
       
main()




                



            

                
                    
                





    
    
            
