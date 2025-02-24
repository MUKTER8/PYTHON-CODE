def search_word(word):
    with open("practice.txt", "r") as f:
        data = f.read()
    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")
search_word("Learning")

def search_line(word):
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
            line_no += 1
    return -1

print(search_line("hello"))