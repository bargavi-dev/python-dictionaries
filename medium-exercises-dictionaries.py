
given_word = input('Please provide a word: ')
def letter_histogram(given_word):
    result = {}
    #for each letter in the user's word:
    for c in given_word:
            #add the letter to the 'result' dictionary
            #result[c] = 1
            #print the result dictionary
           # print(result)
        if c in result:
            result[c] += 1
            
        else:
            result[c] = 1
    print(result)
            
letter_histogram(given_word)


def word_histogram():
    given_sentence = input('Please provide a sentence: ')
    split_sentence = given_sentence.split()
    print(split_sentence)
    result2 = {}
    for word in split_sentence:
        if word in result2:
            result2[word] += 1
        else:
            result2[word] = 1
    print(result2)
word_histogram()

