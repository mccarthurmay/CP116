# Task 1
import os
import wikipedia

#wikipedia pages to download
animals_wiki = ['Aardvark', 'Abyssinian guinea pig', 'Olive Baboon', 'European Robin', 'Narwhal', 'Acadian Flycatcher', 'Ackie Monitor', 'Aesculapian Snake', 'Chickadee', 'Chihuahua (dog)', 'Chinchilla', 'Chipmunk']
holidays_wiki = ["New Year's Day", 'Thanksgiving', 'Christmas', 'Martin Luther King Jr Day', "Washington's Birthday", 'Veterans Day', 'Diwali', 'Holi', 'Rosh Hashanah', 'Yom Kippur', 'Hanukkah', 'Ramadan', 'Eid al-Fitr', 'Eid al-Adha', 'Emancipation Day', "Valentine's Day"]
us_events_wiki = ['Declaration of Independence', 'Articles of Confederation', 'Whiskey Rebellion', 'Louisiana Purchase', 'Battle of New Orleans', 'Treaty of Guadalupe Hidalgo', 'American Civil War', 'Battle of Gettysburg', 'Battle of Little Bighorn', 'Haymarket Affair', 'Stock Market Crash (1929)', 'World War II', 'Assassination of Martin Luther King, Jr.', 'Watergate Scandal', 'PATCO Strike', 'September 11 Attacks', 'COVID-19']

#create wiki pages
def create_wiki_files(wiki_name):
    try:
        #checks if directory exists
        if not os.path.exists('twenty_first_century'):
            os.mkdir('twenty_first_century')
        #removes all old files every time this is ran
        files = os.listdir('twenty_first_century')
        for f in files:
            file_path = os.path.join('twenty_first_century', f)  # Fix the path delimiter
            if os.path.isfile(file_path):
                os.remove(file_path)
    except OSError:
        return

    #create a new txt file containing the content of each wiki page
    for word in list(wiki_name):

        wiki_file = open('twenty_first_century/' + word + '.txt', 'w', encoding="utf-8")
        wiki_page = wikipedia.page(word)
        wiki_file.write(wiki_page.content)
        wiki_file.close()

    return


#wiki page creation function taking user input
def wiki(action):
    if action == "animals":
        create_wiki_files(animals_wiki)
    if action == "holidays":
        create_wiki_files(holidays_wiki)
    if action == "us_events":
        create_wiki_files(us_events_wiki)

#input for wiki page creation
action = input("What wiki file would you like to load? (animals, holidays, us_events):  ")
wiki(action)


#clean files function
def load_and_clean_files(target):
    # load files
    directory = os.listdir(target)
    # store books in a list
    books = []
    # loop to open file and clean text
    for file in directory:
        # open and read book
        contents = open(target+'/'+file, errors="ignore")
        book = contents.read()
        # turn all character lower and remove newline
        book = book.replace('\n',' ')
        for punc in [",", ":", ";", '"',"'","—","‘","’", "-", "/", "$"]:
            book = book.replace(punc, "")
        book = book.lower()
        # add book to list of books
        books.append(book)
    # return list of books
    return books


#remove empty word function
def filter_empty(word_list):
    return list(filter(lambda x: x != "", word_list))

#turn booki to lists function
def book_to_lists(book_text):

    book_text = book_text.replace(".", "<<EOS>>")
    book_text = book_text.replace("?", "<<EOS>>")
    book_text = book_text.replace("!", "<<EOS>>")

    sentences = book_text.split("<<EOS>>")

    word_lists = [item.split(" ") for item in sentences]
    return list(map(filter_empty, word_lists))


#make word counts function
def make_counts(list_of_sents):
    word_count = {}
    pair_count = {}
    for sentence in list_of_sents:
        for wordind in range(len(sentence)):
            current = sentence[wordind]
            if wordind < len(sentence) - 1:
                # get the next word in the sentence
                next = sentence[wordind+1]
                # see if we have a dictionary for the current word,
                # if not, make one
                scores_for_word = pair_count.get(current, {})
                # see if next appears in the dictionary for the
                # current word, if not return 0
                next_score = scores_for_word.get(next,0)
                # modify the score we stored
                scores_for_word[next] = next_score + 1
                # save the original dict
                pair_count[current] = scores_for_word

            count = word_count.get(current,0)
            word_count[current] = count + 1

    return word_count, pair_count


#return words with highest count function
def query(query_word, wc, pc):
    try:
        total = wc[query_word]
        other_counts = pc[query_word]

        other_words = other_counts.keys()
        sorted_words = sorted( other_words, key=lambda x: other_counts[x], reverse=True)
        return sorted_words[:5]
    except:
        return print("Word does not exist.")

#append books into single list
nineteenth_books = load_and_clean_files("nineteenth_century")
all_nineteenth = []
for book in nineteenth_books:
    all_nineteenth += book_to_lists(book)


twentieth_books = load_and_clean_files("twentieth_century")
all_twentieth = []
for book in twentieth_books:
    all_twentieth += book_to_lists(book)

twenty_first_books = load_and_clean_files("twenty_first_century")
all_twenty_one = []
for book in twenty_first_books:
    all_twenty_one += book_to_lists(book)


nine_wc, nine_pc = make_counts(all_nineteenth)
twenty_wc, twenty_pc = make_counts(all_twentieth)
twenty_one_wc, twenty_one_pc = make_counts(all_twenty_one)


#user input function
def print_tasks():

    task = input ("Type task ('help' prints functions): ")

    #help
    if task == "help":
        print("\n'most common word': return the most common word following an input word in each century")
        print("\n'load': load new wiki file list for 21st century")
        print("\n'predict': input a sentence with a '[]' and we will predict the word for you'")

    #prints most common following word in each century
    elif task == "most common word":
        word_input = input("What word do you want: ")
        print(query(word_input, nine_wc, nine_pc))
        print(query(word_input, twenty_wc, twenty_pc))
        print(query(word_input, twenty_one_wc, twenty_one_pc))

    #predicts word in sentence
    elif task == "predict":
        sentence_input = input("Type a sentence with $: ")
        sentence_list = sentence_input.split()

        try:
            #finds word before $
            word_input = sentence_list[sentence_list.index('$') - 1]
            century = input("What century do you want? (19th, 20th, 21st): ")

            #prints most common following word into sentence
            if century == "19th":
                try:
                    predict_word = list(query(word_input, nine_wc, nine_pc))[0]
                    print(sentence_input.replace('$', predict_word))
                except:
                    return print("Word DNE")
            elif century == "20th":
                try:
                    predict_word = list(query(word_input, twenty_wc, twenty_pc))[0]
                    print(sentence_input.replace('$', predict_word))
                except:
                    return print("Word DNE")
            elif century == "21st":
                try:
                    predict_word = list(query(word_input, twenty_one_wc, twenty_one_pc))[0]
                    print(sentence_input.replace('$', predict_word))
                except:
                    return print("Word DNE")
        except:
            return print("'$' is not in the sentence.")

    #load different wiki texts
    elif task == "load":
        action = input("What wiki file would you like to load? (animals, holidays, us_events):  ")
        wiki(action)

task = ""


while task != quit:
    print_tasks()
