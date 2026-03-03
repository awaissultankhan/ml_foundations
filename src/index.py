import sys
import torch
print(f"Python: {sys.version}")
print(f"M2 GPU Active: {torch.backends.mps.is_available()}")
