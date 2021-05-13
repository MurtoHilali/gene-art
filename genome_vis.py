import numpy as np
from PIL import Image
import math

## open genome txt file as string 'seq'
with open(r"c_l_familiaris_c38.txt", 'r') as file:
    seq = file.readlines()[1:]
    seq = ''.join(seq).replace('\n','')

##RGB colours for each base
colours = {
    "A":[85, 61, 54],
    "T":[255, 200, 87],
    "C":[216, 71, 151],
    "G":[135, 160, 178]
}

## return the two closest integer factors of seq_length
## such that one is never more than 5x larger than the other
def dimensions(seq):
    seq_length = len(seq)
    a = int(math.sqrt(seq_length))
    while seq_length % a != 0:
        a += 1
    if a == seq_length or a >= (seq_length // a) * 5:
        vals = [dimensions(seq[:-1])[0], dimensions(seq[:-1])[1], seq[:-1]]
        return vals
    else:
        vals = [a, seq_length // a]
        return vals

## generates array with dimensions from dimensions() containing RGB values from colours {}
def generate(h, w, data):
    for i in range(h):
        for j in range(w):
            data[i,j] = colours3[seq[j+i*w]]
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
img.save('c_l_familiaris_c38.png')
img.show()
