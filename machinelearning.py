import passwordmeter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

CodedPasswords = []

#fp = open('passwords.txt', 'r')
with open('Shortpws.txt', 'r') as fp:
    TSS = []
    line = fp.readline()
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

#for password in CodedPasswords:
       #Strip \n

       #Get strength
       #strength, improvements = passwordmeter.test(password)
       
       #multiply strength by 100 and cast as int
       #int(strength)*=100

       #add pw and stregnth as a nested list to CodedPasswords
       #eg [07606374520,10]

