from roboflow import Roboflow
import json
import cv2
cameraOutput = cv2.VideoCapture(0)
rf = Roboflow(api_key="Jh3LRNFbdEZ8q7wqBpa2")
project = rf.workspace().project("dom-aeber")
model = project.version(2).model

# infer on a local image
# print(model.predict("Ult_DS (109).jpg", confidence=30, overlap=30).json())

# coords = model.predict("Ult_DS (109).jpg", confidence=30, overlap=30).json().get('predictions')[0].get('x')

# visualize your prediction
model.predict("000082_jpg.rf.1f1f752c0069d5649108017e2d3c9b2c.jpg", confidence=30, overlap=30).save("new prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

# prediction = json.loads(str(model.predict("Ult_DS (94).jpg", confidence=30, overlap=30).json()))

prediction = model.predict("000082_jpg.rf.1f1f752c0069d5649108017e2d3c9b2c.jpg", confidence=50, overlap=30).json().get('predictions')

print(prediction)

localizacion = []

for i in range(len(prediction)):

    localizacionI = int(prediction[i].get('width') / 2) + int(prediction[i].get('x')), int(prediction[i].get('height') / 2) + int(prediction[i].get('y'))
    localizacion.append(str(localizacionI))

    print ("Las coordenadas del obeto son: ", localizacion[i], """
    Objeto nro: """, i+1)


print (localizacion)

# Prioridades = sorted(localizacion.get['x'])

# print(Prioridades)