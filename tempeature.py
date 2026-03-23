import c_to_f 
import c_to_k 
import f_to_c 

print("welcome to our software to check temp reading in diff formats")
print()
print("enter 1 for converting celcius to fahrenite")
print()
print("enter 2 for converting celcius to kelvin")
print()
print("enter 3 for converting fahrenhite to celcius")
print()

option=int(input("enter your option"))

if option==1:
    temp=float(input("enter the tempeature you want to convert in fahrenite"))
    out=c_to_f.convert(temp)
    print(f"the temp {temp} in fahrenite is ",out)
elif option==2:
    temp=float(input("enter the tempeature you want to convert in kelvin"))
    out=c_to_k.convert(temp)
    print(f"the temp {temp} in kelvin is ",out)
elif option==3:
    temp=float(input("enter the tempeature you want to convert in celcius"))
    out=f_to_c.convert(temp)
    print(f"the temp {temp} in celcius is ",out)    
else:
    print("enter correct option for choosing degree of change")
