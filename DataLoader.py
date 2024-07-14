import torch
from torch.utils.data import Dataset

class DataLoader(Dataset):
    def __init__(self, sequences, labels):
        self.sequences = sequences
        self.labels = labels
    
    
    def len(self):
        return len(self.sequences)
    
    
    def get_item(self, idx):
        sequence = self.sequences[idx]
        label = self.label[idx]
        return torch.tensor(sequence, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)