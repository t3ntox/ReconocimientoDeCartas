"""
Fichero encargado de obtener las imagenes para analizar

A cada dataset, aplicamos Data Augmentation

Por cierto, en la carpeta de imagenes hya una llamda valid que no hemos usado, igual
deberíamos usarla
"""



from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from Software.Utils.hiperparametros import BATCH_SIZE

train_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

classes = ("AS_T","AS_P","AS_D","AS_C","2_T","2_P","2_D","2_C",
         "3_T","3_P","3_D","3_C","4_T","4_P","4_D","4_C",
        "5_T","5_P","5_D","5_C","6_T","6_P","6_D","6_C",
         "7_T","7_P","7_D","7_C","8_T","8_P","8_D","8_C",
        "9_T","9_P","9_D","9_C","10_T","10_P","10_D","10_C",
         "J_T","J_P","J_D","J_C","Q_T","Q_P","Q_D","Q_C",
        "K_T","K_P","K_D","K_C", "JAJAS")

train_set = datasets.ImageFolder(root='URL de train', transform=train_transform)
test_set = datasets.ImageFolder(root='URL de test', transform=test_transform)

#Mismo Data Augmentation el test
validation_set = datasets.ImageFolder(root='URL de valid', transform=test_transform)

train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=False)
valid_loader = DataLoader(validation_set, batch_size=BATCH_SIZE, shuffle=False)

""" CALCULO NORMALIZACION
dataset = datasets.ImageFolder(
    'C:/UNI/3ºaño/FSI/ReconocimientoDeCartas/DataSet/train',
    transform=transforms.ToTensor()
)
loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=False, num_workers=0)

n_pixels = 0
channel_sum = torch.zeros(3)
channel_squared_sum = torch.zeros(3)

for imgs, _ in loader:
    # Asegura batch_size, canales, alto, ancho
    if imgs.ndimension() != 4 or imgs.shape[1] != 3:
        print("Batch inválido con forma", imgs.shape)
        continue
    imgs = imgs.float()
    n_pixels += imgs.numel() // 3
    channel_sum += imgs.sum(dim=[0, 2, 3])
    channel_squared_sum += (imgs ** 2).sum(dim=[0, 2, 3])

mean = channel_sum / n_pixels
std = (channel_squared_sum / n_pixels - mean ** 2).sqrt()

print("Mean:", mean)
print("Std:", std)
"""
