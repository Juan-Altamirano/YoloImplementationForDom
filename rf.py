from roboflow import Roboflow
import json
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

for i in range(len(prediction)):

    localizacion = {'x': int(prediction[i].get('width')) / 2 + int(prediction[i].get('x')), 'y': int(prediction[i].get('height')) / 2 + int(prediction[i].get('y'))}

    print ("Las coordenadas del obeto son: ", localizacion, """
    Objeto nro: """, i)


print (localizacion)

# Prioridades = sorted(localizacion.get['x'])

# print(Prioridades)