from baudot import encodeBaudot
from convertions import list2string, binary2array 
from hamming import Hammingencoder
from soundencoder import encodeSound
import matplotlib.pyplot as plt

text = str(input('input the data: '))
baudot = list2string(encodeBaudot(text))
print('Baudot code - ',baudot)
hamming = Hammingencoder(baudot)
print('Hamming code - ', hamming)
data = binary2array(hamming)
print('Final data - ',data)
signal = encodeSound(data)

plt.plot(signal)
plt.show()

