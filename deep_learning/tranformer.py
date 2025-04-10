from transformers import TFAutoModel
from tenforflow.keras.layers import Dropout

bert_model = TFAutoModel.from_pretrained('bert-base-uncased')

model.add(Dropout(0.3)) # Add dropout layer with 30% dropout rate
