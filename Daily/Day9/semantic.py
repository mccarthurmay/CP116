#sentence: the powerful dog has the fish of the dig
dict_word = {"the": 2}
dict_pair = {"the":{"powerful":4, "dog":6, "fish":4, "lish":3, "tish": 2, "dish": 1}}
key = ""

def query(key):

    print(dict_word[key])
    global dict_pair
    print (sorted(list(dict_pair[key].values())))
    #print with keys?
    print (dict_pair[key])



while key != "quit":
    key = input("Query: ")
    query(key)
