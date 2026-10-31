class employee:
    def sign_up(self,employee):
        print("--------Sign up--------")
        username=input("Create username: ")
        password=input("Enter password: ")

        for employe in employee:
            if employe["username"] == username:
                print("Username already exists. Try another username.!")
                return

        new_user={
            "username" : username,
            "password" : password
        }

        employee.append(new_user)
        print("Sign up successfull!")

    def login(self,employee):
        print("--------Login--------")
        username=input("Enter username: ")
        password=input("Enter password: ")
        for employe in employee:
            if employe["username"]==username and employe["password"]==password:
                print("Login successful!")
                return username
        print("Invalid username or password. Try again!")
        return None

    def purchase(self,products,orders,username):
        print("--------Purchase products--------")
        pro_id=int(input("Enter product id: "))
        for product in products:
            if product["pro_id"] == pro_id:
                if product["quantity"] > 0:
                    product["quantity"] -= 1
                    order={
                        "order_id":len(orders)+1,
                        "product": product["pro_name"],
                        "username": username,
                        "status": "Pending"
                    }
                    orders.append(order)
                    print("Product booked successfully")
                    print("Waiting for admin confirmation")
                    return
                else:
                    print("Product out of stock!")
                    return
        print("Product not found!")
    def cncl_order(self, products, orders, username):
        print("--------Cancel Order--------")

        employee_orders = []

        for order in orders:
            if order["username"] == username:
                print("Order ID:", order["order_id"])
                print("Product:", order["product"])
                print("Status:", order["status"])

                employee_orders.append(order)

        if len(employee_orders) == 0:
            print("No orders available!")
            return

        order_id = int(input("Enter your order ID to cancel: "))

        for order in employee_orders:
            if order["order_id"] == order_id:

                if order["status"] == "Pending":
                    order["status"] = "Cancelled"

                    for product in products:
                        if product["pro_name"] == order["product"]:
                            product["quantity"] += 1
                            break

                    print("Order cancelled successfully!")
                    return

                else:
                    print("Order cannot be cancelled!")
                    return

        print("Invalid order ID!")

