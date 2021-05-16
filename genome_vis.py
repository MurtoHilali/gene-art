import numpy as np
from PIL import Image
import math

## open genome txt file as string 'seq'
with open(r"c_l_familiaris_c38.txt", 'r') as file:
    seq = file.readlines()[1:]
    seq = ''.join(seq).replace('\n','')

##RGB colours for each base
colours = {
    "A":[170, 172, 176],
    "T":[182, 201, 187],
    "C":[191, 237, 193],
    "G":[27, 47, 51],
    "N":[252, 163, 17]
}

## function to return the two closest integer factors of seq_length
## with a minimum ration of 1:5
def dimensions(seq):
    seq_length = len(seq)
    a = int(math.sqrt(seq_length))
    while seq_length % a != 0:
        a += 1
    if a >= (seq_length // a) * 5:
        vals = [dimensions(seq[:-1])[0], dimensions(seq[:-1])[1]]
    else:
        vals = [a, seq_length // a]
    return vals

## generates array with dimensions from dimensions() containing RGB values from colour {}
def generate(h, w, data):
    for i in range(h):
        for j in range(w):
            data[i,j] = colours[seq[j+i*w]]
    return data

## assign height and width of image
vals = dimensions(seq)
h = min(vals[:2])
w = max(vals[:2])

## create empty array using h and w as dimensions
data = np.zeros((h,w,3), dtype=np.uint8)

## fill array with RGB values
data = generate(h, w, data)

## convert array into png image
img = Image.fromarray(data, 'RGB')
img.save('c_l_familiaris_c38_test_3.png')
img.show()
