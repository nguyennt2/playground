from tensorflow.keras.layers import SimpleRNN, LSTM, Dense

rnn_model = Sequential()
rnn_model.add(LSTM(50,True,  input_shape=(100, 1)))
rnn_model.add(LSTM(50))
rnn_model.add(Dense(1))

rnn_model.compile(optimizer='adam', loss='mse')
