from roboflow import Roboflow
import json
import cv2
import time
rf = Roboflow(api_key="Jh3LRNFbdEZ8q7wqBpa2")
project = rf.workspace().project("dom-aeber")
model = project.version(2).model
p=0
cap = cv2.VideoCapture(0)
localizacion = []
direccion = ""

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA): # Esta función la uso para que el input que le doy a la IA sea correspondiente a las dimensiones de las imgs que se usó para entrenarla
    dim = None
    (h, w) = image.shape[:2] # Esto es para que agarre el alto y ancho de la img

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        # calculate the ratio of the width and construct the dimensions
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

    p+=1
    
    ImgNewName = "Prediction number "+str(p)+".jpg"

    resized_frame = image_resize(frame, width = 640, height = 640)

    IAInput = cv2.imwrite('./images/Imagen_Nro_'+str(p)+'.png',resized_frame) # Esto guarda el frame guardado en la variable frame en la carpeta images como un archivo .jpg, para luego ser usado por la IA

    InputRoute = './images/Imagen_Nro_'+str(p)+'.png' # Esto nomás es la ruta para la img, pq no me dejaba ponerla directamente en el model.predict, pq lo toma como más de 1 parámetro y se enoja

    # q se guarde la img con la bounding box y la prediccion
    model.predict(InputRoute, confidence=30, overlap=30).save(ImgNewName)

    prediction = model.predict(InputRoute, confidence=30, overlap=30).json().get('predictions')

    print(prediction)

    cv2.imshow('IAImgInput', resized_frame)

    for i in range(len(prediction)):

        localizacion = {'x': int(prediction[i].get('width')) / 2 + int(prediction[i].get('x')), 'y': int(prediction[i].get('height')) / 2 + int(prediction[i].get('y'))}

        print ("Las coordenadas del obeto son: ", localizacion, """
        Objeto nro: """, i)

        print (localizacion)

        cv2.circle(resized_frame, (int(localizacion.get('x')), int(localizacion.get('y'))), 5, (0, 0, 255), -1)

    if cv2.waitKey(1) == ord('q'):
        break

    for i in localizacion:
    # Adapting prediction results and location to thrust vectors to be sent to the Arduino, no sé por qué lo puse en inglés pero bueno
        if localizacion.get("x") <= 213:
            direccion = "izq"
            print("Girar a la izquierda")
            # Imagino q los valores van a ir de 0 a 255, por lo que voy a mandarle al motor derecho algo tipo 200 y al izq 50, para que gire a la izq

        elif localizacion.get("x") <= 426 and localizacion.get("x") > 213 and localizacion.get("y") >= 280:
            direccion = "alante"
            print("Seguir derecho")
            # Motor izq 200, motor derecho 200

        elif localizacion.get("x") <= 426 and localizacion.get("x") > 213:
            direccion = "alante"
            print("Seguir derecho")
            # Motor izq 200, motor derecho 200
        
        elif localizacion.get("x") > 426:
            direccion = "der"
            print("Girar a la derecha")
            # Motor izq 200, motor derecho 50
        
        print(direccion)


    # Todavía tengo que hacer el orden de prioridad de los objetos, pero eso lo hago después, por ahora que solo se mueva en función del objeto más a la izq
    # Después me gustaría hacer que si detecta múltiples objetos a la izq y no deja de girar, que después de cierto punto pare y sólo siga derecho, pero ta complejo eso

    time.sleep(3)

cap.release()
cv2.destroyAllWindows()