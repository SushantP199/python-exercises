class Phone:
    "A simple class for test"
    phone_version = "S10"
    brand_name = "Samsung"
    user_name = " "

    # model = "S10+"
    def get_model(self):
        # return self.model
        return "S10+"

    # def set_model(self, val):
    #     self.model = "S10+ ,"+ val

    # constructor
    def __init__(self, user_name):
        self.user_name = user_name

    def BootLogo(self):
        print("SAMSUNG",self.phone_version)

sushant = Phone("sushant")

# sushant.phone_version = "iPhone X"
# sushant.set_model("iPhone")

print(sushant.get_model())
sushant.BootLogo()

print(sushant.__doc__)