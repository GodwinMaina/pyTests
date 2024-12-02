# QUESTION 2

# Write a Python function that checks whether a word or phrase is palindrome or
# not. Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"


def check(wordPhrase):
    checked=wordPhrase.lower()
    #reverse by slicing
    isPandrom=checked[::-1]
    print(isPandrom)

    if (isPandrom==checked):
        print(f"Yes - {isPandrom} is palindrome")
    else:
        print("Not palindrome")

#yes palindrome
check('madam')
check('kayak')
check('racecar')

#Not palindrome
check('palindrom')
check('cardrip')
check('kayaka')
