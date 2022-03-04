import numpy as np
import pandas as pd
from copy import deepcopy
from bertopic import BERTopic

df = pd.read_csv('dados.csv')
df.head()
docs = list(df.loc[:, "data"].values)
print(len(docs))

topic_model = BERTopic(language="Portuguese",min_topic_size=2)
topics, probs = topic_model.fit_transform(docs)

topic_model.get_topics()
print(topic_model.get_topics())
representative_docs = topic_model.get_representative_docs(0)
representative_docs1 = topic_model.get_representative_docs(1)
print(representative_docs)
print(representative_docs1)
frequency = topic_model.get_topic_freq()
print(frequency)
print(topic_model.get_topic_info())