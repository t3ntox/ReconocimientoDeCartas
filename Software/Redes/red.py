"""
Fichero encargado de crear la red base convolucionada, con dropout

- 3 capas convolucionadas
- 3 capas lineales
- Como criterion se usa CrossEntropyLoss()
- Como optimizer se usa el Adam()
"""



import torch
import torch.nn as nn
import torch.optim as optim

from Software.Utils.utility import seed_everything
from Software.Utils.hiperparametros import *

# Por si no está definido:
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# --- Definición de una CNN simple ---
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=53):
        super(SimpleCNN, self).__init__()
        # Capa 1: convolución + activación + pooling
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        # Capa 2: convolución + activación + pooling
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        # Capas totalmente conectadas
        self.fc1 = nn.LazyLinear(512)
        self.fc2 = nn.LazyLinear(256)
        self.fc3 = nn.Linear(256, num_classes)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.4)

    def forward(self, x):
        # dimension de la imagen de entrada: [B, 3, 32, 32]
        x = self.relu(self.conv1(x))
        # dimensión de la salida de la capa 1: [B, 16, 32, 32]
        x = self.pool(x)
        # dimensión de la salida del pooling: [B, 16, 16, 16]
        x = self.relu(self.conv2(x))
        # dimensión de la salida de la capa 2: [B, 32, 16, 16]
        x = self.pool(x)
        # dimensión de la salida del pooling: [B, 32, 8, 8]
        x = self.relu(self.conv3(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.fc3(x)                      # logits
        return x


# --- Instanciar modelo ---
seed_everything(SEED)
model_cnn = SimpleCNN().to(DEVICE)
# --- Criterio y optimizador ---
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model_cnn.parameters(), lr=LR)
