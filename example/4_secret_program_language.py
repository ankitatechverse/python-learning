# Write a python program to translate a message into secret code language. Use the rules below
# to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it at the start

input_message = input("Enter the message: ")

def encode_word(word):
  if len(word) < 3:
    return word[::-1]  # Reverse the string
  else:
    first_letter = word[0]
    encoded_word = word[1:] + first_letter  # Move first letter to the end
    # Append three random characters at the start and end
    random_chars_start = "xyz"
    random_chars_end = "abc"    
    return random_chars_start + encoded_word + random_chars_end
  
def decode_word(word):
  if len(word) < 3:
    return word[::-1]  # Reverse the string
  else:
    # Remove three random characters from start and end
    word = word[3:-3]
    last_letter = word[-1]
    decoded_word = last_letter + word[:-1]  # Move last letter to the start
    return decoded_word
  
a = encode_word(input_message)
print("Encoded message:", a)
b = decode_word(a)
print("Decoded message:", b)
