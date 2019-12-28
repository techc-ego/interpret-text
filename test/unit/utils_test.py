from utils_nlp.models.bert.sequence_classification import BERTSequenceClassifier
from utils_nlp.dataset.multinli import load_pandas_df


def get_mnli_test_dataset():
    DATA_FOLDER = "./temp"
    df = load_pandas_df(DATA_FOLDER, "train")
    df = df[df["gold_label"] == "neutral"]  # get unique sentences
    TEXT_COL = "sentence1"
    return df[TEXT_COL][:50]


def get_bert_model():
    NUM_LABELS = 2
    cache_dir = "./temp"
    classifier = BERTSequenceClassifier(
        language="bert-base-uncased", num_labels=NUM_LABELS, cache_dir=cache_dir
    )
    return classifier.model