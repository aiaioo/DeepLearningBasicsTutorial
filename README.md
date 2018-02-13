# Deep Learning Basics

I assume that you, like me, don't enjoy having to stare at equations on a blackboard, and would rather be working through exercises that help you understand a subject.

These exercises use toy problems to walk you through the basics of deep learning.  Hopefully, you will find it satisfying to learn the subject by doing experiments and observing how various algorithms fare on the toy problems.

# Getting Started

If you have git installed, download all the exercises by issuing the following command:

*git clone https://github.com/aiaioo/DeepLearningBasicsTutorial/*

If you do not have git installed, just grab the slides **DeepLearningBasics.pptx**.

You will be able to commence learning about deep learning immediately.

# Motivation

You are really lucky to be learning (or teaching) machine learning at this time because deep learning has made machine learning a very easy subject to learn.

The only math you will need are multiplication, division and matrices.

If you want to understand the inner working of the deep learning algorithms, then you will also need partial differentiation (and the frameworks we use these days do that automatically for you).

That is all the math you need.

Another thing that makes deep learning easy is the fact that you have a lot fewer algorithms to learn.

When I was a student, we used to take a six month course in NLP to learn to do text processing using machine learning tools.  You’d learn an algorithm or maybe two for training linear classifiers.  Then you’d learn another algorithm for training sequential classifiers, say an HMM (well, actually, you’d learn three algorithms for training HMMs).

But if you wanted to do machine learning on say images or speech, none of those algorithms would help you, and you’d have to learn a whole different subject called computer vision or speech processing which would have been a 6 month course in itself.

With deep learning, you use the same learning algorithm for image processing and speech processing that you use for text processing.

You also use the same core math for sequential models that you use for non-sequential models.

One reason you had so many disciplines was that you had to do something called *feature engineering*.

For each kind of data you worked with, you had to present the data to the machine learning algorithms differently.  With text, you’d throw in POS tags or parse trees.  With images, you might compute SIFT features to allow you to recognize images even if what they contained was rotated or scaled or skewed.  

And to do feature engineering well, you had to develop deep domain expertise – you had to learn linguistics or signal processing.

With deep learning, you don’t need to do much feature engineering.  The deep learning models do a lot of it automatically for you.

So, there is really a lot less to learn.
