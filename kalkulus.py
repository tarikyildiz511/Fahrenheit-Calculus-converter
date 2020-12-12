print("-"*30)
print("1- kalkülüs")
print("2-fahrenheit")

seçim = int(input("1/2?"))
if seçim ==1:
    print("\n celsius to  fahrenheit") 
    celsius = float(input("Derece girin"))
    fahrenheit = (celsius*1.8)+32
    print(f"{celsius}kalkulus{fahrenheit}")
elif seçim ==2:
    print("\n fahrenheit to celsius") 
    fahrenheit = float(input("Derece girin"))
    celsius = (fahrenheit-32) /1.8
    print(f"{fahrenheit}, to {celsius}")

print("-"*30)
print("1-celsius")
print("2-fahrenheit")
secim = int(input("1/2"))


