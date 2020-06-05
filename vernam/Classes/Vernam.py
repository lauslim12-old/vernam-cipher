from random import randint

# Because ASCII value for 'A' is 65, then reduce it by 65 to get 0 (for alphabet/numeric equivalent).
# Alphabet loop equals to 26, because the range from A - Z is just 26.
ALPHABET_EQUIVALENT = 65
ALPHABET_LOOP = 26

class VernamCipher:
  def __init__(self, plaintext = ''):
    self.__plaintext = plaintext
    self.__length = len(plaintext)
    self.__alphabet_equivalent = []
    self.__ciphertext_key = []
    self.__ciphertext_key_sum = []
    self.__ciphertext_array = []
    self.__ciphertext = []
    self.__ciphertext_decrypt = []
    self.__decrypted = []
    self.__debug_array = []

  # Utilities
  def transform_text(self):
    self.__plaintext = self.__plaintext.upper()
  
  def split_text(self):
    self.__plaintext = list(self.__plaintext)

  # Core Functions
  def alphabet_equivalent(self):
    self.__alphabet_equivalent = list(ord(i) - ALPHABET_EQUIVALENT for i in self.__plaintext)

  def generate_key(self):
    i = 0
    while i < self.__length:
      random_number = randint(0, 100)
      self.__ciphertext_key.append(random_number)
      i += 1

  def sum_array(self):
    self.__ciphertext_key_sum = list(sum(i) for i in zip(self.__ciphertext_key, self.__alphabet_equivalent))

  def fetch_ciphertext(self):
    for i in self.__ciphertext_key_sum:
      self.__ciphertext_array.append(i % ALPHABET_LOOP)
    
    for i in self.__ciphertext_array:
      self.__ciphertext.append(chr(i + ALPHABET_EQUIVALENT))

  def decrypt_ciphertext(self):
    # Actual key is to modulo the ciphertext key variable by 26. This is important if you want to be able to decrypt.
    # The only variables that we are using is the ciphertext, and its key. We do not use other variables!
    for i, j in zip(self.__ciphertext_array, self.__ciphertext_key):
      x = i - (j % ALPHABET_LOOP)
      
      if x < 0:
        x += ALPHABET_LOOP
      
      self.__ciphertext_decrypt.append(x)

  # In case, this is the real key (debug function). But we do not call it in the main function. 
  # The only function used is the function above this one.
  def get_real_cipher_key(self):
    for i in self.__ciphertext_key:
      x = i % ALPHABET_LOOP

      if x < 0:
        x += ALPHABET_LOOP
      
      self.__debug_array.append(chr(x + ALPHABET_EQUIVALENT))
  
  def convert_decrypted(self):
    for i in self.__ciphertext_decrypt:
      self.__decrypted.append(chr(i + ALPHABET_EQUIVALENT))
    
  # Setters
  def set_ciphertext(self, ciphertext):
    ciphertext = list(ciphertext.upper())
    self.__ciphertext_array = list(ord(i) - ALPHABET_EQUIVALENT for i in ciphertext)
  
  def set_key(self, key):
    self.__ciphertext_key = list(ord(i) - ALPHABET_EQUIVALENT for i in key)

  # Getters
  def get_plaintext(self):
    return ''.join(self.__plaintext)

  def get_alphabet_equivalent(self):
    return ', '.join(map(str, self.__alphabet_equivalent))

  def get_ciphertext_num_equivalent(self):
    return ', '.join(map(str, self.__ciphertext_array))

  def get_key(self):
    return ', '.join(map(str, self.__ciphertext_key))

  def get_sum_key(self):
    return ', '.join(map(str, self.__ciphertext_key_sum))

  def translate_ciphertext(self):
    return ''.join(self.__ciphertext)

  def get_decrypted_message(self):
    return ''.join(self.__decrypted)

  def get_debug_array(self):
    return ''.join(self.__debug_array)