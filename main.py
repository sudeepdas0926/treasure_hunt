print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line
print("You are a sailor and you are trapped in a desolate island with a map in which there is an inscription 'FOLLOW YOUR HEART EVEN IF IT TAKES YOU ON THE WRONG PATH'")
choice_direction = input("You are at a crossroad. Where do you want to go? 'Left' 'Right' 'Straight' ")
if choice_direction == "Left":
  print("You fell into a ditch")
  decision_ditch = int(input("now you have two options 1. To cry out loud for help\n2. To find something in the ditch to help you out. For option one click 1 and for option two click 2 "))
  if decision_ditch == 2:
    print("You found some logs and made a support to step out of the ditch ")
    print("\nafter passing through a narrow passage you reach an area with a variety of flowers. There are red,blue,yellow,white,violet,purple coloured flowers")
    print("\nafter passing through that area you see five roads infront of you which are going towards a huge cave")
    print("\nthe roads have five colours - blue,white yellow,red,violet")
    print("\nnear the roads you see a signboard in which there is an inscription which says 'MAY YOU REACH YOUR GOAL BY TRAVELLING THROUGH THE ROAD WHOSE COLOUR STAY WITH YOU IN THE LONG RUN'")
    choice_path = input("Which path will you choose? for blue type B\nfor white type W\nfor yellow type Y\nfor red type R\nfor violet type V ")
    if choice_path == 'R':
      print("congratulations you have made it through")
      print("\nYou travel through the road and at its end you find yourself infront of a humongous cave which is surrounded by many big trees and beautiful flowers about 15 steps from the cave there was a big yet narrow circle with some reddish fluid in it.")
      print("\nYou ignore it and move ahead. You are just going to enter the cave but at that point you hear a loud sound WAIT.")
      print("\nYou turn around but you don't find anyone on that place but when you examine the three pillar like structure at the entrance of the cave then you realise that they are not mere pillars but they are the parts of a gigantic armor.")
      print("\nWhen you look up then you see the complete size of the statue and you realise that it was as big as the cave itself and the worst part is that the armor is staring at you.")
      print("\nA metallic voice from the armor tells that it will ask three questions and you have to answer it in one word. If you fail in any of the question then the sword will be slicing you into two.")
      ready = input("Are you ready for its questions? If yes then type Y and if no then type N ")
      if ready == 'Y':
        print("answer the questions without any capital letters")
        print("first quetsion")
        first = input("At night they come without being fetched. By day they are lost without being stolen. What will be your answer? ")
        if first == "fear":
          print("correct")
          print("second question")
          second = input("You can only have it once you have given it. What will be your answer? ")
          if second == "respect":
            print("correct")
            print("final question")
            third = input("Journey without it and you will never prevail but if you have too much of it then you will surely fail. What will be your answer? ")
            if third == "confidence":
              print("correct")
              print("\nthe statue moves and the path is open")
              print("\nYou go inside and find three humongous boxes with their respective keys. The boxes have three colours- purple,violet,orange")
              print("\nyou search around and find a sign in which there is a writing which says 'THE COLOUR WHICH MARKS THE DAWN OF LIFE ON EARTH IS THE PLACE WHERE THE TREASURE OF THE FORMIDABLE CAPTAIN RESIDES'")
              chest = input("which chest will you choose? for choosing type the first letter of the colour in capital ")
              if chest == 'O':
                print("congratulations you have got the treasure")
              else:
                print("You opened the wrong chest and now you are trapped inside the cave forever")
            else:
              print("You are killed by the Great Guardian of the fortune")
          else:
            print("You are killed by the Great Guardian of the fortune")
        else:
          print("You are killed by the Great Guardian of the fortune")
      else:
        print("You are ordered to return by the Great Guardian of the fortune")
    else:
      print("The road cracked open and you fell into the lava and died")
  else:
    print("You keep calling out but no one comes for help and you ultimately die out of thirst and hunger")
elif choice_direction == "Right":
  print("you enter into a forest and die due to the bite of a poisonous snake")
else:
  print("you enter into a dense forest and die as you stepped on a scorpion")