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
<<<<<<< HEAD
    #line = file.readline()
=======
>>>>>>> a36cb46d67e50870c0a3cc4d584fec4273ff3982
    for line in file:
        line=line.rstrip("\n")
        TSS = []
        cnt = 0 
        strength, improvements = passwordmeter.test(line)
        cnt += 1
        TSS.append(line)
        TSS.append(strength*100)
       # TSS.append(strength)
        CodedPasswords.append(TSS)
    print(CodedPasswords)

if __name__ == "__main__":
   main()
