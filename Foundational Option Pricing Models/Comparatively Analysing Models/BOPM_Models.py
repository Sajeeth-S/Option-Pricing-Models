# Code for our 3 BOPM Models
# For more information, refer to BOPM_Code.ipynb notebook

# Importing libraries
import numpy as np
from scipy.stats import binom

# First Model where we are given u and d
def BOPM_Fast(S, K, r, q, u, d, T, n, Option_Type):

    # Check to see if we have a valid option type
    if Option_Type not in ('call','put'):
        print('Invalid option type, please enter either \'call\' or \'put\'')
        return
    
    # Calculate time step and discount factor
    dt = T/n
    df = np.exp(-r * dt)
    
    # Calculate our value for 'a'
    ac = np.ceil((np.log(K/S) - (n * np.log(d))) / (np.log(u/d)))
    ap = np.floor((np.log(K/S) - (n * np.log(d))) / (np.log(u/d))) + 1
    
    # Calculate our 2 risk-neutral probabilities
    p1 = (np.exp((r-q) * dt) - d) / (u - d)
    p2 = u * df * p1
    
    # Create our B lambda function
    B = lambda x, n, p: binom(n, p).cdf(x-1)
    
    if Option_Type == 'call':
        # Calculate the inital value of the option if it is a call
        V = (S * (1 - B(ac, n, p2))) - (K * np.exp(-r * T) * (1 - B(ac, n, p1)))
        
    else:
        # Calculate the inital value of the option if it is a put
        V = (K * np.exp(-r * T) * B(ap, n, p1)) - (S * B(ap, n, p2))
    
    # Return the option price at the root
    #print("The value of our {0} option is {1:0.2f}".format(Option_Type,V))
    
    return V

# CRR Model
def BOPM_CRR(S, K, r, q, sigma, T, n, Option_Type):

    # Check to see if we have a valid option type
    if Option_Type not in ('call','put'):
        print('Invalid option type, please enter either \'call\' or \'put\'')
        return
    
    # Calculate time step and discount factor
    dt = T/n
    df = np.exp(-r * dt)
    
    # Calculate our values for u and d
    u = np.exp(sigma * np.sqrt(dt))
    d = 1/u
    
    # Calculate our value for a
    ac = np.ceil((np.log(K/S) - (n * np.log(d))) / (np.log(u/d)))
    ap = np.floor((np.log(K/S) - (n * np.log(d))) / (np.log(u/d))) + 1
    
    # Calculate our 2 risk-neutral probabilities
    p1 = (np.exp((r-q) * dt) - d) / (u - d)
    p2 = u * df * p1
    
    # Create our B lambda function
    B = lambda x, n, p: binom(n, p).cdf(x-1)
    
    if Option_Type == 'call':
    	# Calculate the inital value of the option if it is a call
        V = (S * (1 - B(ac, n, p2))) - (K * np.exp(-r * T) * (1 - B(ac, n, p1)))
        
    else:
        # Calculate the inital value of the option if it is a put
        V = (K * np.exp(-r * T) * B(ap, n, p1)) - (S * B(ap, n, p2))
    
    # Return the option price at the root
    #print("The value of our {0} option is {1:0.2f}".format(Option_Type,V))
    
    return V

# Chance Model
def BOPM_Chance(S, K, r, q, sigma, T, n, p, Option_Type):

    # Check to see if we have a valid option type
    if Option_Type not in ('call','put'):
        print('Invalid option type, please enter either \'call\' or \'put\'')
        return
    
    # Calculate time step and discount factor
    dt = T/n
    df = np.exp(-r * dt)
    
    # Calculate our values for u and d
    temp1 = np.exp((sigma*np.sqrt(dt))/(np.sqrt(p*(1-p))))
    u = (np.exp(sigma * dt)*temp1)/((p*temp1)+1-p)
    d = np.exp(sigma * dt)/((p*temp1)+1-p)
    
    # Calculate our value for a
    ac = np.ceil((np.log(K/S) - (n * np.log(d))) / (np.log(u/d)))
    ap = np.floor((np.log(K/S) - (n * np.log(d))) / (np.log(u/d))) + 1
    
    # Calculate our 2 risk-neutral probabilities
    p1 = (np.exp((r-q) * dt) - d) / (u - d)
    p2 = u * df * p1
    
    # Create our B lambda function
    B = lambda x, n, p: binom(n, p).cdf(x-1)
    
    if Option_Type == 'call':
        # Calculate the inital value of the option if it is a call
        V = (S * (1 - B(ac, n, p2))) - (K * np.exp(-r * T) * (1 - B(ac, n, p1)))
        
    else:
        # Calculate the inital value of the option if it is a put
        V = (K * np.exp(-r * T) * B(ap, n, p1)) - (S * B(ap, n, p2))
    
    # Return the option price at the root
    #print("The value of our {0} option is {1:0.2f}".format(Option_Type,V))
    
    return V