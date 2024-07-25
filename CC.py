def encrypt(plaintxt,shift):
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
    return pt
def decrypt(ciphertxt,shift):
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
    return ct
print("Welcome to the Caesar Cipher\nPlease Select to either encrypt or decrypt the data\n")
while True:
 print("Press '1' for Encryption")
 print("Press '2' for Decryption")
 print("Press '3' to Quit")
 choice = int(input("Enter your choice: "))
 
 if (choice == 1):
     plaintxt = input("Enter a plain text to encrypt\n")
     shift = int(input("Enter the shift number\n"))
     encrypted_text = encrypt(plaintxt,shift)
     print(f"Encrypted Text: {encrypted_text}")

 elif(choice == 2):
    ciphertxt = input("Enter the cipher text to decrypt\n")
    shift = int(input("Enter the shift number\n"))
    decrypted_text = decrypt(ciphertxt,shift)
    print(f"Decrypted Text: {decrypted_text}")
 
 elif(choice == 3):
     print("Exiting the Program, Goodbye :D")
     break
 else:
     print("Invalid Choice: Please select 1,2, or 3")
