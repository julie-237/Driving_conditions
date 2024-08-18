country = input("In which country do you want to drive(France, South Africa, Mexico, India)? ")
cannot_drive_msg = "you can't drive"
can_drive_msg = "you can drive"
supervision_drive_msg = "you can drive under supervision"


"""if country not in  ("South Africa", "France", "Mexico", "India") :"""
if country !=  "South Africa" and country != "France" and country != "Mexico" and country != "India" :
    print ("Data is not available for this country")
else:
    Age = int(input("How old are you? "))
    if country == "South Africa" :
        if Age >= 17 :
            print ("you can drive assisted by a 1 year old driver until you are a year older")
        else:
            print (cannot_drive_msg) 
        
    elif country == "France" :
        if Age >= 17 :
            print ("you can drive with restrictions until you are 2 or 3 years older")
        elif Age >= 15 :
            print (supervision_drive_msg)
        else: 
            print (cannot_drive_msg)
        
    elif country == "Mexico" :
        if Age >= 18 :
            print (can_drive_msg)
        elif Age >= 16 :
            print("you can drive with parentale agreement")
        elif Age == 15 :
            print (supervision_drive_msg)
        else:
            print (cannot_drive_msg)
        
    elif country == "India" :
        if Age >= 18 :
            print (can_drive_msg)
        else:
            print (cannot_drive_msg)
            
            
            
""" lets assume the country in which we wish to drive is spain
at line 7, the console will print 'Data is not available for this country' and the program will end there.

lets assume the country in which we wish to drive is south africa
at line 11 the console will ask my age
assuming i am 17 years or more,
at line 14, the console will print 'you can drive assisted by a 1yr old driver until you are a yr older' and the program will end there.
assuming i am less than 17,
at line 16, the console will print 'you can't drive' and the program will end there.

lets assume the country in which we wish to drive is france
at line 11 the console will ask my age
assuming i am 17 years or more,
at line 20, the console will print 'you can drive with restrictions until you are 2 or 3 years older' and the program will end there.
assuming i am 15 years or more,
at line 22, the console will print 'you can drive under supervision' and the program will end there.
assuming i am less than 15,
at line 24, the console will print 'you can't drive' and the program will end there.

lets assume the country in which we wish to drive is mexico
at line 11 the console will ask my age
assuming i am 18 years or more,
at line 28, the console will print 'you can drive' and the program will end there.
assuming i am 16 years or more,
at line 30, the console will print 'you can drive with parentale agreement' and the program will end there.
assuming i am 15 years old,
at line 32, the console will print 'you can drive under supervision' and the program will end there.
assuming i am less than 15,
at line 34, the console will print 'you can't drive' and the program will end there.

lets assume the country in which we wish to drive is south africa
at line 11 the console will ask my age
assuming i am 18 years or more,
at line 38, the console will print 'you can drive' and the program will end there.
assuming i am less than 18,
at line 40, the console will print 'you can't drive' and the program will end there.          
 """
        
