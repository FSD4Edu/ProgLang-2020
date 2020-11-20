msg = "Good morning, "
def greetingfunc(name):
    greeting = msg + name + "!"
name = input("Your name?: ")
greetingfunc(name)
print(greeting)
