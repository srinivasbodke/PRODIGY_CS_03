
def passCheck(password):
    upper = 0
    lower = 0
    num = 0
    special = 0

    for x in password:
        if x.isupper(): # uppercase checker
            upper += 1
        
        if x.islower(): # lowercase checker
            lower += 1
        
        if x.isdigit(): # number checker
            num += 1
        
        if not x.isalnum(): # special char checker
            special += 1
        
    print("")

    print("PASSWORD STATUS:\n")
    if len(password) < 8:
        print("Password is Invalid! (Less than 8 characters!)\n")
        

    if(upper == 0):
        print("No uppercase letters! (Ex: ABCDEFGHIJKLMNOPQRSTUVWXYZ)\n")
    
    if(lower == 0):
        print("No lowercase letters!  (Ex: abcdefghijklmnopqrstuvwxyz)\n")
    
    if(num == 0):
        print("No numbers! (Ex: 1234567890)\n")

    if(special == 0):
        print("No special characters! (Ex: ~, @, $, *,?, !)\n")

    if(special != 0 and num != 0 and lower != 0 and upper != 0 and len(password) >= 8):
        print("Password is strong!\n")





print("PASSWORD CHECKER")

password = input("Enter a sentence: ")

passCheck(password)
