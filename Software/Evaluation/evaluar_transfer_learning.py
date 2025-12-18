"""
Fichero encargado de evaluar la red con transfer learning

Para ello, calcula pesos y desbloquea la última capa
para entrenarla.

Después vuelve a evaluar
"""



from Software.Utils.Graficos import plot_training_history
from Software.Redes.Transfer_Learning import *
from Software.Utils.data import train_loader, test_loader
from Software.Utils.utility import evaluate, train_with_validation
import torch.nn as nn


# --- ETAPA 1: Creación de pesos desde 0 ---
print("\n\n---------------------------------- Inicio del calculo de pesos ----------------------------------")
model_cnn, history = train_with_validation(
    model=model_cnn,
    train_loader=train_loader,
    dev_loader=test_loader,
    criterion=criterion,
    optimizer=optimizer,
    epochs=EPOCHS,
)

#red.model_cnn.load_state_dict(torch.load("../Weights/model_weights_Transfer_Learning.pth"))


# --- ETAPA 2: fine-tuning (desbloquear capas profundas) ---
for name, param in model_cnn.named_parameters():
    if "layer4" in name or "fc" in name:
        param.requires_grad = True


#Creamos un optimizer específico para las capas entrenadas (la final en este caso)
optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, model_cnn.parameters()), lr=LR)


# --- ETAPA 3: Validación Final con Pesos Cargados ---

print("\n\n------------------------ Ejecutando la red con los pesos calculados.... -------------------------")
model_cnn, history = train_with_validation(
    model=model_cnn,
    train_loader=train_loader,
    dev_loader=test_loader,
    criterion=criterion,
    optimizer=optimizer,
    epochs=EPOCHS,
)
plot_training_history(history)

#torch.save(red.model_cnn.state_dict(), "model_weights_Transfer_Learning.pth")

# --- Evaluación final ---
print("\nEvaluación final en test:")
seed_everything(SEED)
acc = evaluate(model_cnn, test_loader)
print(f'Accuracy final en test: {acc:.2f}%')