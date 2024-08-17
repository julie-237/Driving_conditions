country = input("In which country do you want to drive(France, South Africa, Mexico, India)? ")
Age = int(input("How old are you? "))

if country == "South Africa" :
    if Age >= 17 :
        print ("you can drive assisted by a 1 year old driver until you are a year older")
    else:
       print ("you can't drive") 
    
elif country == "France" :
    if Age >= 17 :
        print ("you can drive with restrictions until you are 2 or 3 years older")
    elif Age >= 15 :
        print("you can drive under supervision")
    else: 
        print("you can't drive")
    
elif country == "Mexico" :
    if Age >= 18 :
        print ("you can drive")
    elif Age >= 16 :
        print("you can drive with parentale agreement")
    elif Age == 15 :
        print("you can drive under supervision")
    else:
        print("you can't drive")
    
elif country == "India" :
    if Age >= 18 :
        print ("you can drive")
    else:
        print("you can't drive")
    
else:
    country != ("France, South Africa, Mexico, India")
    print ("Data is not available for this country")
    
