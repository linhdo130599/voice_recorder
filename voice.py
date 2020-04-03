import sounddevice as sd
import soundfile as sf
import time
import queue
import numpy
import sys

q = queue.Queue()

nameWav = 'Cau_8.wav'
fileText = 'C:/Users/Tuan Linh/Desktop/test/data/y_kien.txt'
sentence = 'Tôi chia tay người yêu cũng một phần vì văn hoá gia đình anh như vậy'
filename = 'C:/Users/Tuan Linh/Desktop/test/data/y_kien/' + nameWav

def callback(indata, frames, time, status):
    #Callback from another thread 
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def recordingFile(filename, sentence, fileText, nameWav):
    print('Read the below sentence:\n')
    print(sentence)
    try:
        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate = 22000,
                        channels = 1) as file:
            with sd.InputStream(samplerate = 22000, device = sd.default.device,
                                channels = 1, callback = callback):
                print('Press Ctrl+C to stop the recording')
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))

    file = open(fileText, "a")
    file.write(nameWav + '\n')
    file.write(sentence + '\n')
    file.close()

recordingFile(filename, sentence, fileText, nameWav)
