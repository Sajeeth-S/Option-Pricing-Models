# **Option Pricing Models**

## Table of Contents

- [Introduction](#introduction)
- [Why have I made this?](#why-have-i-made-this)
- [File Structure](#file-structure)
- [Optimisations/Features](#optimisationsfeatures)
- [What have I learnt from this?](#what-have-i-learnt-from-this)
- [Improvements to be made](#improvements-to-be-made)
- [How to use this?](#how-to-use-this)

## Introduction

This project is a deep exploration into the following three foundational option pricing models used in financial derivatives pricing:

- **Black-Scholes Model:** A closed-form solution for pricing European/Binary call and put options, derived using stochastic calculus
- **Binomial Tree Model:** A discrete-time framework that models asset price evolution over multiple time steps, suitable for both European and American options
- **Monte Carlo Simulation:** A flexible numerical method that estimates option prices by simulating thousands of random asset price paths

Each model is derived and explained in detail through Jupyter Notebooks and then implemented in Python. The repository is designed for learning, experimentation, and potential extension into more complex financial modeling.

## Why have I made this?

This project was made to not only help myself gain a deeper mathematical understanding behind option pricing theory, but to also act as a helping hand to those who were in my situation beforehand by acting as a resourceful guide. Moreover, this can also familiarise one with implementing financial models in Python, since I will be thoroughly explaining each step. I did not want to stop at just simply explaining and implementing these models, I also comparatively analysed them to consider what the trade-offs were, whether it be computational performance or real-world limitations. Having made this, I feel not only much more confident in my understanding and ability to apply this theory in the financial market, but also hopeful it helps others in the future.

## Features

Black-Scholes Model:

- Derivation of the Black-Scholes equation and prices of various option types
- Derivation of the Greeks as well as 3D plots to visualise the effect strike price and time to expiry have on the value of an option
- An option value calculator for various option types that also plots a heatmap of the prices to see how small changes to strike price or volatility can affect the price
- An implied volatility calculator which can be used to estimate the volatility of an asset by using the Newton-Raphson method

Binomial Tree Model:

- Derivation of the model from the ground up, including various types of binomial models such as CRR or Chance
- A look into how the Binomial Model converges to the Black-Scholes Model as the number of time steps approaches infinity
- An option value calculator for various option types that also plots a heatmap of the prices to see how small changes to strike price or volatility can affect the price

Monte Carlo Simulation:

- Derivation of how we can use monte carlo simulations to predict the price of an asset and thus the option payoffs
- Implementation into code through 2 methods, a slow way to understand how the model works but also a vectorised method to be computationally more efficient

## Optimisations

- Vectorized all pricing and payoff calculations using NumPy
- Used analytic Greeks where available to reduce computational overhead
- Implemented variance reduction techniques (antithetic variates) in Monte Carlo simulations

## What have I learnt from this?

This project deepened my understanding of both the theory and practical implementation of option pricing models. By deriving these models, I strengthened my knowledge and experience working with stochastic calculus and Itô's Lemma, geometric Brownian motion. But apart from the mathematical side of this, the project also helped with financial principles such as delta hedging and the principle of no-arbitrage. Furthermore, this project has developed by numerical and computational skills since by implementing all the models from scratch, this has reinforced my numerical thinking and debugging techniques. I have also gained more experience with convergence analysis, error estimation, and stability in simulations and applying vectorization and random number generation techniques to optimize performance.

This makes me more confident in my ability to apply this into the practical world and be able to apply each model depending on the market conditions and type of options. Moreover, I have gained a practical foundation for extending to more complex models like Heston, SABR, or stochastic volatility.

## Improvements to be made

- Add support for Exotic Options, ie. Asian Options
- Include more complex models, ie. Heston Model

## File Structure
This repository is split into 3 folders for each of the option pricing models we will cover. For each there will be notebooks pertinent to acting as an educational tool and to learn in detail about each model and both its derivation and implementation. Also, there will be Python files with all the code necessary to run the necessary calculations and plots for each model.

## How to use this?

Firstly, I advise going through the Jupyter Notebooks to understand the derivation and reasoning behind each option pricing model and also how I have gone about implementing the code for it. Then, one could use the Python files to see how to use this on any choice of parameters.

Please ensure the necessary libraries have been imported, the full list can either be seen at the start of the Python file or the top of the notebooks.

