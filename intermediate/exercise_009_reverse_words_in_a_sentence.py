"""
9. Reverse Words in a Sentence

Given "hello world this is me", return "me is this world hello".

def reverse_words(sentence):
    pass
"""

string = input("Please, write whatever you want (better if has many words): ")

def reverse_words(sentence: str) -> str:
    word_list = sentence.split(" ")
    print(word_list)
    inverted_words = ""
    for word in word_list[::-1]:
        inverted_words += " " + word
    return inverted_words.strip() # Eliminates first whitespace.

print(f"\n{reverse_words(string)}")

# Solution 2

"""
Notes:
- The function splits the sentence into words, reverses the list, and joins them back into a string.
- Using ' '.join(sentence.split()[::-1]) is more Pythonic and avoids leading/trailing spaces.
- Time complexity is O(n), where n is the length of the sentence.
- Handles multiple spaces and works for any input string.
"""