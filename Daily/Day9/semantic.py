# Task 1
import os
import wikipedia

animals_wiki = ['Aardvark', 'Abyssinian guinea pig', 'Acadian Flycatcher', 'Ackie Monitor', 'Aesculapian Snake', 'Black Mamba', 'Chickadee', 'Chihuahua', 'Chinchilla', 'Chipmunk']
holidays_wiki = ["New Year's Day", 'Memorial Day', 'Independence Day', 'Labor Day', 'Thanksgiving', 'Christmas', 'Martin Luther King Jr. Day', "Washington's Birthday", 'Juneteenth', 'Veterans Day', 'Diwali', 'Holi', 'Rosh Hashanah', 'Yom Kippur', 'Hanukkah', 'Ramadan', 'Eid al-Fitr', 'Eid al-Adha', 'Emancipation Day', 'Malcom X Day', 'Groundhog Day', "Valentine's Day", 'Flag Day']
us_events_wiki = ['Declaration of Independence', 'Articles of Confederation', 'Whiskey Rebellion', 'Louisiana Purchase', 'Battle of New Orleans', 'Monroe Doctrine', 'Treaty of Guadalupe Hidalgo', 'Dred Scott Decision', 'American Civil War', 'Battle of Gettysburg', 'Battle of Little Bighorn', 'Haymarket Affair', 'Plessy v. Ferguson', 'Breakup of Northern Securities', 'Sinking of the Lusitania', 'Stock Market Crash (1929)', 'Hiroshima', 'World War II', 'Cold War', 'Assassination of Martin Luther King, Jr.', 'Watergate Scandal', 'PATCO Strike', 'September 11 Attacks', 'COVID-19']
file_location = open('twenty_first_century')
def create_wiki_files(wiki_name):
    print(wiki_name)
    file_location = open('twenty_first_century/*')
    for f in file_location:
        os.remove(f)
    for word in list(wiki_name):

        wiki_file = open('twenty_first_century/' + word, 'w', encoding="utf-8")
        wiki_page = wikipedia.page(word)
        wiki_file.write(wiki_page.content)
        wiki_file.close()
        return

def wiki(action):
    if action == "animals":
        create_wiki_files(animals_wiki)
    if action == "holidays":
        create_wiki_files(holidays_wiki)
    if action == "us_events":
        create_wiki_files(us_events_wiki)


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



def filter_empty(word_list):
    return list(filter(lambda x: x != "", word_list))


def book_to_lists(book_text):

    book_text = book_text.replace(".", "<<EOS>>")
    book_text = book_text.replace("?", "<<EOS>>")
    book_text = book_text.replace("!", "<<EOS>>")

    sentences = book_text.split("<<EOS>>")

    word_lists = [item.split(" ") for item in sentences]
    return list(map(filter_empty, word_lists))



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


#done
def query(query_word, wc, pc):
    try:
        total = wc[query_word]
        other_counts = pc[query_word]

        other_words = other_counts.keys()
        sorted_words = sorted( other_words, key=lambda x: other_counts[x], reverse=True)
        return sorted_words[:5]
    except:
        return print("Word does not exist.")


nineteenth_books = load_and_clean_files("nineteenth_century")
all_nineteenth = []
for book in nineteenth_books:
    all_nineteenth += book_to_lists(book)


twentieth_books = load_and_clean_files("twentieth_century")
all_twentieth = []
for book in twentieth_books:
    all_twentieth += book_to_lists(book)

#twenty_first_books = load_and_clean_files("twenty_first_century")
#all_twenty-one = []
#for book in twenty_first_books:
#    all_twenty-one += book_to_lists(book)


nine_wc, nine_pc = make_counts(all_nineteenth)
twenty_wc, twenty_pc = make_counts(all_twentieth)
#twenty_one_wc, twenty_one_pc = make_counts(all_twenty-one)

word_input = ""

action = input("What wiki file would you like to load? (animals, holidays, us_events):  ")
wiki(action)


while word_input != quit:
    word_input = input("What word do you want: ")
    print(query(word_input, nine_wc, nine_pc))
    print(query(word_input, twenty_wc, twenty_pc))
#
