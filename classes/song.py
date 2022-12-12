
def return_verse(verse):
    song_array = []
    f = open('../data/song.txt', 'r')
    for line in f:
        if(len(line.strip()) != 0):
            song_array.append(line.strip())
    f.close()

    for i in range (0, len(song_array)):
        if i+1 == verse:
            return song_array[i]

if __name__ == '__main__':
    print(return_verse(1))
