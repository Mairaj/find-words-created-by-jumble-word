import sys
# It is the file location where I saved your file from which the user input will be matched.
#dictfile = "/home/mairaj/Downloads/dictionary.txt"
dictfile = "/usr/share/dict/cracklib-small" 
# A function that will return a list of words from your given file.
def find_words(text):

    return text.split()
     
# This function takes two argument, first is the list of words from your given file,
# and second is the user input It will return the all possible word that will be made from user inputted jumble word
def get_possible_words(words,jword):
    
    # Empty list for storing the all possible word by user given input
    possible_words = []
    # Taking user inputed word length
    jword_length = len(jword)
    for word in words:
        jumbled_word = jword
        if len(word) == jword_length:
            # Taking the word in list formate to itrate the letters.
            letters = list(word)
            for letter in letters:
                # Here I am checking the letters in the user inputted word by letters in your given file.
                if jumbled_word.find(letter) != -1:
                    jumbled_word = jumbled_word.replace(letter,'',1)
            if not jumbled_word:
                possible_words.append(word)
    return possible_words      
             
                 
if __name__ == '__main__':
    words = find_words(file(dictfile).read())
    if len(sys.argv) != 2:
        print "python %s <jumbled word>" % sys.argv[0]
        sys.exit()
    jumbled_word = sys.argv[1]
    words = get_possible_words(words,jumbled_word)
    print "possible words :"
    print '\n'.join(words)
