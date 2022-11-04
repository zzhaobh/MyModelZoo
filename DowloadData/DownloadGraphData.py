from ogb.nodeproppred import DglNodePropPredDataset

dataset = DglNodePropPredDataset(name="ogbn-mag")

split_idx = dataset.get_idx_split()
train_idx, valid_idx, test_idx = split_idx["train"], split_idx["valid"], split_idx["test"]
graph, label = dataset[0]
print(graph, label)