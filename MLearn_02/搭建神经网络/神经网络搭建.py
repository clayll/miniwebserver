'''
神经网络设计模块化或者叫神经网络设八股

'''

# 前向传播就是搭建网络，设计网络结构
def forward(x, regularizer):
    pass

def get_weight(shape, regularizer):
    pass
    #可以加入正则化

def get_bias(shape):
    pass

# 反向传播就是训练网络，优化网络参数

def backward():
    pass

    '''
    第一步：定义基本样本集
    第二步：定义loss函数: y于Y的差距
    a.loss_mse = tf.reduce_mean(tf.square(y-Y))
    b.ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,lables=tf.argmax(Y,1))
      cem = tf.reduce_mean(ce)
    c.loss=cem 或者 loss_mse + tf.add_n(tf.get_collections("losses")) 
    第三步：指数衰减学习率
    learing_rate = tf.train.exponenitial_decay(
                   LEARNING_RATE_BASE,
                   global_step,
                   样本总数/one_size, 
                   LEARNING_RATE_DECAY,
                   staircase+True)
     第四步：定义减小loss值
     第五步：华东平均
     第六步：训练         
    
    '''



