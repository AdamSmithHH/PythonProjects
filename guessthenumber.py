import random
import time

banner = """
  #####                                                        #     #                                    
 #     # #    # ######  ####   ####     ##### #    # ######    ##    # #    # #    # #####  ###### #####  
 #       #    # #      #      #           #   #    # #         # #   # #    # ##  ## #    # #      #    # 
 #  #### #    # #####   ####   ####       #   ###### #####     #  #  # #    # # ## # #####  #####  #    # 
 #     # #    # #           #      #      #   #    # #         #   # # #    # #    # #    # #      #####  
 #     # #    # #      #    # #    #      #   #    # #         #    ## #    # #    # #    # #      #   #  
  #####   ####  ######  ####   ####       #   #    # ######    #     #  ####  #    # #####  ###### #    # 
                                                                                                                                                                                              
"""


print(banner)
print("Welcome to the game that keeps a number between 1 and 100 in mind ")

sayi= random.randint(1,100)
tahmin_hakki=5



while True:
    tahmin=int(input("Guess The Number : "))
    if (tahmin == sayi):
        print(f"You Guessed Correctly Congratulations Predicted Number {sayi}")
    elif(tahmin > sayi):
        print("Choose a lower number")
        tahmin_hakki-=1
        print(f"Remaining guess :{tahmin_hakki} ")
    elif(tahmin < sayi):
        print("Choose a big number")
        tahmin_hakki-=1
        print(f"Remaining guess :{tahmin_hakki} ")
    if (tahmin_hakki==0):
        print("Game Finish")
        print(f"Number of computer {sayi}")
        print("////////////////////////////////////")
        print("AdamSmithH_ development")
        break
