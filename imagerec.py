from PIL import Image
from functools import reduce
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import time


def createEx():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10) 
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
           # print(str(eachNum) + '.' + str(eachVer))
            imgFilePath = 'images/numbers/' + str(eachNum)+'.'+ str(eachVer)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            lineToWrite = str(eachNum)+'::'+ eiar1+'\n'
            numberArrayExamples.write(lineToWrite)
            

def threshold(imageArray):
    balanceAr = []
    newArray = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: int(x) + int(y), eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: int(x) + int(y), balanceAr)/len(balanceAr)

    for Row in newArray:
        for eachPix in Row:
            if reduce(lambda x, y: int(x) + int(y), eachPix[:3])/len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255  
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255


    return newArray 

def whatNumIsThis(filePath):
    matchedAr=[]
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i=Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()

    inQuestion = str(iar1)

    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr=splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ = inQuestion.split('],')

            x=0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1

                
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)

    graphX = []
    graphY = []
    
    for eachItem in x:
        print(eachItem)
        graphX.append(eachItem)
        print(x[eachItem])
        graphY.append(x[eachItem])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY, align='center')
    plt.ylim(400)
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()
    

whatNumIsThis('images/numbers/2.2.png')


            
'''i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

threshold(iar3)
threshold(iar2)
threshold(iar4)
threshold(iar)
fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()'''

#i= Image.open('images/numbers/y0.5.png')
#iar = np.asarray(i)
#plt.imshow(iar)
#plt.show()


