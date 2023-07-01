import torch

# Load the PyTorch model
model = torch.load("model.pt")


# Extract the weights from the PyTorch model
weights = model.state_dict()


# Save the weights to a file with the .weights extension
torch.save(weights, "weights.weights")
