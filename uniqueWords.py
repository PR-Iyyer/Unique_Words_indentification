def get_words(f):
    for line in f:
        for word in line.split():
            yield word
with open(r'D:/vocab.txt','r',encoding='utf-8') as infile:
    unique_words = sorted(set(get_words(infile)))

k=open(r'D:/uniqueWordsV.txt','w',encoding='utf-8') 
for w in unique_words:
    k.writelines('\n'+w)
