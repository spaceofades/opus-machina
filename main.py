def letter_count(words):
    count = {}
    words_lower = words.lower()

    alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

    alpha_list = alphabets.split(',')

    for alphabet in alpha_list:
        count[alphabet] = words_lower.count(alphabet)
    return count

def word_count(file_contents):
    words = file_contents.split()
    return len(words)
    
def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def report(file_path, word_count, letter_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for letter, count in letter_count.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


file_path = 'books/frankenstein.txt'
file = read_file(file_path)
word_counts = word_count(file)
letter_counts = letter_count(file)
report = report(file_path, word_counts, letter_counts)