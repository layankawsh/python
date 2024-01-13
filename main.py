import tkinter as tk

def userandpass2():
    username = txtUsername.get()
    password = txtPassword.get()

    myfile = open("username.txt", "a")
    str1="\n"+username+"-"+password+"-end"
    myfile.write(str1)

def userandpass1():
    username=txtUsername.get()
    password=txtPassword.get()

    myfile=open("username.txt","r")
    alldata=myfile.readlines()

    for x in alldata:
        linedata=x.split("-")
        if username==linedata[0] and password==linedata[1]:
            lblOutput.config(text="Pass")
            break
        else:
            lblOutput.config(text="Fail")

soso=tk.Tk()

lblUsername=tk.Label(soso,text="Username")
lblPassword=tk.Label(soso,text="Password")
lblOutput=tk.Label(soso,text="......")

txtUsername=tk.Entry(soso)
txtPassword=tk.Entry(soso,show="*")

btnLogin=tk.Button(soso,text="Login",command=userandpass1)
btnSignup=tk.Button(soso,text="Signup",command=userandpass2)

lblUsername.pack()
txtUsername.pack()

lblPassword.pack()
txtPassword.pack()

btnLogin.pack()
lblOutput.pack()
btnSignup.pack()

soso.mainloop()

root = tk.Tk()
thelabel1=tk.Label(root,text="1,Sama M.W ")
thelabel2=tk.Label(root,text="2,Premia D.W ")
thelabel3=tk.Label(root,text="3,Sama Appel Juice")
thelabel4=tk.Label(root,text="4,Sama Mango Juice")
thelabel5=tk.Label(root,text="5,Sama Orange Juice")
thelabel6=tk.Label(root,text="6,Sama Pineapple Juice")
thelabel7=tk.Label(root,text="7,Sama Multifruit Juice")
thelabel8=tk.Label(root,text="8,Sama Guava Juice")
thelabel9=tk.Label(root,text="9,Sama Cola CSD")
thelabel10=tk.Label(root,text="10,Sama Lemon CSD")
thelabel11=tk.Label(root,text="11,Sama Orange CSD")
thelabel12=tk.Label(root,text="12,Sama fruit CSD")
thelabel13=tk.Label(root,text="13,Raz Energy Drink")
thelabel1.pack()
thelabel2.pack()
thelabel3.pack()
thelabel4.pack()
thelabel5.pack()
thelabel6.pack()
thelabel7.pack()
thelabel8.pack()
thelabel9.pack()
thelabel10.pack()
thelabel11.pack()
thelabel12.pack()
thelabel13.pack()
root.mainloop()
class ProductCheck:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Check Page")
        title = tk.Label(self.root, text="Enter ProductId:")
        title.grid(row=0, column=0)
        self.title1 = tk.Entry(self.root)
        self.title1.grid(row=0, column=1)
        button1 = tk.Button(self.root, text="Search", command=self.Product)
        button1.grid(row=1, column=1)
        self.result = tk.Label(self.root, text="")
        self.result.grid(row=2, columnspan=2)
        self.total_price = 0
        self.products = {}
    def run(self):
        self.root.mainloop()
    def Product(self):
        wantedProduct = self.title1.get()
        foundProduct = []
        with open("Product.txt", "r") as file:
            for line in file:
                products = line.strip().split(",")
                title = products[0].strip() or products[1].strip()
                price = float(products[2].strip())
                if wantedProduct == title:
                    foundProduct.append((title,price))
                    self.products[title]=price
        if foundProduct:
            self.result.config(text="The Product in")
        else:
            self.result.config(text="The Product is not in")

    def calculate_total(self):
        total = 0
        for price in self.products.values():
            total += price
        return total

class Checkprice:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Check Page")
        title2 = tk.Label(self.root, text="The Total Price is:")
        title2.grid(row=0, column=0)
        self.total_label=tk.Label(self.root,text="")
        self.total_label.grid(row=0,column=1)
        button2 = tk.Button(self.root, text="Total Price", command=self.show_total)
        button2.grid(row=2, column=1)

    def run2(self):
        self.root.mainloop()
    def calculate_total(self):
        with open("Product.txt", "r") as file:
            total = 0
            for line in file:
                _, _, price = line.strip().split(',')
                total += float(price)
            return total
    def show_total(self):
        total =self.calculate_total()
        self.total_price = total
        self.total_label.config(text=f"The Total Price is: {total}")

Product_Check =ProductCheck()
Product_Check.run()
price_Check = Checkprice()
price_Check.run2()

def feedback():
    feedback = feedback_entry.get()
    print("Feedback received:", feedback)
    myfile = open("Feedback.txt","a")
    str1 = "\n" + feedback + ",end"
    myfile.write(str1)
    lolo =tk.Tk()

    lolo.mainloop()

    feedback_entry.delete(0,END)

window =tk.Tk()
window.title("Feedback Form")

feedback_label =tk.Label(window, text="Enter your feedback:")
feedback_label.pack()

feedback_entry =tk.Entry(window, width=50)
feedback_entry.pack()

submit_button =tk.Button(window, text="Submit Feedback", command=feedback)
submit_button.pack()

feedback_label =tk.Label(window, text="Thank you for visiting")
feedback_label.pack()

window.mainloop()