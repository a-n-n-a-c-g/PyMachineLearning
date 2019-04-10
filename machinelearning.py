import passwordmeter
import os, glob, shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def getTokens(inputString):
    tokens = []
    for i in inputString:
        tokens.append(i)
    return tokens

def main():
    CodedPasswords = []
    file = open("Shortpws.txt", "r")
    #line = file.readline()
    for line in file:
        #print "crap"
        TSS = []
        #line = file.readline()
        cnt = 0 
        #while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        strength, improvements = passwordmeter.test(line)
        #print(int (strength*100))
        #print(cnt)
            #print("Strength: ".strenth)
        cnt += 1
        TSS.append(line)
        TSS.append(strength)
        CodedPasswords.append(TSS)
    print(CodedPasswords)

if __name__ == "__main__":
   main()
