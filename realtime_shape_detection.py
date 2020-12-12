import cv2

#untuk countour
contours = {}
#array deteksi polygon
approx = []
#ukuran print text
scale = 1
#untuk open camera
cap = cv2.VideoCapture(0)

#ngitung polygon
while(cap.isOpened()):
    #untuk capture camera tiap frame
    ret, frame = cap.read()
    if ret==True:
        #cv ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #deteksi Canny
        canny = cv2.Canny(frame,80,240,3)

        #gae contours
        canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0,len(contours)):

            #countour perimeter
            approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.02,True)

            #tambahan untuk objek yang tidak jelas
            if(abs(cv2.contourArea(contours[i]))<100 or not(cv2.isContourConvex(approx))):
                continue

            elif(len(approx)==4):

                #Hitung polygon
                vtc = len(approx)

                #Jika Terdeteksi 4 = persegi
                x,y,w,h = cv2.boundingRect(contours[i])
                if(vtc==4):
                    #print peregi dalam frame
                    cv2.putText(frame, 'PERSEGI', (x, y), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 255, 255), 2, cv2.LINE_AA)



        #munculkan hasil
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
        cv2.imshow('frame',frame)
        cv2.imshow('canny',canny)
        if cv2.waitKey(1) == 1048689:
            break

#finish
cap.release()
cv2.destroyAllWindows()