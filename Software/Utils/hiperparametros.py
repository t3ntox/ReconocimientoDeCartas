# --- Configuración Hiperparámetros ---

EPOCHS = 10             #Nº de repeticiones del entrenamiento
LR = 1e-3               #Learning Rate
SEED = 0                #Semilla
BATCH_SIZE =16          #La cantidad de datos o lotes, que podrá analizar la red
FactorReduccion = 0.75  #Proporción en la que se reduce LR
Paciencia = 3           #nº de épocas con peores con peores resultados antes de reducir el LR
LR_red2 = 5e-4          #LR de la 2º red

