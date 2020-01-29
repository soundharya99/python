guess = 29
while True:
    a = input('Guess a number. (q) to quit ')
    if a == 'q':
        break
    num = int(a)
    if num > guess:
        print ('To high')
    elif num < guess:
        print ('To low')
    else:
        print ('Correct')
        break
