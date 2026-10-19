


password = input("Create a password, use at least 8 characters: ")

#---------------------------------------------------------------------------

def check_password(password):

 character_count = len(password)

 if character_count >=8:
        message = "Success! Your password has been created"
 else:
        message = "Your password is too short . Please use at least 8 characters"


 return message

#-----------------------------------------------------------------------------------------
result = check_password(password)
print(result)

input("Press enter to exit...")

