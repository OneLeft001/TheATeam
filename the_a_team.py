import csv, random

def display_banner(banner_phrase, symbol, length):
    print(symbol * length)
    print(banner_phrase)
    print(symbol * length)

def text_to_list(lines_list, text_content):
    while True:
        line = text_content.readline()
        if not line:
            break
        lines_list.append(line.strip())

def lines_to_upper(lines, uppercase_threshold):
    for i, j in enumerate(lines):
        if(len(j) <= uppercase_threshold):
            lines[i] = j.upper()
    
    '''counter = 0
    for i in lines:
        if(len(i) <= uppercase_threshold):
            lines[counter] = i.upper()

        counter += 1
'''
    


def main():
    banner_text_one = "Original Text"
    banner_text_two = "Altered Text"
    banner_symbol = "-"
    banner_symbol_length = 40
    uppercase_threshold = 20
    lines = []

    #Setup the text file
    text_file = "ateam_Original.txt"
    accessMode = "r"
    text_content = open(text_file, accessMode)

    #Display original text
    display_banner(banner_text_one, banner_symbol, banner_symbol_length)
    print(text_content.read())
    text_content = open(text_file, accessMode)

    

    #Divide text line-by-line as a list
    text_to_list(lines, text_content)

    #Upper lines    
    lines_to_upper(lines, uppercase_threshold)

    for i, j in enumerate(lines):
        print(j)
    

    




main()