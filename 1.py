import random

snakes={98:58,
        96:84,
        94:73,
        90:72,
        86:54,
        69:12,
        61:59,
        56:25,
        43:38,
        23:5}

snake_found=list(snakes.keys())
snake_slide=list(snakes.values())

ladder={80:99,
        89:91,
        77:95,
        64:83,
        56:70,
        37:76,
        32:48,
        16:26,
        8:55,
        3:21}

ladder_found=list(ladder.keys())
ladder_climb=list(ladder.values())


place=[1,2,3,4,5,6]

user_initial=0
bot_initial=0
ctr=0


def interface():
    print("WELCOME TO SNAKE AND LADDER GAME")
    print("Version 1.0.0")
    print("DEVELOPED BY CODING_CREW")
    print()
    print()
    print("----------------------------------------------------")
    print("| 100 | 99 | 98 | 97 | 96 | 95 | 94 | 93 | 92 | 91 |")
    print("| 90  | 89 | 88 | 87 | 86 | 85 | 84 | 83 | 82 | 81 |")
    print("| 80  | 79 | 78 | 77 | 76 | 75 | 74 | 73 | 72 | 71 |")
    print("| 70  | 69 | 68 | 67 | 66 | 65 | 64 | 63 | 62 | 61 |")
    print("| 60  | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 |")
    print("| 50  | 49 | 48 | 47 | 46 | 55 | 44 | 43 | 42 | 41 |")
    print("| 40  | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 31 |")
    print("| 30  | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 |")
    print("| 20  | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 |")
    print("| 10  | 09 | 08 | 07 | 06 | 05 | 04 | 03 | 02 | 01 |")
    print("----------------------------------------------------")

    for sp in range(3):
        print()
    print("RULES AND REGULATIONS : ")
    print("-------------------------")
    print("1. INITIALLY YOU ARE AT 0")
    print("2. IF YOU LAND AT THE BOTTOM OF A LADDER,YOU CAN MOVE UP TO THE TOP OF THE LADDER")
    print("3. IF YOU LAND AT THE HEAD OF A SNAKE,YOU CAN SLIDE DOWN TO THE BOTTOM OF THE SNAKE")
    print("4. HIT ENTER TO ROLL THE DICE")
    print("5. THE FIRST TO REACH BETWEEN YOU AND BOT IS THE WINNER")
    for sp in range(3):
        print()
    name=input("ENTER YOUR NAME :- ")
    name=name.upper()
    print()
    print("MATCH PLAYED BETWEEN",name,"AND THE BOT")
    print()

def enter():
    global user_initial
    global bot_initial
    global ctr
    
    if ctr%2==0:
        print("---------------------------")
        chance=input("PRESS ENTER TO ROLL THE DICE :- ")
        if chance=='':
            user_final=random.choice(place)
            print("IT'S A ",user_final)
            u=user_initial
            

            if u>=94:
                if (u+user_final)>100:
                    print("YOU NEEDS A PERFECT OR LESSER DICE")
                else:
                    user_initial+=user_final
                    print("YOU MOVED FROM",u,"TO",user_initial)
            
            else:
                user_initial+=user_final
                print("YOU MOVED FROM",u,"TO",user_initial)
            u=user_initial
            print("---------------------------")

            for sp in range(1):
                print()


            for x in range(0,len(snake_found)):
                if snake_found[x]==user_initial:
                    user_initial=snake_slide[x]
                    print("---------------------------")
                    print("OH!!")
                    print("YOU MOVED DOWN FROM",u,"TO",user_initial)
                    print("---------------------------")
                    print()
                    print()
                    print()

            for y in range(0,len(ladder_found)):
                if ladder_found[y]==user_initial:
                    user_initial=ladder_climb[y]
                    print("---------------------------")
                    print("WOW!!")
                    print("YOU MOVED UP FROM",u,"TO",user_initial)
                    print("---------------------------")
                    print()
                    print()
                    print()
            

    else:
        print("---------------------------")
        print("BOT'S CHANCE")
        bot_final=random.choice(place)
        print("IT'S A ",bot_final)
        b=bot_initial

        if b>=94:
                if (b+bot_final)>100:
                    print("COMPUTER NEEDS A PERFECT OR LESSER DICE")
                else:
                    bot_initial+=bot_final
                    print("BOT MOVED FROM",b,"TO",bot_initial)
        else:
            bot_initial+=bot_final
            print("BOT MOVED FROM",b,"TO",bot_initial)
        b=bot_initial
        print("---------------------------")

        for sp in range(1):
            print()


        for x in range(0,len(snake_found)):
                if snake_found[x]==bot_initial:
                    bot_initial=snake_slide[x]
                    print("---------------------------")
                    print("OH!!")
                    print("BOT MOVED DOWN FROM",b,"TO",bot_initial)
                    print("---------------------------")
                    print()

        for y in range(0,len(ladder_found)):
                if ladder_found[y]==bot_initial:
                    bot_initial=ladder_climb[y]
                    print("---------------------------")
                    print("WOW!!")
                    print("BOT MOVED UP FROM",b,"TO",bot_initial)
                    print("---------------------------")
                    print()

    if ctr%2!=0:
        print("\t"*5,"USER'S SCORE:- ",user_initial)
        print("\t"*5,"BOT'S SCORE:- ",bot_initial)
    ctr+=1

                
interface()

def main():
    while True :
        enter()
        if user_initial>=100:
            print("YOU ARE THE WINNER")
            print("\t"*5,"USER'S SCORE:- ",user_initial)
            print("\t"*5,"BOT'S SCORE:- ",bot_initial)
            break
        elif bot_initial>=100:
            print("YOU ARE THE LOSER")
            break
main()
