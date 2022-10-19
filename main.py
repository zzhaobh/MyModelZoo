"""
author：赵泽宇
play model begin！
"""
print("hellow model zoo！")

from DowloadData import DownloadTextData

dataset = DownloadTextData.load_helper(dataset_name="rotten_tomatoes", split="train", download=True, download_dir="./download_datasets")