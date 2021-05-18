alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# #encrypt function
# def encrypt(text,shift):
#   newtext = []
#   for i in text:
#     if alphabet.index(i)+shift <= alphabet.index('z'):
#       newtext.append(alphabet[alphabet.index(i)+shift])
#     elif alphabet.index(i)+shift > alphabet.index('z'):#incase the index+shift amount is greater than the lenght of the list
#       newtext.append(alphabet[shift-(alphabet.index('z')-alphabet.index(i))-1])

#   print (''.join(newtext))
# #decrypt function
# def decrypt(text,shift):
#   newtext = []
#   for i in text:
#     newtext.append(alphabet[alphabet.index(i)-shift])
#   print(''.join(newtext))
# #select encode or decode
# if direction == 'encode':
#   encrypt(text,shift)
# elif direction == 'decode':
#   decrypt(text,shift)
# else:
#   print('please type the correct text for selection')

def caesar(text,shift,direction):
  newtext = []
  for char in text:
    if direction == 'encode':
      if alphabet.index(char)+shift <= alphabet.index('z'):
        newtext.append(alphabet[alphabet.index(char)+shift])
      elif alphabet.index(char)+shift > alphabet.index('z'):#incase the index+shift amount is greater than the lenght of the list
        newtext.append(alphabet[shift-(alphabet.index('z')-alphabet.index(char))-1])
    if direction == 'decode':
      newtext.append(alphabet[alphabet.index(char)-shift])
  result = ''.join(newtext)    
  print(f'your {direction}new string is {result}')

caesar(text,shift,direction)

