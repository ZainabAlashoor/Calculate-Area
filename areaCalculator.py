# First CheckPoint :: Area Calculator 

import math 

print('==================\nArea Calculator 📐\n==================\n')

print('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n')
choice = int(input('Enter your choice (1-5): '))
print('\n')

if choice == 1: 
    height = int(input('Height: '))
    base = int(input('Base: '))
    area = (height * base)/2
    print(f'\nThe Area is: {area}\n')
elif choice == 2: 
    length = int(input('Length: '))
    width = int(input('Width: '))
    area = length * width 
    print(f'\nThe Area is: {area}\n')
elif choice == 3: 
    side = int(input('Side: '))
    area = side**2
    print(f'\nThe Area is: {area}\n')
elif choice == 4: 
    radius = int(input('Radius: '))
    area = math.pi * (radius**2)
    print(f'\nThe Area is: {area}\n')
else:
    print('See you Soon!')
    
print ('Thank you, Goodbye! 🌷')
    
