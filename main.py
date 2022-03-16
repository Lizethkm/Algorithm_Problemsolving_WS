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
    current_count= 0
    current_letter= strings[0]
    final_result= ''
    for character in strings:
        if character == current_letter:
            current_count += 1
        else:
            final_result= final_result + str(current_count) + current_letter
            current_letter= character
            current_count= 1
    final_result= final_result + str(current_count) + current_letter
    print(final_result)
compressing_strings(word_to_compress)

#problem 4 bonus
users_input= input('Pick a word to check if it reads the same backward as forward: ')
def confirming_palindrome(users_word):
    reversed_word= ''
    for index in range(len(users_input) - 1, -1, -1):
        reversed_word += users_input[index]  
    if reversed_word == users_input:
            print(f'Yes, {reversed_word} reads the same backward as forward! ')
    else:
            print('Sorry, that word is not the same backward as forward.')
confirming_palindrome(users_input)


