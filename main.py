import json
from admin_pckage.admin import admin
from employee.employee import employee
def ld_dt():
    with open("products.json","r") as file:
        data=json.load(file)
    return data
def save_dt(data):
    with open("products.json","w") as file:
        json.dump(data,file)
admin_obj=admin()
employee_obj=employee()
data=ld_dt()
while True:
    print("========INVENTORY MANAGEMENT SYSTEM========")
    print("1.Admin")
    print("2.Employee")
    print("3.Exit")
    choice=int(input("Enter your choice: "))

#admin

    if choice == 1:
        if admin_obj.login():
            while True:
                print("--------Admin Menu--------")
                print("1.View all products")
                print("2.Add products")
                print("3.Remove products")
                print("4.Search product")
                print("5.Confirm order")
                print("6.Logout")

                option=int(input("Enter your choice: "))
                if option == 1:
                    admin_obj.view_pro(data["products"])
                elif option ==2:
                    admin_obj.add_products(data["products"])
                elif option ==3:
                    admin_obj.remove_pro(data["products"])
                elif option ==4:
                    admin_obj.search_pro(data["products"])
                elif option == 5:
                    admin_obj.confirm_order(data["orders"])
                    save_dt(data)
                elif option == 6:
                    print("Admin logged out")
                    break
                else:
                    print("Invalid choice")

#Employee

    elif choice == 2:
        while True:
            print("--------Employee--------")
            print("1.Sign Up")
            print("2.Login")
            print("3.Back")
            echoice=int(input("Enter your choice: "))
            if echoice==1:
                employee_obj.sign_up(data["employee"])
                save_dt(data)
            elif echoice==2:
                username = employee_obj.login(data["employee"])
                if username is not None:
                    while True:
                        print("--------Employee Menu--------")
                        print("1.Search Products")
                        print("2.Purchase products")
                        print("3.Cancel orders")
                        print("4.Logout")
                        option=int(input("Enter your option: "))
                        if option==1:
                            admin_obj.search_pro(data["products"])
                        elif option==2:
                            employee_obj.purchase(data["products"], data["orders"], username)
                        elif option==3:
                            employee_obj.cncl_order(data["orders"],data["products"],username)
                        elif option==4:
                            print("Employee logged out!")
                            break
                        else:
                            print("Invalid choice.")
            elif echoice==3:
                print("Returning to Main Menu....")
                break
            else:
                print("Invalid choice!")
                
#Exit

    elif choice ==3:
        print("Thankyou for using inventory management system. See you again.")
        break
    else:
        print("Invalid choice!")