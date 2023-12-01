from roboflow import Roboflow
import json
import cv2
import time
rf = Roboflow(api_key="Jh3LRNFbdEZ8q7wqBpa2")
project = rf.workspace().project("dom-aeber")
model = project.version(2).model
p=0
cap = cv2.VideoCapture(0)

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized


while True:
    ret, frame = cap.read()
    if ret == False: 
        print("Enchufá la cámara capo, o quizás la está usando otra aplicación (como cámara)")
        break

    ImgNewName = "Prediction number "+str(p+1)+".jpg"
    p += 1

    IAInput = cv2.imwrite('./images/Imagen_Nro_'+str(p)+'.png',frame) # Esto guarda el frame guardado en la variable frame en la carpeta images como un archivo .jpg, para luego ser usado por la IA

    InputRoute = './images/Imagen_Nro_'+str(p)+'.png' # Esto nomás es la ruta para la img, pq no me dejaba ponerla directamente en el model.predict, pq lo toma como más de 1 parámetro

    # q se guarde la img con la bounding box y la prediccion
    model.predict(InputRoute, confidence=30, overlap=30).save(ImgNewName)

    prediction = model.predict(InputRoute, confidence=30, overlap=30).json().get('predictions')

    print(prediction)

    cv2.imshow('IAImgInput', frame)

    for i in range(len(prediction)):

        localizacion = {'x': int(prediction[i].get('width')) / 2 + int(prediction[i].get('x')), 'y': int(prediction[i].get('height')) / 2 + int(prediction[i].get('y'))}

        print ("Las coordenadas del obeto son: ", localizacion, """
        Objeto nro: """, i)

        print (localizacion)

        cv2.circle(frame, (int(localizacion.get('x')), int(localizacion.get('y'))), 5, (0, 0, 255), -1)

    if cv2.waitKey(1) == ord('q'):
        break

    time.sleep(4)

cv2.destroyAllWindows()


# Prioridades = sorted(localizacion.get['x'])

# print(Prioridades)