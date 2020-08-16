import re,collections

def get_words(in_file, out_file):
    with open (in_file, encoding='utf-8') as f:
        words_box=[]
        for line in f:
            words = line.strip().strip(",").strip(".").split()
            words = list(map(lambda x:x.lower(), words))
            words_box.extend(words)
    word_dic = dict(collections.Counter(words_box))
    word_count = sorted(word_dic.items(), key=lambda d: d[1], reverse=True)
    out = open(out_file, 'w')
    for word in word_count:
        out.write(word[0]+":"+str(word[1])+"\n")
    out.close()

get_words("data/ShangHai.txt", 'temp/word_count.txt')