# machines original settings for each component
plugSettings = [19,18,2,4,3,12,6,7,17,9,13,25,12,10,22,21,16,17,1,0,20,15,14,24,23,11]
rotorIsettings = [4,10,12,5,11,6,3,16,21,25,13,19,14,22,24,7,23,20,18,15,0,8,1,17,2,9]
rotorIIsettings = [0,9,3,10,18,8,17,20,23,1,11,7,22,19,12,2,16,6,25,13,15,24,5,21,14,4]
rotorIIIsettings = [1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14]
reflectorSettings = [4,9,12,25,0,11,24,23,21,1,22,5,2,17,16,20,14,13,19,18,15,8,10,7,6,3]
rIreset = False
rIIreset = False

def main():

  # takes message and turns it into a character array with uppercase letters
  message = input("Enter your message \n")
  message = message.upper()
  encrypted = ""
  text = list(message)

  # checks to see which is a letter, whatever is a letter is sent through functions
  for i in range(len(text)):
    a = ord(text[i])-65
    if a > -1 and a < 26:
      a = control(a)
    letter = (chr)(a + 65)
    encrypted += letter

  # prints final message
  print("Encrypted message:",encrypted)

def control(a):

  #takes letters through functions in the correct order
  a = plugboard(a)
  a = staticRotor(a)
  a = rotorI(a)
  a = rotorII(a,rIreset)
  a = rotorIII(a,rIIreset)
  a = reflector(a)
  a = rotorReverseIII(a)
  a = rotorReverseII(a)
  a = rotorReverseI(a)
  a = staticRotor(a)
  a = plugboard(a)

  return a

def plugboard(a):

  # if a letter is paired up to another in the original settings, they will be switched here using the array
  a = plugSettings[a]
  return a

def staticRotor(a):

  # makes the letter increase by one, e.g a becomes b
  a = (a+1)%26
  return a
  
def rotorI(a):

  global rIreset
  global rotorIsettings

  # maps letters depending on the rotor setings
  a = rotorIsettings[a]
  rotorIposition0 = 4
  
  # moves all array values down
  for i in range(26):
    temp = rotorIsettings[i]
    rotorIsettings[i] = rotorIsettings[0]
    rotorIsettings[0] = temp
    
  # checks to see if rotor is in original position
  if rotorIposition0 == rotorIsettings[0]:
    rIreset = True
  else:
    rIreset = False

  return a

def rotorII(a,rIreset):

  global rIIreset
  global rotorIIsettings

  # maps letters depending on the rotor setings
  a = rotorIIsettings[a]
  rotorIIposition0 = 0

  # moves all array values down if first rotor is in original position
  if rIreset:
    for i in range(26):
      temp = rotorIIsettings[i]
      rotorIIsettings[i] = rotorIIsettings[0]
      rotorIIsettings[0] = temp
    # checks to see if rotor is in original position 
    if rotorIIposition0 == rotorIIsettings[0]:
      rIIreset = True
    else:
      rIIreset = False
    
  return a

def rotorIII(a,rIIreset):

  global rotorIIIsettings

  # moves all array values down if second rotor is in original position
  if rIIreset:
    for i in range(26):
      temp = rotorIIIsettings[i]
      rotorIIIsettings[i] = rotorIIIsettings[0]
      rotorIIIsettings[0] = temp

  # maps letters depending on the rotor setings
  a = rotorIIIsettings[a]

  return a

def reflector(a):

  # maps letter from third rotor to another letter depending on value in the array
  a = reflectorSettings[a]
  return a

def rotorReverseIII(a):

  # gives the value of the index of a, does the backwards version of the rotor
  for i in range(26):
    if rotorIIIsettings[i] == a:
      a = i
      break

  return a

def rotorReverseII(a):

  # gives the value of the index of a, does the backwards version of the rotor
  for i in range(26):
    if rotorIIsettings[i] == a:
      a = i
      break

  return a

def rotorReverseI(a):

  # gives the value of the index of a, does the backwards version of the rotor
  for i in range(26):
    if rotorIsettings[i] == a:
      a = i
      break

  return a

main()