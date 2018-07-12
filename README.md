# Deep Learning Basics

I assume that you, like me, don't enjoy having to stare at equations on a blackboard, and would rather be working through toy exercises and doing experiments that help you develop an understanding of the subject.

# Teachers' Tips and Notes

The accompanying slides **DeepLearningBasics.pptx** are for teachers who intend to teach a course on deep learning.  The slides are colour-coded with instructions to teachers (coded "red") or with things to say ("yellow").

# Getting the Lessons

If you have git installed, download all the exercises by issuing the following command:

*git clone https://github.com/aiaioo/DeepLearningBasicsTutorial/*

If you do not have git installed, just download everything.

# Installing Jupyter

[Install jupyter.](http://jupyter.org/install)

Start the notebook server from the directory where you downloaded the lessons by issuing the command:

*jupyter notebook*

These lessons will open up in your browser!

# Installing Pytorch

[Install Pytorch.](http://pytorch.org)  Our lessons are based on Pytorch.

# Getting Started

Start with the slides **DeepLearningBasics.pptx**.

As you go through the slides, do the exercises in the Jupyter Notebook files (.ipynb).

# The Jupyter Notebook Exercises

This course is organized around a series of Pytorch exercises.  Click on the files ending in .ipynb and they'll open up in your browser.

You'll be able to run the programs in the exercises directly from your browser.

Below is the gist of each exercise:

### Exercise 110

How to create and manipulate tensors using Pytorch and how to visualize a multidimensional space.

### Exercise 210

Building a simple neural network *layer* (an affine transform) using Pytorch.

### Exercise 310

Turning a neural network layer into a classifier - just add a decision rule!

### Exercise 350

Introducing toy problem 1.

### Exercise 380

That was easy?  Try toy problem 2.

### Exercise 410

Tool for generating data for toy problems 1 and 2

### Exercise 430

Computing the cross-entropy loss for a single data point

### Exercise 450

Computing the cross-entropy loss for a batch of data

### Exercise 480

Computing the logistic loss for a single data point (an alternative to cross-entropy)

### Exercise 510

Using the 'loss function' $x^2+3$ to illustrate gradient descent.

### Exercise 530

Gradient descent over generated data set for problem 1.

### Exercise 550

Gradient descent over generated data set for problem 2.

### Exercise 610

Generating data-set 3 - the XOR function.

### Exercise 630

Can you compute the XOR function using a single-layer neural network?

### Exercise 650

Using non-linear activation functions.

### Exercise 670

Creating a multi-layer neural network using non-linear activation functions.  Can you compute the XOR function using a multi-layer neural network (using a ReLU)?

### Exercise 680

Can you compute the XOR function using a multi-layer neural network (using a Sigmoid activation function)?

### Exercise 690

Can you compute the XOR function using a multi-layer neural network with a bias term (using a Sigmoid activation function)?

### Exercise 695

Can you improve the XOR function using a multi-layer neural network with a bias term (using a ReLU activation function)?

### Exercise 710

Let's start learning about backprop.

