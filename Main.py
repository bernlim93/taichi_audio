from gtts import gTTS
from pydub import AudioSegment

moves = []
times = []
filename = "moves.txt"


def create_sound():
    """
    Using the moves and times global arrays,
    call the Google TTS library to create sound segments
    for each move.
    Concatenate each new move's sound to the current sound
    chunk.
    Finally, export the sound as a WAV file.
    :return:
    """
    sound = AudioSegment.silent(duration=0)
    for i in range(len(moves)):
        print moves[i], ':', times[i]
        tts = gTTS(text=moves[i], lang='zh')
        tts.save("temp.wav")
        sound += AudioSegment.from_wav("temp.wav")
        sound += AudioSegment.silent(duration=int(times[i])*1000)

    sound.export("output.wav", format="wav")


def create_list():
    """
    Iterate through the input file and add moves and times
    to the global arrays.
    :return:
    """
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


def main():
    create_list()
    create_sound()


if __name__ == '__main__':
    main()
