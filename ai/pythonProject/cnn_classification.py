import tensorflow as tf
import tensorflow_datasets as tfds
import os

BATCH_SIZE = 16
filePath = os.path.join("data", "mnist")

print(filePath)
(train_dataset, test_dataset) = tfds.load("mnist",
                                          data_dir=filePath,
                                          as_supervised=True,
                                          split=["train", "test"])

for images, labels in train_dataset.take(1):
    print(images.shape)
    print(labels.shape)
    break

AUTOTUNE = tf.data.AUTOTUNE
train_dataset = train_dataset.batch(BATCH_SIZE).cache().prefetch(AUTOTUNE)
test_dataset = test_dataset.batch(BATCH_SIZE).cache().prefetch(AUTOTUNE)

callbacks = [
    tf.keras.callbacks.EarlyStopping(monitor="val_loss",
                                     patience=3,
                                     restore_best_weights=True)
]

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(4, kernel_size=2, activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(padding='same'),
    tf.keras.layers.Conv2D(8, kernel_size=2, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(padding='same'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax'),
])

print(model.summary())

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

history = model.fit(train_dataset,
                    epochs=10,
                    callbacks=callbacks,
                    validation_data=test_dataset)

print(model.evaluate(test_dataset))
