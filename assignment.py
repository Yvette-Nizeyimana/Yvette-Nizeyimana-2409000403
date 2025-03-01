# -*- coding: utf-8 -*-
"""Assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bPhwHoYXGGsNJuk6WKsa-nRxy20Ma3br
"""

from cryptography.fernet import Fernet

# Generate a new Fernet key
key= Fernet.generate_key()

#create a Fernet instance using the generated key
fernet = Fernet(key)

message1 = "MY FULL NAME"
message2 = "Yvette Nizeyimana"

# Encrypt message1 using the Fernet instance
encrypted_message1 = fernet.encrypt(message1.encode()) #Encode message

# Decrypt message1 using the Fernet instance
decrypted_message1 = fernet.encrypt(encrypted_message1)

#  Encrypt message2 using the Fernet instance
encrypted_message1 = fernet.encrypt(message2.encode()) #Encode message

#Decrypt message2= using the Fernet instance
decrypted_message2 = fernet.decrypt(encrypted_message1)


# Print the decrypted message
print(decrypted_message1.decode()) # Decode back to string

#Print the decrypted message
print(decrypted_message2.decode()) # Decode back to string