# Deep Learning Basics Using Pytorch

If you, like me, learn by doing, this is a course that you might like.  This is a course on deep learning that invites you to experiment on a series of toy data sets (and in the process learn the subject).  Beginners may continue down the rabbit hole; all others may proceed to arxiv.

# Teachers' Tips and Notes

The accompanying slides **DeepLearningBasics.pptx** are for teachers who intend to teach a course on deep learning.  The slides are colour-coded as instructions to teachers ("red"), with narratives to follow ("yellow") and slides to show ("that dark bluish colour").

# Getting the Lessons

If you have git installed, download all the exercises by issuing the following command:

*git clone https://github.com/aiaioo/DeepLearningBasicsTutorial/*

If you do not have git installed, just download everything as a zip file using the "Clone or Download" link.

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

# Exercises 1xx

## Understanding Pytorch Tensors

### Exercise 110

How to create and manipulate tensors using Pytorch and how to visualize a multidimensional space.

# Exercises 2xx

## Layer of Neurons = Affine Transform

### Exercise 210

Building a simple neural network *layer* (an affine transform) using Pytorch.

# Exercises 3xx

## Understanding Classification

### Exercise 310

Turning a neural network layer into a classifier - just add a decision rule!

### Exercise 350

Introducing toy problem 1.

### Exercise 380

That was easy?  Try toy problem 2.

# Exercises 4xx

## Understanding Casting Learning as an Optimization Problem

### Exercise 410

Tool for generating data for toy problems 1 and 2

### Exercise 430

Computing the cross-entropy loss for a single data point

### Exercise 450

Computing the cross-entropy loss for a batch of data

### Exercise 480

Computing the logistic loss for a single data point (an alternative to cross-entropy)

# Exercises 5xx

## Understanding Single-Layer Neural Networks

### Exercise 510

Using the 'loss function' $x^2+3$ to illustrate gradient descent.

### Exercise 530

Gradient descent over generated data set for problem 1.

### Exercise 550

Gradient descent over generated data set for problem 2.

# Exercises 6xx

## Motivating and Learning about Multi-Layer Neural Networks!

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

# Exercises 7xx

## The Back-Propagation Algorithm

### Exercise 710

Let's start learning about backprop.

### Exercise 720

Backprop computation for a different data point (a different x and y -> input and label).

### Exercise 730

Backprop computation for a batch of data points (a set of x and y -> input and label).

### Exercise 740

Backprop using a single data point for a multilayer neural network.

### Exercise 750

Backprop using a batch of data points for a multilayer neural network.

# Exercises 8xx

## Image Classification and Convolutional Neural Networks

### Exercise 810

Classifying images.  Fetching training data (MNIST).

### Exercise 830

Classification of MNIST images using a single-layer neural network.

### Exercise 850

Classification of MNIST images using a multi-layer neural network.

### Exercise 870

Classification of MNIST images using 7 layers in the multi-layer neural network.

### Exercise 890

Classification of MNIST images using convolutional layers (a rough implementation of LeNet Model 5) in the neural network.

# Exercises 9xx

## Text Processing and Recurrent Neural Networks

### Exercise 910

Creating data for demonstrating sequential classification.

### Exercise 920

Sequential classification using an RNN.

### Exercise 980

A sequence to sequence model.