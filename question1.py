import os

#User input for shift values
shiftInput1 = input("Enter shift1 value: ")
shiftInput2 = input("Enter shift2 value: ")

def encrypt(shift1, shift2):
    #Alphabet
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    message = ""

    #Converting to integer
    shift1Int = int(shift1)
    shift2Int = int(shift2)

    with open('raw_text.txt') as f: 
        for line in f:
            for char in line:
                pos1 = lowercase.find(char)
                pos2 = uppercase.find(char)
            
                #If character is found in lowercase alphabet.. we use -1 because 0=a, meaning that 0 is the start of the alphabet
                if pos1 > -1:
                
                    #Character is in a - m
                    if 'a' <= char <= 'm':                
                        newPos1 = pos1 + (shift1Int*shift2Int)
                        #If new value is greater than the length of alphabet, we need to add its remainder from the start to prevent string index out of range
                        if newPos1 >= len(lowercase):
                            remaining = newPos1 % len(lowercase)
                            message += lowercase[remaining]
                        elif newPos1 <= len(lowercase):
                            message += lowercase[newPos1]
                        
                    #Character is in n - z      
                    elif 'n' <= char <= 'z':
                        newPos1 = pos1 - (shift1Int*shift2Int)
                        if newPos1 >= len(lowercase):
                            remaining = newPos1 % len(lowercase)
                            message += lowercase[remaining]
                        elif newPos1 <= len(lowercase):
                            message += lowercase[newPos1]
                        
                elif pos2 > -1:
                    
                    #Character is in A - M
                    if 'A' <= char <= 'M':
                        newPos2 = pos2 - shift1Int
                        #Using remainder to prevent string index out of range
                        if newPos2 < 0:
                            remaining = newPos2 % len(uppercase)
                            message += uppercase[remaining]
                        else:
                            message += uppercase[newPos2]
                    
                    #Character is in N - Z
                    if 'N' <= char <= 'Z':
                        newPos2 = pos2 + (shift2Int*shift2Int)
                        #Using remainder to prevent string index out of range
                        if newPos2 >= len(uppercase):
                            remaining = newPos2 % len(uppercase)
                            message += uppercase[remaining]
                        elif newPos2 <= len(uppercase):
                            message += uppercase[newPos2]
                
                #To keep the spaces/other characters like grammar, this else statement adds characters that don't need to be encrypted.
                else:
                    message+=char
                    
    #Adding encrypted text to the file 'encrypted_text.txt'
    e = open("encrypted_text.txt", 'a')   
    e.write(message)
    e.close() 
    
#Decrypt is the exact same code, except it is modified so that the positions are reversed, so we can decrypt.
def decrypt(shift1, shift2):
    #Alphabet
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    message = ""

    #Converting to integer
    shift1Int = int(shift1)
    shift2Int = int(shift2)

    #Reads from 'encrypted_text.txt'
    with open('encrypted_text.txt') as f: 
        for line in f:
            for char in line:
                pos1 = lowercase.find(char)
                pos2 = uppercase.find(char)
            
            #If character is found in lowercase alphabet.. we use -1 because 0=a, meaning that 0 is the start of the alphabet
                if pos1 > -1:
                
                    #Character is in a - m
                    if 'a' <= char <= 'm':                
                        newPos1 = pos1 - (shift1Int*shift2Int)
                        #If new value is greater than the length of alphabet, we need to add its remainder from the start to prevent string index out of range
                        if newPos1 >= len(lowercase):
                            remaining = newPos1 % len(lowercase)
                            message += lowercase[remaining]
                        elif newPos1 <= len(lowercase):
                            message += lowercase[newPos1]
                        
                    #Character is in n - z      
                    elif 'n' <= char <= 'z':
                        newPos1 = pos1 + (shift1Int*shift2Int)
                        if newPos1 >= len(lowercase):
                            remaining = newPos1 % len(lowercase)
                            message += lowercase[remaining]
                        elif newPos1 <= len(lowercase):
                            message += lowercase[newPos1]
                        
                elif pos2 > -1:
                    
                    #Character is in A - M
                    if 'A' <= char <= 'M':
                        newPos2 = pos2 + shift1Int
                        #Using remainder to prevent string index out of range
                        if newPos2 < 0:
                            remaining = newPos2 % len(uppercase)
                            message += uppercase[remaining]
                        else:
                            message += uppercase[newPos2]
                    
                    #Character is in N - Z
                    if 'N' <= char <= 'Z':
                        newPos2 = pos2 - (shift2Int*shift2Int)
                        #Using remainder to prevent string index out of range
                        if newPos2 >= len(uppercase):
                            remaining = newPos2 % len(uppercase)
                            message += uppercase[remaining]
                        elif newPos2 <= len(uppercase):
                            message += uppercase[newPos2]
                
                #To keep the spaces/other characters like grammar, this else statement adds characters that don't need to be encrypted.
                else:
                    message+=char
                
                    
    #Adding encrypted text to the file 'decrypted_text.txt'
    e = open("decrypted_text.txt", 'a')   
    e.write(message)
    e.close() 
    
encrypt(shiftInput1, shiftInput2)
decrypt(shiftInput1, shiftInput2)
                            
