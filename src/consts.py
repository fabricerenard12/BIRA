import torch

DEVICE = "cuda" if torch.is_cuda_available() else "cpu"