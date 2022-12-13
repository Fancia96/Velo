
def return_verse(verse=None, end_verse=None):
    song_array = []
    f = open('../data/song.txt', 'r')
    for line in f:
        if(len(line.strip()) != 0):
            song_array.append(line.strip())
    f.close()

    verses = ""

    for i in range(0, len(song_array)):
        if i+1 == verse and end_verse == None:
            return song_array[i]
        if end_verse != None and i+1 >= verse and i+1 <= end_verse:
            verses += song_array[i]+"\n"

    return verses

def return_whole_song():
    number_of_verses = 0
    f = open('../data/song.txt', 'r')
    for line in f:
        if (len(line.strip()) != 0):
            number_of_verses += 1

    return return_verse(1, number_of_verses)

if __name__ == '__main__':
    pass
    # print(return_verse(1))
    #print(return_verse(4, 6))
    #print(return_whole_song())
