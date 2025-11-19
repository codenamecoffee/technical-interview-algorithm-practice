"""
2. Character Compression

Implement a simple string compression algorithm:
Convert "aaabbccccd" into "a3b2c4d1".

def compress_string(s):
    pass
"""

s = "aaabbccccd"
s2 = "abc"
s3 = ""
s4 = "aabbaabbccddccdd"

def compress_string(s: str) -> str:

    if s:
        result = ""
        index = 0  
        while (index < len(s)):
            char = s[index]
            count = 1 
            index += 1 
            while (index < len(s) and char == s[index]):
                count += 1
                index += 1 
            result += char + str(count)
        
        return result
            
    else:
        return "El string es vacío (sin caracteres)."

print(compress_string(s))
print(compress_string(s2))
print(compress_string(s3))
print(compress_string(s4))

"""
Notes:
- This implementation performs run-length encoding: it compresses the string by counting consecutive repeated characters.
- For each group of consecutive characters, it appends the character and its count to the result.
- Handles empty strings and works for any input.
- Time complexity is O(n), where n is the length of the input string.
- Example: "aabbaabbccddccdd" → "a2b2a2b2c2d2c2d2"
"""