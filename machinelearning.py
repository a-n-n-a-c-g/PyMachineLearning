import passwordmeter
import os, glob, shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    CodedPasswords = []
    file = open("Shortpws.txt", "r")
    for line in file:
        #print "crap"
        TSS = []
        line = file.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            strength, improvements = passwordmeter.test(line)
            print(int (strength*100))
            print(cnt)
            #print("Strength: ".strenth)
            cnt += 1
            TSS.append(line)
            TSS.append(strength)
            CodedPasswords.append(TSS)
    print(CodedPasswords)

if __name__ == "__main__":
   main()
