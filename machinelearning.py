import passwordmeter
import os, glob, shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    CodedPasswords = []
    file = open("passwords.txt", "r")
    for line in file:
        line.rstrip("\n");
        TSS = []
        cnt = 0 
        strength, improvements = passwordmeter.test(line)
        cnt += 1
        TSS.append(line)
        TSS.append(strength*100)
        CodedPasswords.append(TSS)
    print(CodedPasswords)

if __name__ == "__main__":
   main()
