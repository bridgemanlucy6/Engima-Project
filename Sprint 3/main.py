def main():
  
  # reading text file
  message = ""
  file = open("Sprint 3\message.txt", "rt")
  for x in file:
    message += x
  file.close()
  message = message.upper()
  mList = list(message)

  
  # checking if characters are letters and adding them into a string
  text = ""
  for i in range(len(mList)):
      if ord(mList[i])-65 > 0 and ord(mList[i])-65 < 25:
          text += mList[i]

        
  # taking ludendorff key and encrypting message with the cipher
  lKey = input("Please enter Ludendorff key: \n")

  
  #enigSettings[] = numberSettings()
  #ludendorffEncrypt(text,lKey)
  #miniEnigma(text,enigSettings[])
  #bruteForce()


main()