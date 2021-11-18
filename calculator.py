banner = '''
                                                                                                   
 @@@@@@@   @@@@@@   @@@        @@@@@@@  @@@  @@@  @@@        @@@@@@   @@@@@@@   @@@@@@   @@@@@@@   
@@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
!@@       @@!  @@@  @@!       !@@       @@!  @@@  @@!       @@!  @@@    @@!    @@!  @@@  @@!  @@@  
!@!       !@!  @!@  !@!       !@!       !@!  @!@  !@!       !@!  @!@    !@!    !@!  @!@  !@!  @!@  
!@!       @!@!@!@!  @!!       !@!       @!@  !@!  @!!       @!@!@!@!    @!!    @!@  !@!  @!@!!@!   
!!!       !!!@!!!!  !!!       !!!       !@!  !!!  !!!       !!!@!!!!    !!!    !@!  !!!  !!@!@!    
:!!       !!:  !!!  !!:       :!!       !!:  !!!  !!:       !!:  !!!    !!:    !!:  !!!  !!: :!!   
:!:       :!:  !:!   :!:      :!:       :!:  !:!   :!:      :!:  !:!    :!:    :!:  !:!  :!:  !:!  
 ::: :::  ::   :::   :: ::::   ::: :::  ::::: ::   :: ::::  ::   :::     ::    ::::: ::  ::   :::  
 :: :: :   :   : :  : :: : :   :: :: :   : :  :   : :: : :   :   : :     :      : :  :    :   : :  
                                                                                                   
'''
print(banner)

while True:
    islem=input("Please Select Transaction(+,-,*,/,**) : ")
    if(islem=="q"):
        print("EXİT")
        break
    elif(islem=="+"):
        sayi1=input("Number one : "))
        sayi2=input("Number two : "))
        try:
            sayi_1 = int(sayi1)
            sayi_2 = int(sayi2)
            total = sayi_1 + sayi_2
            print(total)
        except ValueError:
            print("Please use the number !!!!")
    elif(islem=="-"):
        sayi1=input("Number one : ")
        sayi2=input("Number two : ")
        try:
            sayi_1 = int(sayi1)
            sayi_2 = int(sayi2)
            total = sayi_1 - sayi_2
            print(total)
        except ValueError:
            print("Please use the number !!!!")
    elif(islem=="*"):
        sayi1=input("Number one : ")
        sayi2=input("Number two : ")
        try:
            sayi_1 = int(sayi1)
            sayi_2 = int(sayi2)
            total = sayi_1 * sayi_2
            print(total)
        except ValueError:
            print("Please use the number !!!!")
    elif(islem=="/"):
        sayi1=input("Number one : ")
        sayi2=input("Number two : ")
        try:
            sayi_1 = int(sayi1)
            sayi_2 = int(sayi2)
            total = sayi_1 / sayi_2
            print(total)
        except ValueError:
            print("Please use the number !!!!")
    elif(islem=="**"):
        sayi1=input("Number one : ")
        sayi2=input("Number two : ")
        try:
            sayi_1 = int(sayi1)
            sayi_2 = int(sayi2)
            total = sayi_1 ** sayi_2
            print(total)
        except ValueError:
            print("Please use the number !!!!")
    



