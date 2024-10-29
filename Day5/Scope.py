# Local scope
def car():
    x = 300 
    print(x)
car() # x isnt available outside a function

# Function inside a function 
def honda():
    spare = 500 #varible used inside nexted function
    def steering():
        print(spare)
    
    steering()
honda()

# Global keyword
def kawasiki():
    global brand
    brand = 690
    print(brand)

kawasiki()
print(brand)

# Non local keyword - to use variable on nexted parent fucntion

def drive():
    trip = "ooty"

    def sail():
        nonlocal trip
        trip = "sri lanka"

    sail()

    return trip

print(drive())