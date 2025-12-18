"""
Fichero encargado de crear predicciones

No la hemos usado, hay que mirar su uso


"""



import random

import matplotlib.pyplot as plt # Para mostrar la imagen uso matplotlib (otra librería muy usada en Python)
from Software.Redes.red import *
from Software.Utils.data import *

def imshow(img, label):
    img = img / 2 + 0.5
    img = img.clamp(0, 1)
    plt.imshow(img.permute(1, 2, 0))
    plt.title(f'Label: {label}')
    plt.show()

INDEX = random.randint(0, 16)
dataiter = iter(test_loader)
images, labels = next(dataiter)
output = model_cnn(images[INDEX].to(DEVICE)) # Añadir una dimensión para el batch y mover al dispositivo
_, predicted = torch.max(output.data, 1) # Obtener la predicción
imshow(images[INDEX], labels[INDEX].item()) # Mostrar la primera imagen del primer batch
print(f'Predicted: {predicted.item()}') # Mostrar la predicción




