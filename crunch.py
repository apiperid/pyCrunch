import sys
import itertools


def checkInput(length):
    if length<=0:
        print("The generated passwords must have length > 0")
        return -1

def generate(length,charset,outputFile):
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
    
    file = open(outputFile+".txt","a")
    for password in itertools.product(charset,repeat=length):
        file.write("%s\n" % ''.join(password))
    file.close()
    print("Generation Finished")


if __name__=="__main__":
    if len(sys.argv)!=4 :
        print("The arguments must be exactly 4")
    else:
        if checkInput(int(sys.argv[1]))!=-1:
            generate(int(sys.argv[1]),sys.argv[2],sys.argv[3])
    
