from gtts import gTTS
from pydub import AudioSegment

moves = []
times = []
filename = "moves.txt"


def print_list():
    sound = AudioSegment.silent(duration=0)
    for i in range(len(moves)):
        print moves[i], ':', times[i]
        tts = gTTS(text=moves[i], lang='zh')
        tts.save("temp.wav")
        sound += AudioSegment.from_mp3("temp.wav")
        sound += AudioSegment.silent(duration=int(times[i]))

    sound.export("output.wav", format="wav")


def main():
    global moves, times
    moves_file = open(filename)
    for movetime in moves_file:
        if len(movetime.split(',')) != 2:
            print "invalid input"
            continue

        move, time = movetime.split('\n')[0].split(',')

        if not time.isdigit():
            print "invalid time"
            continue

        moves.append(move)
        times.append(time)

    print_list()


if __name__ == '__main__':
    main()
