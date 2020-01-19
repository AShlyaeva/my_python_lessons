tolstoy_text = open('tolstoy.txt', 'r').read()

mur2 = "ryjghntyj sasha tyhetgh sasha"
mur = "Hello Artem"
#print(mur)
#print(mur[0:5])
#for i in range(6, len(mur)):
#    print(mur[i])
def find_smth(where, what):
    for i in range(0, len(where) - len(what) + 1):
        cur_slice = where[i:i + len(what)].lower()
        if cur_slice == what.lower():
            for j in range(0, len(cur_slice)):
                print(cur_slice[j])
            print("Впервые встретилось в символе №", i)
            return
    print("Слово ", what, " не нашел")

def find_smth2(where, what):
    start = where.lower().find(what.lower())
    if start >= 0:
        for i in range(len(what)):
            print(where[i + start])
        print("Впервые встретилось в символе №", start)
        return
    print("Слово ", what, " не нашел")

#find_smth(mur, "Artem")
#find_smth(mur2, "SasHA")
find_smth(tolstoy_text, 'КНЯЗЬ')
    
find_smth2(tolstoy_text, 'КНЯЗЬ')