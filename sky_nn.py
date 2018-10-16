'''
Skynet Bot Neural Network System v1.01

This utilizes tflearn based on Tensor Flow for Python 3.6

Training will be done with a dataset in CSV format for now. Later we can use more complex methods.


We can gather initial data by randomly running the snake game, and acquiring histories of inputs.
For each move, we can capture everything the snake "sees" and refer back to it later.
So: for Step 1: snake_observations[(0,1,1,3)

A dataset will have the following shape:
1,0,1,1,3 
0,0,1,1,2
1,0,1,2,3

To provide vision to the immediate left, front, right, and back of the snake, as well
as the suggested move (0, 1, 2, or 3 to represent direction choice.)

When this is ran through the neural network, the inputs (1,0,1,2 - not the last element!) will
be inputted into the NN's "sensors" - one for each value, or feature. These will then pass through
a hidden layer in the NN, using TFLearn, and return an output (0,1,2, or 3 to represent movement choice.)


'''

from snake import SnakeGame
from random import randint
import numpy as np
import tflearn
import math
import argparse
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean
from collections import Counter

class SkyNN:
    def __init__(self, initial_games, test_games, goal_steps, lr, filename = 'snake_nn3.tflearn'):
            self.initial_games = initial_games
            self.test_games = test_games
            self.goal_steps = goal_steps
            self.lr = lr
            self.filename = filename
    
    def init_data_population(self, iterations):
        output_data = [] # this is the list of results that will be exported.
        for i in range(0,iterations):
            print("populating")
            # run the game, with random inputs. 
            # generate observations
        return output_data
        
    def train(self, nn_model, test_data):
        print("training complete.")
    
    
    def generate_random_action(self):
        return -1
        
    # ask the model to make a decision given particular observations to plug into the model.
    def make_decision(self, model, observations):
        return -1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter a filename to parse.")
    parser.add_argument("-d", "--data_generate", required=False, nargs = 2, help="Amount of games to run for initial data population, and filename to export into. (e.g. --data_generate dataset1 2000. CSV format is used.")
    parser.add_argument("-m", "--model", required=False, nargs = 2, help="Load a dataset and generate an initial model for that data. USAGE: -m dataset1 nnresults")
    # TBA
    # parser.add_arugment("--transfer", required=False, nargs = 2, help="Transfer learning from one NN to another that integrates more features, without getting rid of learned values. This is for integrating new features without restarting the entire learning process. TBA - not sure how to complete this yet.")
    # https://www.reddit.com/r/MLQuestions/comments/9myo4r/can_i_add_features_to_an_existing_neural_net/
    parser.add_argument("--test", required=False, nargs  = 2, help="run a neural network and see it perform. pair with -g to see visualization. USAGE: --test filename #tests")
    parser.add_argument("-a", "--activation", required=False, default="mean_square", help="Type of activation function to use, as defined by TFLearn. More documentation later.")
    parser.add_argument("-l", "--loss", required=False, default="categorical_crossentropy", help="Type of loss function to use as defined by TFLearn. More documentation later.")
    parser.add_argument("-t", "--train", required=False, nargs = 3, help="Train an existing model and save results. USAGE: filename1: neural network model, filename2: dataset to train from, filename3: filename to export new neural network as.")
    parser.add_argument("-o", "--optimizer", required=False, default="adam", help="Optimizer to use for training. See http://tflearn.org/optimizers/")
    parser.add_argument("-lr", "--learn_rate", required=False, default=0.01, help="DEFAULT: 0.01. learning rate for training purposes (e.g. 0.01)")
    parser.add_argument("-g", "--gui", required=False, default=False, help="DEFAULT: False. Decide whether to display the game's GUI during use.")
    #parser.add_argument("--graph", required=False, default=False, help="create performance/fitness graph for observation upon completion. TBA.")
    
    
    args = parser.parse_args()
    
    #create the neural network
    #nn = SkyNN()
    print("""
          _                     _   
         | |                   | |  
      ___| | ___   _ _ __   ___| |_ 
     / __| |/ / | | | '_ \ / _ \ __|
     \__ \   <| |_| | | | |  __/ |_ 
     |___/_|\_\\__,  |_| |_|\___|\__|
                __/ |               
               |___/    
    """)           
    if(args.train):
        print("Loading Training Session on existing NN with the Following Parameters:")
        print("Neural Net Model: " + args.train[0])
        print("Training Data: " + args.train[1])
        print("Output Model: " + args.train[2])
        print("--Training Parameters [can be changed in args]--")
        print("Activation: " + args.activation)
        print("Optimizer: " + args.optimizer)
        print("Learning Rate: " + str(args.learn_rate))
        print("Loss Function: " + args.loss)
    elif(args.model):
        print("Creating an Initial Model/Train Session with the Following Parameters:")
        print("Dataset: " + args.model[0])
        print("Output Model: " + args.model[1])
        print("--Training Parameters [can be changed in args]--")
        print("Activation: " + args.activation)
        print("Optimizer: " + args.optimizer)
        print("Learning Rate: " + str(args.learn_rate))
        print("Loss Function: " + args.loss)
        print("GUI: " + str(args.gui))
    elif(args.data_generate):
        print("Creating an Initial Dataset with the Following Parameters:")
        print("Output Dataset: " + args.data_generate[0])
        print("Total Iterations: " + args.data_generate[1])
        #print("Epochs (model checkpoint saves): " + args.data_generate[2])
        print("--Training Parameters [can be changed in args]--")
        print("Random Actions: True")
    elif(args.test):
        print("Starting a Test session to See Performance of NN with the Following Parameters:")
        print("Model: " + args.test[0])
        print("--Training Parameters [can be changed in args]--")
        print("Activation: " + args.activation)
        print("Optimizer: " + args.optimizer)
        print("Learning Rate: " + str(args.learn_rate))
        print("Loss Function: " + args.loss)
        print("GUI: " + str(args.gui))
        
        
        