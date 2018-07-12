# Deep Learning Basics

I assume that you, like me, don't enjoy having to stare at equations on a blackboard, and would rather be working through exercises that help you understand a subject.

These exercises use toy problems to walk you through the basics of deep learning.  Hopefully, you will find it satisfying to learn the subject by doing experiments and observing how various algorithms fare on the toy problems.

# Teachers' Tips and Notes

The accompanying slides **DeepLearningBasics.pptx** are intended to make it easy for the teachers to teach a course on deep learning.  The slides are colour-coded with instructions to teachers (coded "red") or with material to say ("yellow") and are linked to the exercises here.

The slides can also be used by anyone who's learning the subject by themselves.  They can just go through the slides and the accompanying Pytorch exercises, using the teachers' notes to propel themselves along.

# Getting Started

If you have git installed, download all the exercises by issuing the following command:

*git clone https://github.com/aiaioo/DeepLearningBasicsTutorial/*

If you do not have git installed, just grab the slides **DeepLearningBasics.pptx**.

As you go through the slides, you will be asked to do exercises (for example exercise 980).  You can find a corresponding Jupyter Notebook file (named exercise_980.ipynb) which you can run.

If you have not used Jupyter Notebooks before, they are very easy to use.  Just install jupyter and then start it from the directory where the notebook files are by issuing the command:  jupyter notebook

# Motivation

You are really lucky to be learning (or teaching) machine learning at this time because **deep learning** has made machine learning a **very easy** subject to learn.

The reasons are:

### 1. Very Simple Math

The only math you will need are multiplication and matrices.

If you want to understand the learning algorithms, you will also need partial differentiation, but the frameworks we use these days build the learning algorithm automatically for you.

### 2. Less to Learn

With deep learning, there's *just* one learning algorithm for pretty much everything.

You can use the same learning algorithm and models with relatively minor variations for image processing, speech processing and text processing.

You get 3 for the price of 1.

You can also use the same algorithms for sequential classification that you use for linear classification.

So, it's actually 3 * 2 for the price of 1.

### 3. Little to No Feature Engineering

With un-deep machine learning, you had to do something called *feature engineering*.

For each kind of data you worked with, you had to present the data to the machine learning algorithm in a different way.

For instance, with text, you’d enhance the text with POS tags or parse trees.  With images, you might compute SIFT features.  With speech, you'd compute Cepstral coefficients.  You'd bring a lot of domain expertise to each domain of application.

With deep learning, you don’t need to do much feature engineering.  The deep learning models do it automatically for you.

# The Jupyter Notebook Exercises

This course is organized around a series of Pytorch exercises.  Click on the files ending in .ipynb and they'll open up in your browser.  If you've installed Jupyter Notebook and cloned this Git repository, you can click on each exercise and it will open up in your browser.  You'll be able to run the programs in the exercises directly from your browser (provided you have Pytorch installed).

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

