x = ('Masala', 'lemon','ginger')
y = enumerate(x)
# <enumerate object at 0x000001D39F979D50>

list(y)
# [(0, 'amit'), (1, 'raju'), (2, 'rohit')]

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

# The enumerate() function adds a counter as the key of the enumerate object.

# file Handeling 

file = open("file.txt","w")

try:
  file.write('what are you doing ')
finally:
  file.close() 

 # with Better Synatx 
with open('f1/txt','w') as file :
    file.write('its the better synatx ') 