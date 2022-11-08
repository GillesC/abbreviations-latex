# usage ./merge_abbr.py <filename1> <filename2> ...
# example ./merge_abbr.py abbr1.tex abbr2.tex
# results are stored in abbr-merged.tex

# be sure that your files are located in the same folder as this script
import re
import sys

args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

REGEX = r"^\\newacronym(\[(?P<plural>.*)\])?\{(?P<key>.*)\}\{(?P<abbr>.*)\}\{(?P<expand>.*)\}"

abbr = {}

for file_name in args:
    with open(file_name) as f:
       for line in f:
        line = line.strip()
        if not (len(line) == 0 or line.startswith("%")):
            m = re.search(REGEX, line)
            if m is not None:
                key = m.group('key')
                print(key)
                if key in abbr:
                    if abbr[key] == line:
                        print("same entry so ignored the double")
                    else:
                        print("Duplicate found, which to keep?")
                        choice = int(input(f"1: {abbr[key]} or 2: {line} or 3 to keep and change key"))
                        if choice == 2:
                            abbr[key] = line
                        if choice == 3:
                            print(f"Change key of {abbr[key]}?")
                            choice = input("N or <new-key>:")
                            if choice != "N":
                                abbr[choice] = abbr[key].replace(key, choice, 1)
                                del abbr[key]
                            print(f"Change key of {line}?")
                            choice = input("N or <new-key>:")
                            if choice != "N":
                                abbr[choice] = line.replace(key, choice, 1)
                else:
                    abbr[key] = line
        
with open("abbr-merged.tex", 'w') as f:
    f.write(r"generated by Gilles Callebaut with the script: https://github.com/DRAMCO/writing-scientific-papers-in-latex-tips-and-tricks/blob/main/glossaries/merge_abbr.py\n\n")
    first_letter = ""
    for key in sorted(abbr):
        if key[0] != first_letter:
            f.write(f"%%%%%%%%%%%% {key[0].upper()} %%%%%%%%%%%%\n")
            first_letter = key[0]
        f.write(f"{abbr[key]}\n")


