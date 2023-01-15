# machines original settings for each component
plugSettings = [19,18,2,4,3,12,6,7,17,9,13,25,5,10,22,21,16,8,1,0,20,15,14,24,23,11]
rotorIsettings = [4,9,10,2,7,1,23,9,13,16,3,8,2,9,10,18,7,3,0,22,6,13,5,20,4,10]
rotorIIsettings = [0,8,1,7,14,3,11,13,15,18,1,22,10,6,24,13,0,15,7,20,21,3,9,24,16,5]
rotorIIIsettings = [1,2,3,4,5,6,22,8,9,10,13,10,13,0,10,15,18,5,14,7,16,17,24,21,18,15]
reflectorSettings = [4,9,12,25,0,11,24,23,21,1,22,5,2,17,16,20,14,13,19,18,15,8,10,7,6,3]
rotorIposition0 = 0
rotorIIposition0 = 0

def main():

  # takes message and turns it into a character array with uppercase letters
  message = ""
  message = readFile(message)
  message = message.upper()
  encrypted = ""
  text = list(message)

  # checks to see which characters are letters, whatever is a letter is sent through functions and if not it is just added to the final message outputted
  for i in range(len(text)):
    a = ord(text[i])-65
    if a > -1 and a < 26:
      a = control(a)
    letter = (chr)(a + 65)
    encrypted += letter

  # prints final message
  print("Encrypted message:",encrypted)

def readFile(message):

  #reads the text file and puts it into a string to send to the main function
  file = open("Sprint 2\message.txt", "rt")
  for x in file:
    message += x
  file.close()
  return message

def control(a):

  #takes letters through functions in the correct order
  a = plugboard(a)
  a = rotorI(a)
  a = rotorII(a)
  a = rotorIII(a)
  a = reflector(a)
  a = rotorIIIreverse(a)
  a = rotorIIreverse(a)
  a = rotorIreverse(a)
  a = plugboard(a)
  rotorReset()

  return a

def plugboard(a):

  # if a letter is paired up to another in the original settings, they will be switched here using the array
  a = plugSettings[a]
  return a

def rotorI(a):

  # maps letters depending on the rotor setings
  a = (a + rotorIsettings[a])%26
  return a

def rotorII(a):

  # maps letters depending on the rotor setings
  a = (a + rotorIIsettings[a])%26
  return a

def rotorIII(a):

  # maps letters depending on the rotor setings
  a = (a + rotorIIIsettings[a])%26
  return a

def reflector(a):

  # maps letter from third rotor to another letter depending on value in the array
  a = reflectorSettings[a]
  return a

def rotorIreverse(a):

  # loops through all possible alphabet values and takes them through the first rotor, if the output is equal to the value passed through it will return the value of the alphabet letter
  for i in range (26):
    x = rotorI(i)
    if x == a:
      return i

def rotorIIreverse(a):

  # loops through all possible alphabet values and takes them through the second rotor, if the output is equal to the value passed through it will return the value of the alphabet letter
  for i in range (26):
    x = rotorII(i)
    if x == a:
      return i

def rotorIIIreverse(a):

  # loops through all possible alphabet values and takes them through the third rotor, if the output is equal to the value passed through it will return the value of the alphabet letter
  for i in range (26):
    x = rotorIII(i)
    if x == a:
      return i

def rotorReset():

  global rotorIsettings
  global rotorIIsettings
  global rotorIIIsettings
  global rotorIposition0
  global rotorIIposition0

  # moves the first array down by one
  for i in range(26):
    temp = rotorIsettings[i]
    rotorIsettings[i] = rotorIsettings[0]
    rotorIsettings[0] = temp
  rotorIposition0 = (rotorIposition0 + 1)%26

  # checks if first rotor has moved down 26 times, if it has the second rotor moves down by one
  if rotorIposition0 == 0:
    for i in range(26):
      temp = rotorIIsettings[i]
      rotorIIsettings[i] = rotorIIsettings[0]
      rotorIIsettings[0] = temp
    rotorIIposition0 = (rotorIIposition0 + 1)%26

  # checks if second rotor has moved down 26 times, if it has the third rotor moves down by one
    if rotorIIposition0 == 0:
      for i in range(26):
        temp = rotorIIIsettings[i]
        rotorIIIsettings[i] = rotorIIIsettings[0]
        rotorIIIsettings[0] = temp

main()