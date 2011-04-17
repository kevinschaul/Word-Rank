import sys

file = open(sys.argv[1], 'r')
fileContent = file.read()
l = {}
for word in fileContent.split():
    # make everything lowercase
    word = word.lower()
    
    # check for words in () or []
    if word.startswith('[') or word.startswith('('):
        word = word[1:]
    if word.endswith(']') or word.endswith(')'):
        word = word[:-1]
        
    # check for words that end with punctuation
    if word.endswith('.') or word.endswith(',') or word.endswith(';') or word.endswith(':'):
        word = word[:-1]
    # if word is in dictionary, increment the value
    # otherwise add the word to dictionary with value 1
    if word in l:
        l[word] += 1
    else:
        l[word] = 1
        
# this prints the dict out sorted by value
for key, value in sorted(l.iteritems(), key=lambda (k,v): (v,k)):
    print '%s: %s' % (key, value)
