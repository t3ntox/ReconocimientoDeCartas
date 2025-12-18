"""
Fichero encargado de crear la red con Transfer Learning

Importa la red resnet18 y desactiva todas las capas excepto la última
para entrenarla

Al cambiar de red, hay que cambiarle en nº de inputs y outputs.
"""



from torchvision.models import resnet18, ResNet18_Weights
from Software.Redes.red import *


model_cnn = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
for param in model_cnn.parameters():
    param.requires_grad = False
for param in model_cnn.fc.parameters():
    param.requires_grad = True

# Reemplaza la capa fc por un nuevo clasificador
in_features = model_cnn.fc.in_features
model_cnn.fc = nn.Sequential(
    nn.Linear(in_features, 256),
    nn.ReLU(),
    nn.Dropout(0.4),
    nn.Linear(256, 53)
)
model_cnn = model_cnn.to(DEVICE)