"""
Fichero encargado de evaluar la red base

Carga pesos (si conviene) y evalua
"""
from Software.Evaluation.matriz_confusion import matriz_confusion
from Software.Utils.Graficos import plot_training_history
from Software.Utils.data import train_loader, test_loader, valid_loader       # asegúrate que usan normalización y tamaño correctos
from Software.Utils.utility import *
import Software.Redes.red as red

dev_loader = test_loader

seed_everything(SEED)

#Quitar comentario tras ejecutar por primera vez
red.model_cnn.load_state_dict(torch.load("../Weights/model_weights.pth"))

red.model_cnn, history = train_with_validation(
    model=red.model_cnn,
    train_loader=train_loader,
    dev_loader=dev_loader,
    criterion=red.criterion,
    optimizer=red.optimizer,
    epochs=EPOCHS,
)

optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, red.model_cnn.parameters()), lr=LR)

plot_training_history(history)

torch.save(red.model_cnn.state_dict(), "../Weights/model_weights.pth")

# --- Evaluación final ---
print("\nEvaluación final en test:")
seed_everything(SEED)
acc = evaluate(red.model_cnn, dev_loader)
print(f'Accuracy final en test: {acc:.2f}%')

matriz_confusion(red.model_cnn)
