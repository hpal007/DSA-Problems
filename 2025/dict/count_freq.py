
"""
Count Word Frequency
    Define a function to count the frequency of words in a given list of words.
Example:
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
    count_word_frequency(words) 
    Output: {'apple': 3, 'orange': 2, 'banana': 1}
    
"""

def count_word_frequency(words):
    result = dict()
    
    for el in words:
        if el in result:
            result[el] +=1
        else:
            result[el] = 1
    return result

# using get
def count_word_frequency_get(words):
    result = dict()
    
    for word in words:
        result[word] = result.get(word, 0) + 1

    return result
 
result = count_word_frequency_get(['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] )
print(result)