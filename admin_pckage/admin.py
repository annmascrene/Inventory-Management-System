class admin:
    def login(self):
        username=input("Enter username: ")
        password=input("Enter password: ")
        if username == 'Ann Mascrene' and password == '12345':
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Try again!")
            return False

    def add_products(self,products):
        print("--------Add Products--------")
        pro_id=int(input("Enter product ID: "))
        pro_name=input("Enter product name: ")
        pro_price=float(input("Enter product price: "))
        quantity=int(input("Enter quantity: "))

        product={
            "pro_id" : pro_id,
            "pro_name": pro_name,
            "pro_price": pro_price,
            "quantity": quantity
        }

        products.append(product)
        print("Product added sucessfully!")

    def remove_pro(self,products):
        print("--------Remove Products--------")
        pro_id=int(input("Enter product ID: "))
        for product in products:
            if product["pro_id"] == pro_id:
                products.remove(product)
                print("Product removed successfully!")
                break
                return
        print("Product unavailable!")

    def view_pro(self,products):
        print("--------All Products--------")
        for product in products:
            print("Product ID: ",product["pro_id"])
            print("Product name: ",product["pro_name"])
            print("Product price: ",product["pro_price"])
            print("Quantity: ",product["quantity"])

        if len(products) == 0:
            print("No products available")
            return

    def search_pro(self,products):
        print("--------Search Products--------")
        pro_id=int(input("Enter product id: "))
        for product in products:
            if product["pro_id"] == pro_id:
                print("Product ID: ",product["pro_id"])
                print("Product name: ",product["pro_name"])
                print("Product price: ",product["pro_price"])
                print("Quantity: ",product["quantity"])
                return
        print("Product not found!")

    def confirm_order(self,orders):
        self.__confirm_order(orders)
    def __confirm_order(self,orders):
        print("--------Confirm order--------")
        if len(orders) == 0:
            print("No orders available!")
            return
        for order in orders:
            print("Order ID: ",order["order_id"])
            print("Username: ",order["username"])
            print("Product: ",order["product"])
            print("Status: ",order["status"])

            if order["status"] == "Pending":
                choice=input("COnfirm order status - Yes / No: ")
                if choice.lower() == "yes":
                    order["status"] = "Confirmed"
                    print("Order confirmed!")

