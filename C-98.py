def countWordsfromfile():
    filename=input("Enter the file name : ")
    file=open(filename,"r")
   
    numberofwords=0
    charCount=0
    for line in file:
        charCount+=1
        words=line.split()
        numberofwords=numberofwords+len(words)
    
    print(numberofwords)
    print(charCount)
countWordsfromfile()
        