import torch.nn as nn
from torch import zeros


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout):
        self.linear_1 = nn.Linear(in_features=input_size, hidden_size=hidden_size)
        self.activation = nn.ReLU()
        self.lstm_layers = nn.LSTM(input_size=hidden_size, hidden_size=hidden_size, num_layers=num_layers)
        self.dropout_layer = nn.Dropout(p=dropout)
        self.linear_2 = nn.Linear(num_layers * hidden_size, out_features=1)
    
    
    def forward(self, x):
        batch_size = x.shape[0]
        
        x = self.linear_1(x)
        x = self.activation(x)
        lstm_out, (h_n, c_n) = self.lstm_layers(x)
        x = h_n.permute(1, 0, 2).reshape(batch_size, -1)
        x = self.dropout_layer(x)
        predictions = self.linear_2(x)
        
        return predictions[:, -1]
        
        
    
    
    def loss(self):
        pass
    
    