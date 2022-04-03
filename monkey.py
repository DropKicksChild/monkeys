import string
import random
import threading

characters = list(string.ascii_letters)
genWords = 0
island = input('enter: ')
lf = island.lower()

def monkeys():

    random.shuffle(characters)
    typing = True

    while typing:
   
        word = []

        length = random.randint(1, 7)
        for i in range(length):
            word.append(random.choice(characters))
        random.shuffle(word)
        bob = ("".join(word).lower())
        global genWords
        genWords += 1
        #print(f'{genWords}: {bob}')

        if lf in bob:
            print(f'the monkeys finally wrote {lf}, and they typed {genWords} before getting here')
            typing = False


threads = []
for i in range(50):
    t = threading.Thread(target=monkeys())
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()

monkeys()
