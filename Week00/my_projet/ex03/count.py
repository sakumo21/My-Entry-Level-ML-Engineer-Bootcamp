from string import punctuation
import sys

def text_analyzer(string: str | None = None):
    '''text_analyzer is a function that takes a single string and displays
the total number of printable characters'''
    u_letter = 0
    l_letter = 0
    p_mark = 0
    space = 0
    if not isinstance(string, str):
        print("this is not a string!")
        return
    while not string:
        s = input("enter string:")
    for a in string:
        if a.isupper():
            u_letter += 1
        elif a.islower():
            l_letter += 1
        elif a in punctuation:
            p_mark += 1
        elif a == " ":
            space += 1
        
    print(
        f"The text contains {len(string)} printable character(s):",
        f"- {u_letter} upper letter(s)",
        f"- {l_letter} lower letter(s)",
        f"- {p_mark} punctuation mark(s)",
        f"- {space} space(s)",
        sep="\n",
    )

if __name__ == '__main__':
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("ERROR!:more than one argument")