import bs4 as bs
import urllib.request
import textract
import re
import numpy as np


def dictionary_parsing(file_path):
    # source page
    source = urllib.request.urlopen(file_path).read()
    # create the bs object
    soup = bs.BeautifulSoup(source, 'lxml')

    my_dictionary = {
            "words": []}

    for idx, s in enumerate(soup.find_all('strong')):
        if idx > 1:
            word = s.string
            if word[:3] == 'to ':
                word = word[3:]
            my_dictionary["words"].append(word)

    return my_dictionary


my_dict_path = 'file:///D:/Andrei/Programming/Python/Movie_script_analysis/Dictionary.html'
my_dictionary = dictionary_parsing(my_dict_path)
my_dictionary_words = np.array(my_dictionary['words'])

popular_words_1000_path = 'file:///D:/Andrei/Programming/Python/Movie_script_analysis/1000_popular_words.html'
pop_words = dictionary_parsing(popular_words_1000_path)
pop_words = np.array(pop_words['words'])

known_words = np.append(my_dictionary_words, pop_words)

script_text = textract.process("D:\Andrei\Programming\Python\Movie_script_analysis\Blow_out_script.docx")
words_in_text = re.findall(r'\w+', str(script_text))
#words_in_text = re.split(r'[\n \t\r,.!?]', str(script_text))
#words_in_text = [words_in_text[i] for i in range(len(words_in_text)) if len(words_in_text[i])<15]
words_in_text = np.unique(np.array([words_in_text[i].lower() for i in range(len(words_in_text))]))
words_in_text = np.array([words_in_text[i] for i in range(np.size(words_in_text)) if not words_in_text[i].isdigit()])

known_words_in_text = np.array([words_in_text[i] for i in range(np.size(words_in_text)) if words_in_text[i] in known_words])
unknown_words_in_text = np.array([words_in_text[i] for i in range(np.size(words_in_text)) if words_in_text[i] not in known_words])

