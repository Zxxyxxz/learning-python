import sys
#prints the argumetns that added while running thisfile
print(sys.argv)

# print the system version
print(sys.version)
print("\n")
# print the list of directories where the python looks for modules
print(sys.modules)
print("\n")

# now we access a specific module 
print(sys.modules['os'])

#  check if a module is loaded
if "math" in sys.modules:
    print("math is in the sys modules")
else:
    print("it is not loaded")


# loading or force loading a module
if "random" not in sys.modules:
    print("random module is not loaded we are foce loading it ")
    import random
else:
    print("the random module is already loaded")


print("please enter something ___")
ina=sys.stdin.read()
# sys.quit(0)
print("you have entered"+ina)
sys.stdout.write("hi")           