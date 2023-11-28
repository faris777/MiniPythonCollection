import re
with open('lorem.txt','r') as file:
    readed = file.read()
    mat = re.findall(r'[I]',readed)
    mat1 = re.search(r'\bt\b',readed)
print(mat)
print(mat1)
