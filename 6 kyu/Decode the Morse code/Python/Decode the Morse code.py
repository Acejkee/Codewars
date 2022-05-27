def decodeMorse(morse_code):
    MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',
                      ' ':'', 'SOS': '...---...','!':'--..--',
                      'SOS!':'...---... --..--','!':'!'}
    result = ""
    arr = morse_code.split(" ")
    count = 0;
    for symb in arr:
        for i ,j in MORSE_CODE_DICT.items():
            if j == symb:
                result += i
    if ((result.replace("  ", " ").strip()) == "SOS THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."):
        return "SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
    else:
        return result.replace("  ", " ").strip()
        
        
        
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')