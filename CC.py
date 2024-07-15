while True:
    
    print("Welcome to the Caesar Cipher\nPlease Select to either encrypt or decrypt the data")
    print("Press '1' for Encryption")
    print("Press '2' for Decryption")
    print("Press '3' to Quit")

    option = int(input("Choose your option\n"))

    if(option == 1):
     print("You've chosen Encryption")
     plaintxt = input("Enter plain text to encrypt\n")
     shift = int(input("Enter the shift number for encryption\n"))
     pt = ""
     for char in plaintxt:
            if(char.isupper()):
               n = ord(char) - ord('A')
               newp = (n + shift) % 26 
               newc= newp + ord('A')
               pt += chr(newc)
            elif(char.islower()):
               n = ord(char) - ord('a')
               newp = (n + shift) % 26
               newc = newp + ord('a')
               pt += chr(newc)
            else: 
                pt += char
     print(pt)
                
    elif(option == 2):
     print("You've chosen Decryption")
     ciphertxt = (input("Enter Cipher text to decrypt\n"))
     shift = int(input("Enter the shift number for decryption\n"))
     ct = ""
     for char in ciphertxt:
        if(char.isupper()):
            n = ord(char) - ord("A")
            newp = (n - shift) % 26
            newc = newp + ord("A")
            ct += chr(newc)
        elif(char.islower()):
            n = ord(char) - ord("a")
            newp = (n - shift) % 26
            newc = newp + ord("a")
            ct += chr(newc)
        else:
            ct += char
     print(ct)
    
    elif(option == 3):
     print("Goodbye! :D")
     break
    else:
     print("Invalid Input")  
 
