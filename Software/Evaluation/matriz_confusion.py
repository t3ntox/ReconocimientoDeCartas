"""
Fichero encargado de crear la matriz de confusión de la red elegida

La matriz de confusión es una matriz de nxn clases (53 en este caso)
en la que se representa con valores enteros que representa donde falla más
1º Se elige la red para analizar


"""



from sklearn.metrics import confusion_matrix
import seaborn as sns

import Software.Redes.red as base_red
import Software.Redes.Transfer_Learning as transfer_learning
from Software.Utils.data import *
from Software.Utils.utility import *
import matplotlib.pyplot as plt


## Evaluación
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


#Red base y Transfer Learning
#Descomentar la red que se quiera evaluar


#model_cnn = base_red.model_cnn.eval()              #-> Red base
model_cnn = transfer_learning.model_cnn.eval()     #-> Red Transfer Learning




all_preds = []
all_labels = []
with torch.no_grad():                   #Se quita el cálculo del gradiente
    for inputs, labels in test_loader:  #Para cada imagen y label
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model_cnn(inputs)     #Inicia predicción
        _, predicted = torch.max(outputs, 1)
        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())
cm = confusion_matrix(all_labels, all_preds)    #Se crea la matriz
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
