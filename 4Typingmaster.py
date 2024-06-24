from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except:
            error=error+1
    return error   

def Speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)

while True:
    ck = input("Ready to test : yes/no : ")
    if (ck == "yes"):     
        test=["Hello this is a paragraph a self-contained unit of discourse","This is a boy and you are a girl. Yes he is saying right!","ohh! How are you ? What do you mean by the Python..is it a programming language"]
        test1 = r.choice(test)
        print("       ***** Typing Speed *****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter : ")
        time_2 = time()

        print("Speed : ",Speed_time(time_1,time_2,testinput),"w/sec")
        print("Error : ",mistake(test1,testinput))
    elif(ck == "no"):
        print("      ***** Thank You *****")
        break
    else:
        print("Wrong Input!!")
