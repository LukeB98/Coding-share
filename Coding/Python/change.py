list_alpha = list(input('Type a word: '))
n = -1

while n < 9:
    n = n + 1
        
    vowels = list('aeiouAEIOU')
    letter = vowels[n]
         
    while True:
        
        if letter in list_alpha:
            list_alpha.remove(letter)
    
        else:
           break
       
print(''.join(list_alpha))