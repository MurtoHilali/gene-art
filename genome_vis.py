import numpy as np
from PIL import Image
import math

## NZ_CP053416.1 Salmonella bongori strain 85-0051 chromosome, complete genome

## open genome txt file as string 'seq'
with open(r"\s_bongori.txt", 'r') as file:
    seq = file.read().replace('\n','')

## get string length (put inside of dimensions?)
seq_length = len(seq)

## RGB colours for each base
colours = {
    "A":[98, 60, 234],
    "T":[136, 90, 90],
    "C":[244, 185, 66],
    "G":[75, 192, 217]
}

## function to return the two closest integer factors of seq_length
def dimensions(seq_length):
    a = int(math.sqrt(seq_length))
    while seq_length % a != 0:
        a += 1
    if a == seq_length:
        return "Is prime"
        ## in this case, should I remove a nucleotide and try again
        ## repeatedly? or prompt for a different sequence
    else:
        return a, int(seq_length / a)

## generates array with dimensions from dimensions() containing RGB values from colour {}
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
h = dimensions(seq_length)[1]
w = dimensions(seq_length)[0]

## create empty array using h and w as dimensions
data = np.zeros((h,w,3), dtype=np.uint8)

## fill array with RGB values
data = generate(h, w, data)

## convert array into png image
img = Image.fromarray(data, 'RGB')
img.save('img.png')
img.show()
