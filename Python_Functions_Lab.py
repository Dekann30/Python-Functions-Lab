# Challenge 1
def sum_to(n):
    nums = range(n+1)
    print(sum(nums))

sum_to(10)

# Challenge 2
def largest(numbers):
    print(max(numbers))

largest([85,52,92,582,592,974])

# Challenge 3
def occurances(word, letter):
    if letter in word:
        print(word.count(letter))
    else:
        print(f'{letter} is not in {word}')

occurances('giant', 'a')

# Challenge 4
def product(*args):
    prod = 1
    for arg in args:
        prod *= arg
    return prod

print(product(8,2,9,4))