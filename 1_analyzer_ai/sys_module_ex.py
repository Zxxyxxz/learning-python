import sys
#prints the argumetns that added while running thisfile
print(sys.argv)

# print the system version
print(sys.version)
print("\n")
# print the list of directories where the python looks for modules
print(sys.modules)
print(f"{"\n."*100}")

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



# now we are playing with the stdin and stdout

# we can read from stdin these 2 variations are just kinda the same
print(f"lets request some input with the commands form the sys module and ex we ar using\n  sys.stdin.readline() with the input() so you gotta enter twice the same or dif things")
user_input= sys.stdin.readline()
user_input_2= input()
print(f"the first time variation retrieves the innupt as {user_input} and the secnond nput is {user_input_2}{"\n"*5} if oyu see that it got wrong please enter q if correct just proceed")
user_input_verify = sys.stdin.readline()
if user_input_verify == 'q':
    print(f"the system failed to aquire the right inpiuts so we are exiting with the call of exit in the sys module sys.exit()")
    sys.exit(1)
else:
    print(f"nice that the system was succesful in the proces if aquirign using the sys module")
    
print(f"now we can proceed with stdout")

