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

## 1. Very Little Math

The only math you will need are multiplication, division and matrices.

If you want to understand the inner working of the deep learning algorithms, then you will also need partial differentiation (and the frameworks we use these days do that automatically for you).

## 2. Less to Learn

Another thing that makes deep learning easy is the fact that you have very few algorithms to learn.

You don't have to learn the math of two or three learning algorithms for linear classification and three more for sequential classification.

With deep learning, there's *just* one learning algorithm for pretty much everything.

Moreover, you came use the same learning algorithm and models with relatively minor variations for image processing and speech processing that you use for text processing.

## 3. No Feature Engineering

One reason you had so many disciplines was that you had to do something called *feature engineering*.

For each kind of data you worked with, you had to present the data to the machine learning algorithms in a different way.  For instance, with text, you’d use POS tags or parse trees.  With images, you might compute SIFT features.  

In order to do feature engineering well, you'd have to develop deep domain expertise.

With deep learning, you don’t need to do much feature engineering.  The deep learning models do it automatically for you.
