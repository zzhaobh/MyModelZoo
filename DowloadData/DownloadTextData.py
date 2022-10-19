from datasets import load_dataset_builder, load_dataset, get_dataset_split_names, get_dataset_config_names, \
    DownloadManager, Dataset

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
# 获取dataset dict对象的训练数据分片
dataset = load_dataset(path=dataset_name)
dataset["train"]
# 预处理数据
def preprocess_function(examples):
    audio_arrays = [x["array"] for x in examples["audio"]]
    inputs = feature_extractor(
        audio_arrays,
        sampling_rate=16000,
        padding=True,
        max_length=100000,
        truncation=True,
    )
    return inputs
dataset = dataset.map(preprocess_function, batched=True)
# datasets对象转pytorch的dataloader对象
from torch.utils.data import DataLoader
dataset.set_format(type="torch", columns=["input_values", "labels"])
dataloader = DataLoader(dataset, batch_size=4)
"""


def load_helper(url: str = None, dataset_name: str = None, download: bool = True, download_dir: str = None,
                **kwargs) -> Dataset:
    """
    加载数据集合，从url或者dataset，是否下载
    :param download_dir: 下载位置
    :param url: 从http下载
    :param dataset_name: 从hub下载
    :param download: 是否下载
    :return:
    """
    dataset = None
    if dataset_name is not None and download is True:
        dataset = load_dataset(path=dataset_name, data_dir=download_dir, **kwargs)
    elif dataset_name is not None and download is False:
        dataset = load_dataset(path=dataset_name, **kwargs)

    assert dataset is not None
    return dataset


if __name__ == "__main__":
    d = load_helper(dataset_name="rotten_tomatoes", download=True, download_dir="./download_datasets")
    print(type(d))
    print(dir(d))
    for i in d["train"]:
        print(i)
        break
