import numpy as np
from PIL import Image
import math

## open genome txt file as string 'seq'
with open(r"~\s_bongori.txt", 'r') as file:
    seq = file.read().replace('\n','')

##RGB colours for each base
colours = {
    "A":[98, 60, 234],
    "T":[136, 90, 90],
    "C":[244, 185, 66],
    "G":[75, 192, 217]
}

## function to return the two closest integer factors of seq_length
## now if there is a prime number of nucleotides in genome 
## the last one is dropped to make the new seq
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


## generates array with dimensions from dimensions() containing RGB values from colours {}
def generate(h, w, data):
    for k in range(w):
        data[0,k] = colours[seq[k]]
        data[1,k] = colours[seq[k+w]]
    for i in range(2, h):
        for j in range(w):
            if j == 0:
                data[i,j] = colours[seq[i*w]]
            else:
                data[i,j] = colours[seq[i*j]]
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
img.save('img4.png')
img.show()
