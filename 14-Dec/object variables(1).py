class Myclass:
    variable = "blah"

    def function(self):
        print("THis is amessage inside the class.")

myobjectx = Myclass()
myobjecty = Myclass()

myobjecty.variable = "yackity"

#print both values
print(myobjectx.variable)
print(myobjecty.variable)
