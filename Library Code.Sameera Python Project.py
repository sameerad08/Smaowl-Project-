#library code
print("Welcome, choose your book")
print("1.The Lightning Thief")
print("2.The Sea of Monsters")
print("3.The Titans Curse")
print("4.The Battle of the Labrynth")
print("5.The Last Olympian")
print("6.The Sorcerers Stone")
print("7.The Chamber of Secrets") 
print("8.The Prisoner of Askaban")
print("9.The Goblet of Fire")
print("10.The Order of The Pheonix")
print("11.The Half-Blood Prince")
print("12.The Deathly Hallows")
print("13.The Selection")
print("14.The Elite")
print("15.The One")
b=int(input("Find Availablity, Author, and Number of Holds Placed By Entering Book Title Number#"))
if(b==1) or (b==2) or (b==3) or (b==4) or (b==5):
    print("Author:Rick Riorden")
if(b==6) or (b==7) or (b==8) or (b==9) or (b==10) or (b==11) or (b==12):
    print("Author:J.K Rowling")
elif(b==13) or (b==14) or (b==15):
    print("Author:Kiera Cass")
if(b==1) or (b==4) or (b==5) or (b==7) or (b==10) or (b==12) or (b==13) or (b==15):
    print("This Book is Available")
elif(b==2) or (b==3) or (b==6) or (b==8) or (b==9) or (b==11) or (b==14):
    print("This Book is Unavailable")
if (b==2):
    print("You are 1st in line to place a hold on this book")
if (b==3):
    print("5 Holds Placed on This Book")
if (b==6):
    print("8 Holds Placed on This Book")
if (b==8):
    print("1 Hold Placed on This Book")
if (b==9):
    print("10 Holds Placed on This Book")
if (b==11):
    print("2 Holds Placed on This Book")
elif(b==14):
    print("You are 1st in line to place a hold on this book")

print("Thank You For Coming This Library!")
    
    
