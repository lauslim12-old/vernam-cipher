#!/usr/bin/env python

"""
  Vernam Cipher / One Time Pad Gist for Encryption and Decryption
  For now, my cipher cannot encrypt numbers, and symbols, hence its prototype status.
  Paradigm is Object Oriented Programming
  It is not really safe to use this in production environment, as the random number generator used is not TRNG, but PRNG.
  Encryption:
  - Plaintext will be converted to alphabet equivalent numbers (A will be 0, B will be 1, etc)
  - There will be random number generation from 0 to 100 (as key).
  - Alphabet equivalent number and the key will be summed.
  - Modulo the result sum by 26.
  - Translate the numeric equivalent to alphabet equivalent. It will be the ciphertext.
  - Ciphertext is done.

  Decryption:
  - Subtract the ciphertext with the key. But before subtracting, modulo the key by 26. 
  - Convert the numbers back into alphabet equivalent numbers.
  - You're done.

  Have fun!
"""

__author__ = "Nicholas Dwiarto Wirasbawa"
__copyright__ = "Copyright 2020, Nicholas Dwiarto Wirasbawa"
__credits__ = "Nicholas Dwiarto Wirasbawa"

__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Nicholas Dwiarto Wirasbawa"
__email__ = "nicholasdwiarto@yahoo.com"
__status__ = "Prototype"

from Classes.Vernam import VernamCipher

# Menus
def main_menu():
  print("---------- One Time Pad Encryption ----------")
  print("1. Encrypt Message")
  print("2. Decrypt Message")
  print("3. Full-Stage Encrypt and Decrypt")

# Utilities for Main
def spacer():
  print("")

# Core Functions for Main
def encrypt_message(plaintext, key):
  obj = VernamCipher(plaintext)
  obj.set_key(key)
  
  obj.alphabet_equivalent()
  obj.sum_array()
  obj.fetch_ciphertext()

  print("Encrypted message: ", obj.translate_ciphertext())

def decrypt_message(ciphertext, key):
  obj = VernamCipher()

  obj.set_ciphertext(ciphertext)
  obj.set_key(key)

  obj.decrypt_ciphertext()
  obj.convert_decrypted()
  print("Decrypted message: ", obj.get_decrypted_message())
  
def full_run():
  # Feel free to change the text input here!
  cipher_object = VernamCipher("doctorsbelieveindonesiasweatherunfavorableforcoronavirus")
  cipher_object.transform_text()
  print("Plaintext: ", cipher_object.get_plaintext())

  cipher_object.split_text()
  cipher_object.alphabet_equivalent()
  print("Numeric Equivalent: ", cipher_object.get_alphabet_equivalent())
  
  # Actual key is to modulo the ciphertext key variable by 26. This is important if you want to be able to decrypt.
  # The only variables that we are using is the ciphertext, and its key. We do not use other variables!
  # See the method for more details.
  cipher_object.generate_key()
  print("Random Number (Key): ", cipher_object.get_key())
  
  cipher_object.sum_array()
  print("Sum: ", cipher_object.get_sum_key())
  
  cipher_object.fetch_ciphertext()
  print("Scaled down (mod 26): ", cipher_object.get_ciphertext_num_equivalent())
  print("Ciphertext: ", cipher_object.translate_ciphertext())
  
  cipher_object.decrypt_ciphertext()

  cipher_object.convert_decrypted()
  print("Decrypted: ", cipher_object.get_decrypted_message())

  # Debugging purposes
  cipher_object.get_real_cipher_key()
  print("True Key (already modulo'ed): ", cipher_object.get_debug_array())
  # Remove this line if successfully debugged.

def main():
  # Infinite loop for application-like script.
  while(True):
    main_menu()
    choice = int(input("Enter your desired menu: "))

    if(choice == 1):
      plaintext = input("Enter your desired plaintext: ")
      key = input("Input your key: ")
      encrypt_message(plaintext, key)
      spacer()
    elif(choice == 2):
      ciphertext = input("Enter your desired ciphertext: ")
      key = input("Input the key: ")
      decrypt_message(ciphertext, key)
      spacer()
    elif(choice == 3):
      full_run()
      spacer()
    else:
      print("Invalid input!")

if __name__ == "__main__":
  main()
