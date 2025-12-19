import torchvision

import Software.Utils.utility as util
import matplotlib.pyplot as plt
import numpy as np

from Software.Utils.data import *

# --- Información sobre el dataset ---
print("\n--- Información del dataset ---")
print(f"Número de imágenes de entrenamiento: {len(train_set)}")
print(f"Número de imágenes de prueba: {len(test_set)}")
print(f"Tamaño de una imagen: {train_set[0][0].shape}")  # (3, 32, 32) -> RGB 32x32

# --- Obtener algunas imágenes del loader ---
dataiter = iter(train_loader)
images, labels = next(dataiter)

print("\n--- Información del batch ---")
print(f"Dimensión del batch de imágenes: {images.shape}")  # (batch_size, canales, alto, ancho)
print(f"Dimensión del batch de etiquetas: {labels.shape}")

# --- Función para mostrar imágenes ---
def imshow(img):
    img = img / 2 + 0.5     # Desnormalizar
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.axis('off')
    plt.show()

# --- Mostrar imágenes y etiquetas ---
imshow(torchvision.utils.make_grid(images))
