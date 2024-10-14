#import torch
#import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
#import pathlib
import sys
import time
from logging import log


transform = transforms.Compose(
    [transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])]
)

batch_size = 1

trainset = ''
flag = 0
while trainset == '' and flag < 10:
    flag += 1
    print(flag)
    try:
        trainset = CIFAR10(
            root='./data',
            train=True,
            download=True,
            transform=transform,
        )
        break
    except Exception as ex:
        print("Exception", ex, file=sys.stdout)
        log.exception(ex)
        time.sleep(5)
        continue
print("trainset done")

trainloader = ''
flag = 0
while trainloader == '' and flag < 10:
    flag += 1
    print(flag)
    try:
        trainloader = DataLoader(
            trainset, batch_size=batch_size, shuffle=True, num_workers=0,
        )
        break
    except:
        print("connection refused")
        time.sleep(5)
        print("awaken and continue")
        continue
print("trainloader done")

# trainloader = DataLoader(
#     trainset, batch_size=batch_size, shuffle=True, num_workers=0,
# )

#
# testset = CIFAR10(
#     root='./data',
#     train=False,
#     download=True,
#     transform=transform,
# )
#
# testloader = DataLoader(
#     testset, batch_size=batch_size, shuffle=False, num_workers=0,
# )
#
# classes = (
#     'plane', 'car', 'bird', 'cat', 'deer',
#     'dog', 'frog', 'horse', 'ship', 'truck'
# )





# ------------------------------------------------------------------------------------------------

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
