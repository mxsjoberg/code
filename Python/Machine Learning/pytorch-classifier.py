import os
import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from tqdm import tqdm

# CIFAR10
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
# download datasets
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)
# define classes
classes = ("plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")

# use cuda if available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Running on: {str(device).upper()}")

# convolutional neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # layers
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
          
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
          
        return x
          
net = Net()
net = net.to(device)

if __name__ == "__main__":
    # loss function
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    # train
    for epoch in range(1):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # data is list of [inputs, labels]
            inputs, labels = data[0].to(device), data[1].to(device)
            # zero parameter gradients
            optimizer.zero_grad()
            # forward -> backward -> optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            # stats (print every 2000-th)
            running_loss += loss.item()
            if i % 2000 == 1999:
                print(f"[{epoch + 1}, {i + 1}] loss: {running_loss / 2000}")
                running_loss = 0.0

    # save model
    # torch.save(net.state_dict(), "./cifar10.pth")

    # evaluate
    # correct = 0
    # total = 0
    # with torch.no_grad():
    #     for data in testloader:
    #         images, labels = data[0].to(device), data[1].to(device)
    #         outputs = net(images)
    #         _, predicted = torch.max(outputs.data, 1)
    #         total += labels.size(0)
    #         correct += (predicted == labels).sum().item()
    # detailed
    class_correct = list(0. for i in range(10))
    class_total = list(0. for i in range(10))
    with torch.no_grad():
        for data in testloader:
            images, labels = data[0].to(device), data[1].to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs, 1)
            c = (predicted == labels).squeeze()
            for i in range(4):
                label = labels[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1

    # print(f"Accuracy: {100 * correct / total}%")
    for i in range(10):
        print(f"accuracy of {classes[i]}: {100 * class_correct[i] / class_total[i]}%")
        # accuracy of plane: 53.2%
        # accuracy of car: 65.4%
        # accuracy of bird: 29.8%
        # accuracy of cat: 19.3%
        # accuracy of deer: 32.9%
        # accuracy of dog: 55.7%
        # accuracy of frog: 71.2%
        # accuracy of horse: 55.7%
        # accuracy of ship: 64.0%
        # accuracy of truck: 49.8%
