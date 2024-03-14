zip_code = input("enter your zip code:  ")
a = len(zip_code)

if a == 5 and zip_code.isdigit():
    print("your entry is valid")
else:
    print("Please enter a valid entry")



while True:
  zip_code = input("Please enter a zip code: ")
  z_1 = len(zip_code.strip())
  z_2 = zip_code.isdigit()


  if  z_1 == 5 and z_2 == True:
     print(" your entry is valid")
     break
  else:
     print("please enter a valid zip code")