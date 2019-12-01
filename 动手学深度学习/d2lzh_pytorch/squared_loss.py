def squared_loss(y_hat,y):
    return (y_hat - y.view(y_hat.size()))**2 /2