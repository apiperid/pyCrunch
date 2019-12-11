import sys
import itertools


def checkInput(passwords,updateStep):
    if passwords <= 0:
        print("The generated passwords must be > 0")
        return -1
    if updateStep <= 0:
        print("The update step must be > 0")
        return -1

def generate(charset,outputFile,firstPassword,passwords,updateStep):
    length = len(firstPassword)
    print("Generated passwords : "+str(passwords))
    KB = (passwords*5)/1024
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
    startGenerating = False
    totalPasswords = passwords
    file = open(outputFile+".txt","a")
    for password in itertools.product(charset,repeat=length):
        password = ''.join(password)
        if startGenerating == True:
            file.write("%s\n" % password)
            generatedPasswords += 1
            passwords -= 1
            if passwords == 0:
                break
            if generatedPasswords == updateStep:
                updates += 1
                print(str(generatedPasswords*updates)+"/"+str(totalPasswords))
                generatedPasswords = 0
        # this if is here because we dont count the password you gave us
        # passwords will be generated after your given password
        if password == firstPassword:
            startGenerating = True
    file.close()
    print("Generation Finished")
    

if __name__ == "__main__":
    # first arg is the charset
    # second arg is the output file
    # third arg is the first password
    # forth arg is the number of password will be generated
    # fifth arg is the update step
    if len(sys.argv)!= 6:
        print("The arguments must be exactly 6")
    else:
        if checkInput(int(sys.argv[4]),int(sys.argv[5]))!=-1:
            generate(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5]))
