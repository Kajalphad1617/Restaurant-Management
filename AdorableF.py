class Restaurant:
    user = {"kajal": ["123", "kajal@gmail.com"]}

    def __init__(self):
        self.Amenu_list = {
            "Chinese Food": {"Fried Rice": 160, "Manchurian": 120, "Schezwan Noddles": 180, "Tommato soup": 80, "Bassil fried rice": 130},
            "Thai Food": {"Green curry": 180, "Rice paper roll": 130, "Thai special": 120},
            "Indian Food": {"Thali special": 120, "veg biryani": 140, "paneer and roti":200},
            "desserts": {"vanilla scoop": 120, "brownie": 210, "choco fudge": 180,  "donuts": 60}
        } 
        self.name = "Adorable Restaurant"
        self.orderdict={}
        self.quantity={}

    def Registration(self):
        name = input("Enter name: ")
        if name.isdigit():
            print("......... Enter valid name ........")
        else:
            email = input("Enter your E-mail: ")
            if "@gmail.com" in email:
                password = input("Enter the password: ")
                self.user.update({name: [password, email]})
                print("Your Registration completed successfully.")
            else:
                print("........ Enter valid E-mail ........")

    def User_login(self):
        self.uname = input("Enter your name: ")
        if self.uname in self.user.keys():
            mail = input("Enter your E-mailid: ")
            if "@gmail.com" in mail:
                if mail == self.user.get(self.uname)[1]:
                    password = input("Enter password: ")
                    if password == self.user.get(self.uname)[0]:
                        print("*******>| Welcome", self.uname, "|<******")
                        while True:
                            print("-"*40)
                            print("1: Display_menu  \n2: Order  \n3: Cancel_order \n4: Billing \n5: Exit ")
                            print("-"*40)
                            choice1 = input("Enter your choice: ")
                            if choice1 == "1":
                                self.display_menu()
                            elif choice1 == "2":
                                self.order()
                            elif choice1 == "3":
                                self.CancelOrder()
                            elif choice1 == "4":
                                self.Billing()
                            elif choice1 == "5":
                                print("....Thank you for visiting our Restaurant....")
                                break
                            else:
                                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")
                    else:
                        print("  x-x-x-x  Incorrect Password   x-x-x-x  ")
            else:
                print("  x-x-x-x  Enter valid E-mail  x-x-x-x  ")
        else:
            print("  x-x-x-x  Enter valid name  x-x-x-x  ")

    
    def order(self):
        print("We have following menu in our Restaurant:")
        while True:
            print("-"*40)
            print("1: Chinese Food  \n2: Thai Food \n3: Indian Food \n4: Desserts  \n5: Exit")
            print("-"*40)
            choice = input("Enter your choice: ")
            if choice in ["1", "2", "3", "4", "5"]:
                if choice == "1":
                    section = "Chinese Food"
                elif choice == "2":
                    section = "Thai Food"
                elif choice == "3":
                    section = "Indian Food"
                elif choice == "4":
                    section = "desserts"
                elif choice == "5":
                    break
                self.menu = input("Enter menu name: ")
                
                if self.menu in self.Amenu_list[section]:
                    self.quantity1=int(input("Enter the quantity:-"))
                    self.quantity.update({self.menu:self.quantity1})
                    self.orderdict.update({self.menu:[self.quantity1,self.Amenu_list.get(section).get(self.menu)]})
                    print(self.orderdict)
                    print("You order", self.menu, "enjoy your meal.")
                    
                    
                else:
                    print("  x-x-x-x  There is no menu available with this name in ", section, "section  x-x-x-x  ")
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")

    def CancelOrder(self):
        print("-----We have following menu in our Restaurant-----:")
        while(True):
            print("-"*40)
            print("1:Chinese food  \n2:Thai Food \n3:Indian Food \n4.desserts \n5.Exit")
            print("-"*40)
            choice=input("Enter your choice :")
            if choice in ["1","2","3","4","5"]:
                if choice=="1":
                    section="Chinese Food"
                elif choice=="2":
                    section="Thai Food"
                elif choice=="3":
                    section="Indian Food"
                elif choice=="4":
                    section="desserts"
                elif choice=="5":

                    break
                menu=input("Enter the menu to be removed:")
                if menu in self.Amenu_list.get(section):
                   
                    self.orderdict.pop(menu)
                    print(self.orderdict)
                else:
                    print("  x-x-x-x In your orderList there is no menu with these name  x-x-x-x   ")
            else:
                    print("  x-x-x-x  Enter valid choice  x-x-x-x  ")

    def Billing(self):
        
        print(" "*10,"Restaurant Receipt")
        print(" "*12,"Delicacies from the oven")
        print(" "*10,"sector 11 khanda colony,panvel.")
        print(" "*12,"Mobile no=+915358556148")
        import datetime
        import functools
        import operator
        x=datetime.datetime.now()
        print(x.strftime("%c"))
        print('-'*78)
        print("Menu\t\t|\tRate\t|\tQuantity|\tTotal_price")
        print('-'*78) 
        for menu in self.orderdict.keys():
            total_price=self.orderdict.get(menu)[0]*self.orderdict.get(menu)[1]
           
        print(menu,'\t|\t',self.orderdict.get(menu)[1],'\t|','\t',self.orderdict.get(menu)[0],'\t|\t',"Rs.",total_price)
        print('-'*78)
        print("THANK YOU FOR DINNING WITH US!\nPLEASE COME AGAIN")





    def Manager_login(self):
        mname = input("Enter Manager name:")
        if 'kajal' in mname:
            memail = input("Enter manager e-mail:")
            if 'kajal@gmail.com' in memail:
                mpassword = input("Enter manager password:")
                if mpassword == '456':
                    while True:
                        print("....Welcome manager to Adorable Restaurant....")
                        print("\n1. Display Menu \n2. Update Menu \n3. Add menu \n.4 Remove Menu \n5. Users  \n6. Exit ")
                        print("-"*40)
                        choice = input("Enter your choice:")
                        if choice == '1':
                            self.display_menu()
                        elif choice == '2':
                            self.update_menu()
                        elif choice == '3':
                            self.Add_menu()
                        elif choice=='4':
                            self.remove_menu()
                        elif choice == '5':
                            print("visited users:")
                            j = 0
                            for i in self.user.keys():
                                j += 1
                                print('-----', i)
                            print("Total user visited:", j)
                        elif choice == '6':
                            break
                        else:
                            print("Enter correct choice")
                else:
                    print("______Enter correct password______")
            else:
                print("______Enter correct email______")
        else:
            print("______Enter correct name______")

    

    def display_menu(self):
        print("We have following menu in our Restaurant:")
        while True:
            print("-"*40)
            print("1: Chinese Food  \n2: Thai Food \n3: Indian Food \n4: Desserts  \n5: Exit")
            print("-"*40)
            choice = input("Enter your choice: ")
            if choice == "1":
                print("We have following menu in our Restaurant:")
                for menu, price in self.Amenu_list["Chinese Food"].items():
                    print("-->", menu, ":", price)
            elif choice == "2":
                print("We have following menu in our Restaurant:")
                for menu, price in self.Amenu_list["Thai Food"].items():
                    print("-->", menu, ":", price)
            elif choice == "3":
                print("We have following menu in our Restaurant:")
                for menu, price in self.Amenu_list["Indian Food"].items():
                    print("-->", menu, ":", price)
            elif choice == "4":
                print("We have following dessets in our Restaurant:")
                for menu, price in self.Amenu_list["desserts"].items():
                    print("-->", menu, ":", price)
            elif choice == "5":
                break
            else:
                print("  x-x-x-x  Enter valid choice  x-x-x-x  ")

    
    def update_menu(self):
        print("We have following items in our Restaurant:")
        while True:
            print("-"*40)
            print("1: Chinese Food  \n2: Thai Food \n3: Indian Food \n4: Desserts  \n5: Exit")
            print("-"*40)
            choice = input("Enter your choice : ")
            if choice in ["1", "2", "3", "4","5"]:
                if choice == "1":
                    section = "Chinese Food"
                elif choice == "2":
                    section = "Thai Food"
                elif choice == "3":
                    section = "Indian Food"
                elif choice == "4":
                    section = "desserts"
                elif choice == "5":
                 break
                print(f"We have following menu in {section}:")
                for menu, price in self.Amenu_list[section].items():
                    print("-->", menu, ":", price)

                menu_to_update = input("Enter menu name to update: ")
                if menu_to_update in self.Amenu_list[section]:
                    new_price = input(f"Enter new price for {menu_to_update}: ")
                    if new_price.isdigit():
                        self.Amenu_list[section][menu_to_update] = int(new_price)
                        print(f"{menu_to_update}' price has been updated to {new_price}.")
                    else:
                        print("Invalid price. Please enter a number.")
                else:
                    print("menu not found in the menu.")
                    
           
            else:
                print("Enter valid choice.")            


    
    def Add_menu(self):
        print("We have following items in our Restaurant:")
        while True:
            print("-"*40)
            print("1: Chinese Food  \n2: Thai Food \n3: Indian Food \n4: Desserts  \n5: Exit")
            print("-"*40)
            choice = input("Enter your choice : ")
            if choice in ["1", "2", "3", "4","5"]:
                if choice == "1":
                    section = "Chinese Food"
                elif choice == "2":
                    section = "Thai Food"
                elif choice == "3":
                    section = "Indian Food"
                elif choice == "4":
                    section = "desserts"
                elif choice == "5":
                 break
               
                add_menu = input("Enter menu name to Add: ")
                price=int(input("Enter the menu price: "))
                if add_menu not in self.Amenu_list[section]:
                    self.Amenu_list[section].update({add_menu:price})
                    print(add_menu,"Added to the list.")
                    
                else:
                    print(add_menu,"already present in the list.")
            else:
                print("Enter valid choice.")  



    def remove_menu(self):
        print("We have following menu in our Restaurant:")
        while True:
            print("-"*40)
            print("1: Chinese Food  \n2: Thai Food \n3: Indian Food \n4: Desserts  \n5: Exit")
            print("-"*40)
            choice = input("Enter your choice : ")
            if choice in ["1", "2", "3", "4","5"]:
                if choice == "1":
                    section = "Chinese Food"
                elif choice == "2":
                    section = "Thai Food"
                elif choice == "3":
                    section = "Indian Food"
                elif choice == "4":
                    section = "desserts"
                elif choice == "5":
                    break
                
                print(f"We have following menu in {section}:")
                for menu in self.Amenu_list[section].keys():
                    print("-->", menu)
                
                menu_to_remove = input("Enter menu name : ")
                if menu_to_remove in self.Amenu_list[section]:
                    self.Amenu_list[section].pop(menu_to_remove)
                    print(f"{menu_to_remove} has been removed from the menu list.")
                else:
                    print("menu not found in the menu.")
                
            
            else:
                print("Enter valid choice.")
    
    def Home(self):
        print("-------------> Welcome to ", self.name, " <------------------")
        while True:
            print("-"*40)
            print("\n1: Manager_login  \n2: User_login \n3: Registration \n4: Exit")
            print("-"*40)
            choice = input("Enter your choice: ")
            if choice == "1":
                self.Manager_login()
            elif choice == "2":
                self.User_login()
            elif choice == "3":
                self.Registration()
            elif choice == "4":
                break
            else:
                print("........  Enter valid choice  ........ ")          

Rest=Restaurant()
Rest.Home()