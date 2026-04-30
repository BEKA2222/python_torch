from fastapi import FastAPI, UploadFile, File
import io
import uvicorn
import torch
from torchvision import datasets, transforms
import torch.nn as nn

class ClassImage(nn.Module):
 def __init__(self):
    super().__init__()

    self.first = nn.Sequential(
      nn.Conv2d(1, 16, kernel_size=3, padding=1),
      nn.ReLU(),
      nn.MaxPool2d(2)
  )
    self.second = nn.Sequential(
      nn.Flatten(),
      nn.Linear(16 * 14 * 14, 64),
      nn.ReLU(),
      nn.Linear(64, 10)
  )

 def forward(self, x):
   x = self.first(x)
   x = self.second(x)
   return x

check_image_app = FastAPI()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
class ClassImage()


if __name__ == "__main__":
        uvicorn.run(check_image_app, host="127.0.0.1", port=8000)