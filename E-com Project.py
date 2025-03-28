Fruits=["Banana (100/Dozen)","Apple (120/kg)","Orange (140/Dozen)","Mange (180/kg)"]
Vegetables=["Tomato (120/kg)","Potato (130/kg)","Onion (100/kg)","LadyFinger (120/kg)"]
Cosmetic=["Shampoo (350 only)","Cream (400 only)","FWash (200 only)","FMask (130 only)"]
Kitchen_items=["Spoon (15)","Cooker (2500)","CupHolder (200)","Oven (35000)"]
Bakery_items=["CreamRolls (30)","ButterBiscuits (500/kg)","Pastry (30)","Pizza (60)"]


def itemlist(items):
    count=1
    for i in items:
        print("\t", count ," : " , i)
        count+=1

                
print(" \t 'Welcome To My Store' ")
print("""
    1: Fruits
    2: Vegetables
    3: Cosmetics
    4: Kitchen items
    5: Bakery items
""")

cart=[]

while True:

    user_input=int(input("Which Category would you like to choose? : "))
    if user_input == 1:
        itemlist(Fruits)

        user_choice=int(input("Add to your cart? "))
        if user_choice == 1:
            cart.append[0]

        elif user_choice == 2:
            cart.append(120)   

        elif user_choice == 3:
            cart.append(140) 

        elif user_choice == 4:
            cart.append(180)  

        else:
            print("Invalid Item number!")            
              

    elif user_input == 2:
        itemlist(Vegetables) 

        user_choice=int(input("Add to your cart? "))
        if user_choice == 1:
            cart.append(120)

        elif user_choice == 2:
            cart.append(130)   

        elif user_choice == 3:
            cart.append(100) 

        elif user_choice == 4:
            cart.append(120)  

        else:
            print("Invalid Item number!")

    elif user_input == 3:
        itemlist(Cosmetic) 

        user_choice=int(input("Add to your cart? "))
        if user_choice == 1:
            cart.append(350)

        elif user_choice == 2:
            cart.append(400)   

        elif user_choice == 3:
            cart.append(200) 

        elif user_choice == 4:
            cart.append(130)  

        else:
            print("Invalid Item number!") 

    elif user_input == 4:
        itemlist(Kitchen_items)  

        user_choice=int(input("Add to your cart? "))
        if user_choice == 1:
            cart.append(15)

        elif user_choice == 2:
            cart.append(2500)   

        elif user_choice == 3:
            cart.append(200) 

        elif user_choice == 4:
            cart.append(35000)  

        else:
            print("Invalid Item number!") 

    elif user_input == 5:
        itemlist(Bakery_items)
        
        user_choice=int(input("Add to your cart? "))
        if user_choice == 1:
            cart.append(30)

        elif user_choice == 2:
            cart.append(500)   

        elif user_choice == 3:
            cart.append(30) 

        elif user_choice == 4:
            cart.append(60)  

        else:
            print("Invalid Item number!")        
    else:
        print("Invalid Category Selection!")   

    askagain=input("Do you want to buy anything else? (y/n) : ") 
    if askagain == "n":
        total=sum(cart)
        print(f"Your Total Bill : {total}")
        print("Thanks for vistiing our store")   
        exit()




