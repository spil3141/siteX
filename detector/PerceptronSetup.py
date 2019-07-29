import numpy as np

class Perceptron:
    learning_rate = None
    n_iteration = None
    randomstate_value = None

    def __init__(self,learning_rate = 0.01,n_iteration = 50,randomstate_value = 1):
        self.learning_rate = learning_rate
        self.n_iteration = n_iteration
        self.randomstate_value = 1

    def Fit(self,X,y):
        #Setting up Random Generator and Initializing Weights
        rgen = np.random.RandomState(self.randomstate_value)
        self.w_ = rgen.normal(loc=0.0,scale = 0.01,size = X.shape[1] + 1)
        self.error_values = []

        #Iterating over the sameples and for each sample compute the generalization
        for _ in range(self.n_iteration):
            error_count = 0
            for xi,target in zip(X,y):
                predicted_value = self.Predict(xi)
                update = self.learning_rate * (target - predicted_value)
                self.w_[1:] += update * xi
                self.w_[0] += update
                error_count += int(update != 0.0) # if the prediction is correct the value of the update variable will be 0 else some other value
            self.error_values.append(error_count)
        return self

    def Net_Input(self,X):
        """Calculate the Net Input"""
        return np.dot(self.w_[1:],X) + self.w_[0] # we add the bias unit to the dot result ( Decision function result / Unit step function ) to do what it does (influencing the decision function)

    def Predict(self,X):
        return np.where(self.Net_Input(X) >= 0.0,1,-1)



# """ Importing and Preprocessing the mnist Training dataset"""
# import pandas as pd
# import numpy as np
# df = pd.read_csv("C:/Users/spil3141/Desktop/siteX/detector/static/detector/externals/mnist_train.csv",header=None)
# data = df.values
# y = []
# X = []
#
# for i in data:
#     if i[:1] == 0:
#         y.append(i[:1])
#         X.append(i[1:])
#     elif i[:1] == 1:
#         y.append(i[:1])
#         X.append(i[1:])
# y = np.asarray(y)
# y = np.where(y == 0,1,-1)
# X = np.asarray(X)
# print("Completed inputting Training dataset")
#
# # Trainign then plotting the Misclassifization to visual the errors
# ppn = Perceptron(learning_rate=0.1,n_iteration=20)
# ppn.Fit(X,y)
#
#//Serializing the Model / Saving the model trained progress
# import joblib
# joblib.dump(ppn,"C:/Users/spil3141/Desktop/siteX/detector/static/detector/externals/Serialized_Perceptron_State.sav")
