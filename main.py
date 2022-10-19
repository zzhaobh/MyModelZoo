"""
author：赵泽宇
play model begin！
"""
print("hellow model zoo！")

from DowloadData import DownloadTextData
from torch.utils.data import DataLoader

dataset = DownloadTextData.load_helper(dataset_name="rotten_tomatoes", split="train", download=True, download_dir="./download_datasets")

dataset.set_format(type="torch", columns=["text", "label"])
dataloader = DataLoader(dataset, batch_size=4)

for i in dataloader:
    print(i)
    break