import csv

def display_banner(banner_phrase, symbol, length):
    print(symbol * length)
    print(banner_phrase)
    print(symbol * length)


def main():
    banner_text_one = "Original Text"
    banner_text_two = "Altered Text"
    banner_symbol = "-"
    banner_symbol_length = 40

    #Setup the text file
    text_file = "ateam_Original.txt"
    accessMode = "r"
    text_content = open(text_file, accessMode)

    #Display original text
    display_banner(banner_text_one, banner_symbol, banner_symbol_length)
    print(text_content.read())




main()