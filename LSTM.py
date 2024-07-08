import torch.nn as nn


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout):
        self.linear_1 = nn.Linear(in_features=input_size, hidden_size=hidden_size)
        self.activation = nn.ReLU()
        self.lstm_layers = nn.LSTM(input_size=hidden_size, hidden_size=hidden_size, num_layers=num_layers)
        self.dropout_layer = nn.Dropout(p=dropout)
        self.linear_2 = nn.Linear(num_layers * hidden_size, out_features=1)
    
    
    def forward(self, x):
        pass
    
    
    def loss(self):
        pass
    
    