alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_len = len(alphabet)

def decode_message(message, offset, shift):
  result = ""
  chars = []
  # iterate through message, shift (L/R) each char index in ALPHABET by offset
  for letter in message:
    if letter not in alphabet: # add whitespaces/non char
      chars.append(letter)
      continue

    if shift == 'LEFT':
      # check if index needs to wrap around
      if (alphabet.index(letter) - offset) <= 0:
        chars.append(alphabet[alphabet_len - ((alphabet.index(letter) + offset) % 
        alphabet_len)])
       # offset index leftward 
      else: chars.append(alphabet[alphabet.index(letter) - offset])

    if shift == 'RIGHT':
      # check if index needs to wrap around
      if (alphabet.index(letter) + offset) >= alphabet_len: 
        chars.append(alphabet[((alphabet.index(letter) + offset) % alphabet_len)]) 
      # offset index rightward
      else: 
        chars.append(alphabet[alphabet.index(letter) + (offset)]) 
  result = ''.join(chars)
  return result


def encode_message(message, offset, shift):
  result = ""
  chars = []
  letter_index = 0

  for letter in message:

    if letter not in alphabet:
      chars.append(letter)
      continue

    letter_index = alphabet.index(letter)
    if shift == 'LEFT':
      if letter_index - offset <= 0:
        chars.append( 
          alphabet[alphabet_len + (letter_index - offset)]
        )
      else: chars.append(alphabet[letter_index - offset])

    if shift == 'RIGHT':
      if letter_index + offset >= alphabet_len:
        chars.append(
          alphabet[(letter_index + offset) % alphabet_len]
        )
      else: chars.append(alphabet[letter_index + offset])
          

  result = ''.join(chars)
  return result


message = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je 
tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"""
offset = 10
shift = 'RIGHT'

decoded_message = decode_message(message, offset, shift)
print("message recieved:", decoded_message, "\n")

send = "hey there pal"
offset = 10
encoded = encode_message(send, offset, shift)
print("Sending:", encoded, "(", decode_message(encoded, offset, 'RIGHT'), ")")

message_in = """jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."""
offset = 10
shift= 'RIGHT'
decoded = decode_message(message_in ,offset, shift)
print("\nDecoded message:", decoded)

message_in = """bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue 
qhqz yadq eqogdq!"""
offset = 14
shift = 'RIGHT'
print("\nDecoded message:", decode_message(message_in, offset, shift))