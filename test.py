# Programmer: Cory DeMar
# ComSc 20
# Assognment #10
# Strings

def to_pig(word):
    vowel = 'aeiouy'
    has_cap = word[0].isupper()
    word = word.lower()

    if word[0] in vowel and word[0] != 'y':
        result = word + 'way'
    else:
        pos = 0
        while word[pos] not in vowel:
            pos = pos + 1
        result = word[pos:] + word[0:pos] + 'ay'
    return result


sentence = input("Enter a word you would like to change into Pig Latin: ")

while sentence != '':
    sentence = sentence.rstrip()
    latin = ''
    
    while sentence != '':
        pos = sentence.find(' ')
        if pos < 0:
            pos = len(sentence)
        word = sentence[:pos]

        latin = latin +to_pig(word) + ' '
        sentence = sentence[pos + 1:]
    latin = latin.rstrip()
    print(latin)
    sentence = input("Enter another sentence, or ENTER to exit: ")