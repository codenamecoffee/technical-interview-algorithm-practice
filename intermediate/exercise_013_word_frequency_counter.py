"""
Word Frequency Counter (dicts)

Given a long string, return a dictionary where each key is a word and the value is how many times it appears.

"""

sentence = input("Plase, enter a sentence with many words separated by whitespaces: ")

def word_counter(sentence: str) -> dict[str, int]:
    sentence = sentence.replace(".","")
    result = {}
    word_list = sentence.split()
    for word in word_list:
        if word not in result:
            result[word] = 1
        else: 
            result[word] += 1
    return result

print(word_counter(sentence))

"""
Notes:
- The function removes periods from the sentence before splitting it into words.
- It uses a dictionary to count the frequency of each word.
- Using split() without arguments is more robust, as it handles multiple spaces.
- To make the count case-insensitive, convert the sentence to lowercase.
- Time complexity is O(n), where n is the number of words in the sentence.
"""