from tensorflow.keras import callbacks

# first attempt at creating a callback for csv logging
csv_callback = callbacks.Callback.CSVlogger(filename = str(epoch))

# early stopping call back
stop_95 = callbacks.EarlyStopping(monitor='accuracy', restore_best_weights=True)
