import csv

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

def main():
    banner_text_one = "Original Text"
    banner_text_two = "Altered Text"
    banner_symbol = "-"
    banner_symbol_length = 40
    lines = []

    #Setup the text file
    text_file = "ateam_Original.txt"
    accessMode = "r"
    text_content = open(text_file, accessMode)

    #Display original text
    display_banner(banner_text_one, banner_symbol, banner_symbol_length)
    #print(text_content.read())

    #Divide text line-by-line as a list
    text_to_list(lines, text_content)
    

    for i in lines:
        print(i)




main()