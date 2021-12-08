import numpy as np
import cv2
#importando as bibliotecas

cap = cv2.VideoCapture('fish1.mp4')
#importando o video com a função do cv2

fgbg = cv2.createBackgroundSubtractorMOG2()
#criando instancia com ajuda do cv2

#while infinito
while (1):
    ret, frame = cap.read()
    #read le as frames do video

    fgmask = fgbg.apply(frame)
    #aplica o brackground subtractor

    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame', frame)
    #displaying todos os frames

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    #realease

cap.release()
cv2.destroyAllWindows()