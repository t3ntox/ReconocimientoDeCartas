"""
Fichero que aloja dependencias y funciones varias.
"""



import numpy as np
import torch
import torch.nn.functional as F
from Software.Utils.hiperparametros import *


def seed_everything(seed):
    """ Verifica que todos los pesos y valores 'pseudoaleatorios'
        siempre sean los mismos, así se podrá obtener los 'mismos'
        valores
    """

    import random
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False





def evaluate(model, test_loader):
    """
    Función que evalúa el modelo

    :param model: El propio modelo inteligente
    :param test_loader: Dataset para testear
    :return Precisión: obtenida
    """

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.eval()  # Poner el modelo en modo evaluación
    correct = 0
    total = test_loader.dataset.__len__()  # Total de muestras en el conjunto de test
    with torch.no_grad():  # No calcular gradientes
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)  # Mover datos al dispositivo
            outputs = model(inputs)  # Forward pass
            _, predicted = torch.max(outputs, 1)  # Obtener las predicciones
            correct += (predicted == labels).sum().item()  # Actualizar el contador de aciertos
    accuracy = 100 * correct / total if total > 0 else 0.0
    return accuracy



def train_with_validation(model, train_loader, dev_loader, criterion, optimizer, epochs):
    """
    Función principal que evalua y calcula los resultados
    :param model: Modelo red neuronal
    :param train_loader: Dataset para entrenar el modelo
    :param dev_loader: Dataset para evaluar el modelo
    :param criterion: Función de pérdida, mide que tan mal lo hace el modelo
    :param optimizer: Componente que ajusta pesos en función a unos parámetros
    :param epochs: Nº de repeticiones del entrenamiento
    :returns: 'model' 'history' -> Devuelve el modelo y el historial de resultados obtenidos
    """

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    history = {'train_loss': [], 'train_acc': [], 'dev_loss': [], 'dev_acc': []}

    # Scheduler (agrega aquí)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=FactorReduccion, patience=Paciencia)

    for epoch in range(epochs):
        model.train()
        running_loss, correct, total = 0.0, 0, 0

        for inputs, labels in train_loader:
            optimizer.zero_grad()
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

        avg_train_loss = running_loss / max(1, len(train_loader))
        train_acc = 100.0 * correct / max(1, total)

        # Validación (loss y accuracy)
        model.eval()
        dev_running_loss = 0.0
        with torch.no_grad():
            for inputs, labels in dev_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                n_classes = outputs.shape[1]
                labels_one_hot = F.one_hot(labels, num_classes=n_classes).float()
                dev_loss = criterion(outputs, labels_one_hot)
                dev_running_loss += dev_loss.item()
        avg_dev_loss = dev_running_loss / max(1, len(dev_loader))
        dev_acc = evaluate(model, dev_loader)

        # Guarda histórico
        history['train_loss'].append(avg_train_loss)
        history['train_acc'].append(train_acc)
        history['dev_loss'].append(avg_dev_loss)
        history['dev_acc'].append(dev_acc)

        # Scheduler: actualiza usando la accuracy de validación
        scheduler.step(dev_acc)

        print(f'[Epoch {epoch + 1}] '
              f'train_loss: {avg_train_loss:.3f} | train_acc: {train_acc:.2f}% | '
              f'dev_loss: {avg_dev_loss:.3f} | dev_acc: {dev_acc:.2f}% | lr={optimizer.param_groups[0]["lr"]:.6f}')

    return model, history

