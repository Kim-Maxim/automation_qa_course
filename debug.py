# data1 = ['Desktop', 'Private']
# data2 = ['desktop', 'private']

# print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())
# print(data2)

# data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
# data2 = str(data2).replace(' ','').lower()

# assert data1 == data2
data1 = rf"C:\Users\kimma\github\automation_qa_course\filetest701.txt"
data2 = rf"C:\fakepath\filetest701.txt"

print(data1.split('\\')[-1])
print(data2.split('\\')[-1])

assert data1.split('\\')[-1] == data2.split('\\')[-1] 