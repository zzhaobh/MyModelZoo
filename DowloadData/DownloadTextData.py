from datasets import load_dataset_builder
from datasets import load_dataset
from datasets import get_dataset_split_names
from datasets import get_dataset_config_names
"""
# 加载数据集合
ds_builder = load_dataset_builder("rotten_tomatoes")  # 翻译数据集合
# 数据集合描述
print(ds_builder.info.description)
# 数据的schema信息
print(ds_builder.info.features)
# 数据集合的split分块信息
print(get_dataset_split_names("rotten_tomatoes"))
# 加载数据预分片一个Dataset对象
dataset = load_dataset("rotten_tomatoes", split="train")
# 加载一个DatasetDict对象
dataset_dict = load_dataset("rotten_tomatoes")
# 得到数据集合的子集信息
configs = get_dataset_config_names("PolyAI/minds14")
print(configs)
# 完整的使用数据集合的api接口
mindsFR = load_dataset("PolyAI/minds14", "fr-FR", split="train")
"""

def


