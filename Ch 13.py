#programming exercise 4-13
character='*'

size=10

for row in range(size):
    
    for col in range(size, row, -1):
        print(character, end='')
        
    print()