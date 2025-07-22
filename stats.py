def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = dict()
    for c in text:
        c = c.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sorted_char_count(char_count):
    def sort_on(items):
        return items["num"]

    char_counts = []
    for k,v in char_count.items():
        char_counts.append({"char": k, "num": v})
    char_counts.sort(reverse=True, key=sort_on)
    return char_counts
