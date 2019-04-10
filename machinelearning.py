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
    PWs = []
    STRENGTHs = []
    file = open("Shortpws.txt", "r")
    for line in file:
        line=line.rstrip("\n")
        TSS = []
        cnt = 0 
        strength, improvements = passwordmeter.test(line)
        cnt += 1
        TSS.append(line)
        PWs.append(line)
        TSS.append(strength*100)
        STRENGTHs.append(int(round(strength*100)))
       # TSS.append(strength)
        CodedPasswords.append(TSS)
    print(CodedPasswords)
    vectorizer = TfidfVectorizer(tokenizer=getTokens)
    X = vectorizer.fit_transform(PWs)
    X_train, X_test, y_train, y_test = train_test_split(X, STRENGTHs,
            test_size=0.20, random_state=42)
    lgs = LogisticRegression(penalty='l2',multi_class='ovr')
    lgs.fit(X_train, y_train)
    print(lgs.score(X_test, y_test))

if __name__ == "__main__":
   main()
