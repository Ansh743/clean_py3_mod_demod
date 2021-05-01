import pyaudio


RATE = 44100
CHANNELS = 1
BUFFER = 1024

class Audio(object):

	def __init__(self):

		self.p = pyaudio.PyAudio() 
		self.stream = self.p.open(format=pyaudio.paInt16, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=BUFFER)

	def play(self, signal, loop=1):

		for i in range(loop):
			self.stream.write(signal, len(signal))

		#self.stream.close()
		#self.p.terminate()