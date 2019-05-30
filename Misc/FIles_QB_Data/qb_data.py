qbfile = open("qbdata.txt", "r")   # open the connection to the file that we'll be using

for aline in qbfile:
    values = aline.split()
    print('QB', values[0], values[1], 'had a rating of', values[10] )

qbfile.close()