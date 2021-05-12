import numpy as np
from PIL import Image
import math

## open genome txt file as string 'seq'
with open(r"h_cinaedi.txt", 'r') as file:
    seq = file.readlines()[1:]
    seq = ''.join(seq).replace('\n','')

##RGB colours for each base
colours = {
    "A":[98, 60, 234],
    "T":[136, 90, 90],
    "C":[244, 185, 66],
    "G":[75, 192, 217]
}

## function to return the two closest integer factors of seq_length
def dimensions(seq):
    seq_length = len(seq)
    a = int(math.sqrt(seq_length))
    while seq_length % a != 0:
        a += 1
    if a == seq_length:
        vals = [dimensions(seq[:-1])[0], dimensions(seq[:-1])[1], seq[:-1]]
        return vals
    else:
        vals = [a, int(seq_length / a)]
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
if len(vals) == 3:
    seq = vals[2]

## create empty array using h and w as dimensions
data = np.zeros((h,w,3), dtype=np.uint8)

## fill array with RGB values
data = generate(h, w, data)

## convert array into png image
img = Image.fromarray(data, 'RGB')
img.save('e_coli_new.png')
img.show()
