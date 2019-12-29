# go on this site: http://cit.evc.edu/comsc020/
# Skip 9.15

#---------------------------------------------------------

# Giving a string str and a positive number
# positive pos, return the equivalent negative
# positive.
def negative_position(str, pos):
    result = pos - len(str)
    return result

s = 'testing'
p = s.index('n')
print('positive position:', p)
print('negative postition:', negative_position(s, p))

#---------------------------------------------------------

s = 'cat'
for ch in s:
    print (ch)

#---------------------------------------------------------

s = 'house'

#print each caracter on a seprate line
for ch in s:
    print(ch)

#seprator line
print('-' * 20)

# print each charater on a seporate line, by using index number
for i in range(len(s)):
    print(s[i])

#---------------------------------------------------------

# Print everything up to but not including the
# first non-letter in a string.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

str = input('Enter your string: ')
while str != '':
    pos = 0 # Start at beginning of string
    while str[pos].lower() in alphabet:
        pos = pos + 1
    print('your 1st word is', str[0:pos])

    str = input('Enter another string, or ENTER to quit: ')

#---------------------------------------------------------

# accept a sectence and reverse each word in the sentence.
# thus: ham sandwach -> mah hciwdnas

#   Get a sentance (input)
#   split it into individual words
#   result sentence starts as the empty string
#   for each world:
#       reverse the word
#       add it to my result sentence
#   prent result sentence

def reverse(word):
    new_word = ''
    for char in word:
        new_word = char + new_word # add characters at start
    return new_word

sentence = input('Enter a sentence: ')
words = sentence.split() # Creat a list
backwards = "" #this will be my result
for one_word in words:
    backwards = backwards + reverse(one_word) + ' '

print(backwards)
    