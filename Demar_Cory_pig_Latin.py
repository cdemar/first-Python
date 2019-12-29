# Programmer: Cory DeMar
# ComSc 20
# Assognment #10
# Strings

def to_pig(word):
    vowel = 'aeiouy' # word bank for vowel
    word = word.lower() # to help me have all lowercace

    if word[0] in vowel and word[0] != 'y': # if first leter is vowel and not 'y'
        result = word + 'way'
    else: # if first letter is anything else
        pos = 0
        while word[pos] not in vowel:
            pos = pos + 1
        result = word[pos:] + word[0:pos] + 'ay'
    return result


# opening sentence
sentence = input("Enter a word you would like to change into Pig Latin: ") #starting sentence


while sentence != '': #enter function checks for spaces and removes them before translating to pig latin
    sentence = sentence.rstrip()
    latin = ''
    
    while sentence != '':
        pos = sentence.find(' ') # adds a space after translation so to_pig
        if pos < 0:
            pos = len(sentence)
        word = sentence[:pos]

        latin = latin +to_pig(word) + ' '
        sentence = sentence[pos + 1:]
    latin = latin.rstrip()
    
    print(latin)
    sentence = input("Enter another sentence, or ENTER to exit: ") #continually asking after it transverts