print("------------------------------")
print("Traffic Fine Management System")
print("------------------------------")

# User Input
vehicle_num=input("Enter the Vehicle Number: ")
driver_name=input("Enter Vehicle Driver Name: ")
speed=int(input("Enter Speed: "))
helmet_seatbelt=input("Has helmet/seatbelt (yes/no): ")
license_valid=input("Has license Valid (yes/no): ")

fine = 0

# Speed Checking
if speed <= 60:
    print("No Overspeeding of Rule Violation")
elif speed <= 80:
    print("Your Vehicle has Crossed the Speed Limit -> Fine Is ₹500")
    fine += 500
elif speed <= 100:
    print("Your Vehicle has Crossed the Speed Limit -> Fine Is ₹1000")
    fine += 1000
else:
    print("Your Vehicle is Over Speeding -> Fine Is ₹2000)")
    fine += 2000

# License checking
if license_valid == "no":
    print("Your License is Not Valid -> Fine Is ₹1500")
    fine += 1500
else:
    print("Your License is Valid")

# Helmet and Seatbelt checking
if helmet_seatbelt == "no":
    print("No Helmet or Seatbelt Detected (Fine ₹1000)")
    fine += 1000
else:
    print("Helmet and Seatbelt Worn Properly")

# Final fine 
print("-----------------------------------")
print(f"Total Fine is ₹{fine}")

if fine > 0:
    print("Status: Pay the Fine Immediately")
    print("Warning: Please drive safely!")
else:
    print("Status: No Fine — Drive Safely ")
print("-----------------------------------")