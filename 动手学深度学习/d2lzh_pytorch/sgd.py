def sgd(params,lr,batch_size):
    for param in params:
        param.data -= lr*param.grad/batch_size  