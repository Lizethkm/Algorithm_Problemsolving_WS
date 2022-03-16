



#problem 1
reversed_word= ''
word= 'Hello'

for index in range(len(word) - 1, -1, -1):
    reversed_word += word[index]   
print(reversed_word) 

#problem 2
words_to_capitalize= 'hello world'
capitalizing_words= words_to_capitalize.title()
print(capitalizing_words)

#problem 3
word_to_compress= 'aaabbbbbccccaacccbbbaaabbbaaa'
def compressing_strings(strings):
    for character in strings:
        while character == 'a':
           count +=1
        while string == 'b':
            character += 1
        while string == 'c':
            character += 1
    return result
result= compressing_strings(word_to_compress)

