
# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

terms = (range(50))
first_number = 0
second_number = 1
for term in terms:
    if term < 2:
        print(f'term: {term} / number: {term}')
    else:
        new_number = first_number + second_number
        print(f'term: {term} / number: {new_number}')
        first_number = second_number
        second_number = new_number