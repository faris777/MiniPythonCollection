#reversing the message
message = input('enter a message want reverse \n')

l = len(message)-1

m = ''
for i in range(l,-1,-1):
    m += message[i]

print(m)
