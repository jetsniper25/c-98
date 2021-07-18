def countWordsfromfile():
    filename=input("Enter the file name : ")
    file=open(filename,"r")
   
    numberofwords=0
    charCount=0
    for f in file:
        charCount+=1
    
    print(numberofwords)
    print(charCount)
countWordsfromfile()