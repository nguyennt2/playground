from keras.tuner import RandomSearch

tuner = RandomSearch(
    model,
    objective='val_accuracy',
    max_trials=5,
)

tuner.search(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
