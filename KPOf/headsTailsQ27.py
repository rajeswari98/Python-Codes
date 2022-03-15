def flip(ch):
    return 'H' if (ch=='T') else 'T'

def getFlipwithStartingCharcter(str, expected):

    flipcount = 0
    for i in range(len( str)):

        if (str[i] !=expected):
            flipcount += 1

    expected = flip(expected)
    return flipcount

def minFlipToMakeStringAlternate(str):

    return min(getFlipwithStartingCharcter(str,'T'), getFlipwithStartingCharcter(str, 'H'))

if __name__== "__main__":

    s = "TTTHTHTHHH"
    print(minFlipToMakeStringAlternate(s))