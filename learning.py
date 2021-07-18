import torch
import torch.nn as nn  # 뉴럴 네트워크를 생성하기 위한 패키지
import torch.optim as optim
import matplotlib.pyplot as plt
import cv2
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import os
import time
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
torch.manual_seed(0)  # 랜덤 시드를 준다
device = 'cuda'

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 4, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(4),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)
        )

        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(4, 8, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(8),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)
        )

        self.layer3 = torch.nn.Sequential(
            torch.nn.Conv2d(8, 16, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(16),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)
        )

        self.layer4 = torch.nn.Sequential(
            torch.nn.Conv2d(16, 32, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU()
        )

        self.layer5 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU()
        )

        self.layer6 = torch.nn.Sequential(
            torch.nn.Conv2d(64, 128, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(128),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)
        )

        self.layer7 = torch.nn.Sequential(
            torch.nn.Conv2d(128, 256, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)
        )

        self.layer8 = torch.nn.Sequential(
            torch.nn.Conv2d(256, 512, kernel_size=2, stride=1, padding=1),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)
        )

        self.fc = torch.nn.Sequential(
            torch.nn.Linear(8192, 4)
        )

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = self.layer5(out)
        out = self.layer6(out)
        out = self.layer7(out)
        out = self.layer8(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out

def deepcall(image):
    image = cv2.resize(image, dsize=(200, 200), interpolation=cv2.INTER_AREA)
    cv2.imwrite( './hi.jpg', image)
    image = torch.FloatTensor(image).to(device)
    image = image.transpose(1, 2)
    image = image.transpose(0, 1)
    image = torch.unsqueeze(image, 0)
    model = CNN().to(device)
    model.load_state_dict(torch.load('./test_model.pth'))

    model.eval().to(device)  # model = 훈련이 완료 된 모델
    with torch.no_grad():
      y_pred = model(image)
    print("y_pred의 값:"+str(y_pred))


