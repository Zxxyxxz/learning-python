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
if user_input_verify.strip() == 'q':
    print(f"the system failed to aquire the right inpiuts so we are exiting with the call of exit in the sys module sys.exit()")
    sys.exit(1)
else:
    print(f"nice that the system was succesful in the proces if aquirign using the sys module")
    
print(f"""now we can proceed with stdout
      \n ok now we will try the sys.strdout.write comand\n
      """)
print(sys.stdout.write(f"\n hey do you see. this mesage{"wo "*5}"))
print(f"now you are probably wondering why there is a nuber right it is because the two thiungs being happened it steraming the string bundle to screen and since it is wrapped aptuna. print statemnt the ...write returns the total chars it writes so that also i s printed \n so the wirte usage would be out tof the print wrapper")
sys.stdout.write(f"now do oyu see any numbers?\n")

sys.stdout.write(f"""no right o the thing is that our sys.stdout determines where to flush the stream
                 \n so lets see our current sys.stdout():{sys.stdout}
                 
                 """)
# now we are taking pause on sys exploriung back to main project of the cahtbot learning we wil continenue on sys and flushing out on a file and so on next 
