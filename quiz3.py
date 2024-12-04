# QUESTION 3

# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog

def check_pangram(pass_string):
    checked_string=pass_string.lower()
    print(checked_string)
    
    #set to crosscheck
    alphabet_set=set('abcdefghijklmnopqrstuvwxyz')

    ifPangram=set(checked_string)
    print(sorted(ifPangram))

    if alphabet_set.issubset(ifPangram):   #all 26 in the sentence
        print('the sentence is pangram')
    else:
       print("not pangram")
 
check_pangram("abcdefghijklmnopqrstuvwxyz")
check_pangram('The quick brown fox jumps over the lazy dog')

#not pangram
check_pangram('boyz')
check_pangram('money')

################