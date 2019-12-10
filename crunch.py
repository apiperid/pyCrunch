import sys
import itertools

def checkInput(length,updateStep):
    if length<=0:
        print("The generated passwords must have length > 0")
        return -1
    if updateStep<=0:
        print("The update step must be > 0")
        return -1

def generate(length,charset,outputFile,updateStep):
    print("Generated Passwords : "+ str(len(charset)**length))
    KB = ((len(charset)**length)*5)/1024
    print("File Size (KB) : "+str(float("%.4f" % KB)));
    MB = KB/1024
    print("File Size (MB) : "+str(float("%.4f" % MB)));
    GB = MB/1024
    print("File Size (GB) : "+str(float("%.4f" % GB)));
    TB = GB/1024
    print("File Size (TB) : "+str(float("%.4f" % TB)));

    enter = input("\nPress Enter If You Want To Continue")

    updates = 0
    generatedPasswords = 0
    file = open(outputFile+".txt","a")
    for password in itertools.product(charset,repeat=length):
        file.write("%s\n" % ''.join(password))
        generatedPasswords += 1
        if generatedPasswords == updateStep:
            updates += 1
            print(str(generatedPasswords*updates)+"/"+str(len(charset)**length))
            generatedPasswords = 0
    file.close()
    print(str(len(charset)**length)+"/"+str(len(charset)**length))
    print("Generation Finished")


if __name__=="__main__":
    if len(sys.argv)!=5 :
        print("The arguments must be exactly 5")
    else:
        if checkInput(int(sys.argv[1]),int(sys.argv[4]))!=-1:
            generate(int(sys.argv[1]),sys.argv[2],sys.argv[3],int(sys.argv[4]))
    
