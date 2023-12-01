import cv2
import time

cap = cv2.VideoCapture(0)

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA): # Esta función la uso para que el input que le doy a la IA sea correspondiente a las dimensiones de las imgs que se usó para entrenarla
    dim = None
    (h, w) = image.shape[:2] # Esto es para que agarre el alto y ancho de la img

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

p=0

while True:
    ret, frame = cap.read()
    if ret == False: 
        print("Enchufá la cámara capo, o quizás la está usando otra aplicación (como cámara)")
        break
    
    p+=1

    resized_img = image_resize(frame, width = 640, height = 640)

    cv2.imwrite('./images/Imagen_Nro_'+str(p)+'.png', resized_img)

    cv2.imshow('IAImgInput', resized_img)

    print(resized_img.shape[:2])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(2)

cap.release()
cv2.destroyAllWindows()