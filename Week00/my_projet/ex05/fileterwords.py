import sys
from string import punctuation

if __name__ == '__main__':
    print(sys.argv[1])
    if len(sys.argv) == 3 or (len(sys.argv) > 1 and not sys.argv[1].isnumeric()):
        list = sys.argv[1].split()
        filter = [x for x in list if len(x) > int(sys.argv[2])]
        result = []
        for a in filter:
            clean_word = a
            for b in clean_word:
                if b in punctuation:
                    clean_word = clean_word.replace(b, '')
            if clean_word != "" and len(clean_word) > int(sys.argv[2]):
                result.append(clean_word)
        print(result)
    else:
        print("ERROR!")