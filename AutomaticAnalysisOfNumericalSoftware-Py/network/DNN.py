from keras.models import Sequential
from keras.layers import Dense

input_size = 64
output_size = 1

train_x = []
train_y = []
test_x = []
test_y = []

# 1. 建立模型
model = Sequential()
model.add(Dense(units=8, input_shape=(64, 1)))
model.add(Dense(units=12))
model.add(Dense(units=12))
model.add(Dense(units=8))

# 2. 均方误差回归问题
model.compile(optimizer='rmsprop', loss='mse')

# 3. 训练模型
batch_size = 1000
epochs = 100

print("Starting training ")
h = model.fit(train_x, train_y, batch_size=batch_size, epochs=epochs, shuffle=True, verbose=1)
print("Training finished \n")

# 4. 评估模型
eval = model.evaluate(test_x, test_y, verbose=0)
print("Evaluation on test data: loss = %0.6f accuracy = %0.2f%% \n" % (eval[0], eval[1] * 100))

# 5. 使用模型预测
test_data = []
predicted = model.predict(test_data)
