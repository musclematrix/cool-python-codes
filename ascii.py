def generate_ascii(name):
    letters = {
        'A': ['  A   ', ' A A  ', 'AAAAA ', 'A   A ', 'A   A '],
        'B': ['BBBB  ', 'B   B ', 'BBBB  ', 'B   B ', 'BBBB  '],
        'C': [' CCCC ', 'C     ', 'C     ', 'C     ', ' CCCC '],
        'D': ['DDDD  ', 'D   D ', 'D   D ', 'D   D ', 'DDDD  '],
        'E': ['EEEEE ', 'E     ', 'EEE   ', 'E     ', 'EEEEE '],
        'F': ['FFFFF ', 'F     ', 'FFF   ', 'F     ', 'F     '],
        'G': [' GGGG ', 'G     ', 'G  GG ', 'G   G ', ' GGGG '],
        'H': ['H   H ', 'H   H ', 'HHHHH ', 'H   H ', 'H   H '],
        'I': ['IIIII ', '  I   ', '  I   ', '  I   ', 'IIIII '],
        'J': [' JJJJ ', '   J  ', '   J  ', 'J  J  ', ' JJJ  '],
        'K': ['K   K ', 'K  K  ', 'KKK   ', 'K  K  ', 'K   K '],
        'L': ['L     ', 'L     ', 'L     ', 'L     ', 'LLLLL '],
        'M': ['M   M ', 'MM MM ', 'M M M ', 'M   M ', 'M   M '],
        'N': ['N   N ', 'NN  N ', 'N N N ', 'N  NN ', 'N   N '],
        'O': [' OOO  ', 'O   O ', 'O   O ', 'O   O ', ' OOO  '],
        'P': ['PPPP  ', 'P   P ', 'PPPP  ', 'P     ', 'P     '],
        'Q': [' QQQ  ', 'Q   Q ', 'Q   Q ', 'Q  QQ ', ' QQQQ '],
        'R': ['RRRR  ', 'R   R ', 'RRRR  ', 'R  R  ', 'R   R '],
        'S': [' SSSS ', 'S     ', ' SSS  ', '    S ', 'SSSS  '],
        'T': ['TTTTT ', '  T   ', '  T   ', '  T   ', '  T   '],
        'U': ['U   U ', 'U   U ', 'U   U ', 'U   U ', ' UUU  '],
        'V': ['V   V ', 'V   V ', ' V V  ', '  V   ', '  V   '],
        'W': ['W   W ', 'W   W ', 'W W W ', 'WW WW ', 'W   W '],
        'X': ['X   X ', ' X X  ', '  X   ', ' X X  ', 'X   X '],
        'Y': ['Y   Y ', ' Y Y  ', '  Y   ', '  Y   ', '  Y   '],
        'Z': ['ZZZZZ ', '   Z  ', '  Z   ', ' Z    ', 'ZZZZZ '],
        ' ': ['      ', '      ', '      ', '      ', '      '],
    }

    # Convert name to uppercase
    name = name.upper()
    
    # Initialize the lines
    ascii_lines = ['' for _ in range(5)]
    
    # Build ASCII art line by line
    for char in name:
        if char in letters:
            for i in range(5):
                ascii_lines[i] += letters[char][i] + '  '

    # Print the output with formatting
    print("\nEnter name:", name)
    print("~" * 30,"\n")  # Line separator
    for line in ascii_lines:
        print(line)
    print("\n","~" * 30)  # Line separator

# Input name
user_name = input("Enter a name: ")
generate_ascii(user_name)
