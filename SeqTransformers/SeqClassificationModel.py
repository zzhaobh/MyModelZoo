from transformers import AutoModelForSequenceClassification, AutoTokenizer
"""
# 加载模型的方式有两种
#一种是从config文件解析初始化，可以加载预训练config，也可以自己设置config
from transformers import AutoConfig, AutoModelForSequenceClassification
# 下载初始化config对象
# Download configuration from huggingface.co and cache.
config = AutoConfig.from_pretrained('bert-base-cased')
model = AutoModelForSequenceClassification.from_config(config)
#一种是直接加载预训练模型
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
#################################################################
from transformers import BertModel, BertConfig
# 直接从BertConfig对象初始化自己设定参数
configuration = BertConfig(vocab_size=30522, hidden_size=768, num_hidden_layers=12, num_attention_heads=12, 
intermediate_size=3072, hidden_act='gelu', hidden_dropout_prob=0.1, attention_probs_dropout_prob=0.1, 
max_position_embeddings=512, type_vocab_size=2, initializer_range=0.02, layer_norm_eps=1e-12, pad_token_id=0, 
gradient_checkpointing=False, position_embedding_type='absolute', use_cache=True,)
# 通过config对象初始化模型
model = BertModel(configuration)
# 提取模型confid
configuration = model.config
"""


def bert_model(model_name: str = "bert-base-uncased"):
    """
    加载bert model，输出model和tokenizer
    Args:
        model_name: 模型在hub上名字

    Returns:

    """
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return model, tokenizer
