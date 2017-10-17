import tensorflow as tf
import random

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def get_features(str):
    return [len(str)]

def lens(strs):
	return [get_features(s) for s in strs]

alens = lens(read_file("arxiv.txt"))
slens = lens(read_file("snarxiv.txt"))

atargets = [[1, 0]] * len(alens)
stargets = [[0, 1]] * len(slens)

inputs = alens + slens
targets = atargets + stargets

pairs = list(zip(inputs, targets))

random.shuffle(pairs)


assert len(inputs) == len(targets)

print("have", len(alens), "arxiv examples and", len(slens), "snarxiv examples")

#W = tf.Variable([.03, .03], dtype=tf.float32, name="weights")
#b = tf.Variable([.03, -.03], dtype=tf.float32, name="biases")
#
#x = tf.placeholder(tf.float32, name="input")
#y = tf.placeholder(tf.float32, name="target")

x = tf.placeholder(tf.float32, [None, 1], name="x")
W = tf.Variable(tf.zeros([1, 2]))
b = tf.Variable(tf.zeros([2]))
#y = tf.matmul(x, W) + b
y = x + b

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 2])


cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

train = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)

init = tf.global_variables_initializer()

sess = tf.Session()
result = sess.run(init)
print(result)
batch_size = 100
for _ in range(100):
    for i in range(len(pairs) // batch_size):
        batch = pairs[i * batch_size: (i + 1) * batch_size]
        x_train, y_train = zip(*batch)
        _, loss_val = sess.run([train, cross_entropy], {x: x_train, y_: y_train})


x_train, y_train = zip(*pairs)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: x_train,
                                      y_: y_train}))

print(sess.run([W, b]))
