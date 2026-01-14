# ReconocimientoDeCartas


Este repositorio contiene el código de una **red neuronal convolucional (CNN)** desarrollada para identificar automáticamente las cartas de la baraja de póker estándar de 52 cartas.

## 📊Dataset
- **Fuente**: [Cards Image Dataset Classification](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification) [Kaggle]     

## 🛠️ Estructura del Proyecto    
```
.idea/                       
Software/                               
  ├── Configuraciones/                          
  │     └── Hiperparámetros y resultados experimentados.                    
  ├── Evaluation/                         
  │     └── Scripts de evaluación, entrenamiento y métricas.                      
  ├── Redes/                          
  │     └── Arquitecturas de CNN y de Transfer Learning.                        
  ├── Utils/                      
  │     └── Funciones auxiliares, utilidades e hiperparámetros.                       
  └── Weights/                          
        └── Pesos de modelos entrenados.
```
## 🛠️ Estructura de la Red

🔹 ENTRADA: Imágenes RGB [batch_size, 3, 32, 32]

🔹 CAPAS CONVOLUTIONALES (3):  
│   Conv1: 3→32 canales (3x3, padding=1) → ReLU → MaxPool(2x2)  
│   Conv2: 32→64 canales (3x3, padding=1) → ReLU → MaxPool(2x2)    
│   Conv3: 64→128 canales (3x3, padding=1) → ReLU → MaxPool(2x2)  

🔹 FLATTEN: [batch_size, 128 * 4 * 4 = 2048]

🔹 CAPAS LINEALES (3):  
│   FC1: LazyLinear→512 → ReLU → Dropout(0.4)  
│   FC2: LazyLinear→256 → ReLU  
│   FC3: Linear(256→53) → logits  

🔹 SALIDA: [batch_size, 53 clases]

ENTRENAMIENTO:  
• Criterion: CrossEntropyLoss()  
• Optimizer: Adam(lr=LR)  
• Device: CUDA/CPU automático  

## 🛠️ Estructura de la Red de Transfer Learning

🔹 BASE: ResNet18 pre-entrenada (ImageNet1K_V1)  
│   • Backbone completo CONGELADO (excepto FC)  
│   • 18 capas convolucionales residuales  
│   • Global Average Pooling antes de FC  
                                                 
## 🔗 Configuraciones disponibles
- [Configuración 1](Software/Configuraciones/Primera/Configuracion.md)
- [Configuración 2](Software/Configuraciones/Segunda/Config.md) 
- [Configuración 3](Software/Configuraciones/Tercera/Configuracion.md)
- [Configuración 4](Software/Configuraciones/Cuarta/Configuracion.md)
- [Configuración 5](Software/Configuraciones/Quinta/Configuracion.md)

## 👥 Desarrolladores

- [@Arael J](https://github.com/xAraelx)
- [@Texenery Bordón Rodríguez](https://github.com/texem4k)
- [@Vidal](https://github.com/t3ntox)

