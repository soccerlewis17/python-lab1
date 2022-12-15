
# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

letter = input('Enter a letter from A-Z to see if it is a vowel: ').upper()
if letter in 'A E I O U':
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant')