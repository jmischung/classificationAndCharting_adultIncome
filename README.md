# Adult Income | Classification & Interactive App  

__Date Created:__ 2020-06-16  
__Author:__ Josh Mischung  
__Email:__ josh@knoasis.io  
__Website:__ [knoasis.io](knoasis.io)  
__LinkedIn:__ [www.linkedin.com/in/joshmischung](www.linkedin.com/in/joshmischung)

## Purpose  
__Dataset:__ [Adult Income, UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Adult)  

This repository stores the work performed to build a classification model that will be connected to a user-facing frontend powered by [Plotly-Dash](https://plotly.com/dash/). Once deployed you will be able to interact with the app at knoasis.io/demo (at this point the app is still in development).  

The Adult dataset from the UCI Machine Learning Repository was chosen for this task because a layperson will intuitively have enough understanding of the inputs to change them and mentally form their own hypothesis about how the change will impact the probability of the outcome (*adult income >$50K*).  
<br>  

## Files & Directories
__knoasis\_ds__  
This directory servers as the data-processing package. Functions and classes that prove useful during the process of exploring, manipulating, and modeling the data are moved to a file in this directory and given proper documentation.

__adult\_df\_postEDA.pkl__  
This is a pickle of the dataframe at the end of `adultIncome_nb1_eda.ipynb` with dtype `object` converted to dtype `category` and nulls imputed using variable-specific distributional imputation.  

## Notebooks
__adultIncome\_nb1_eda.ipynb__  
The objective of this notebook is performing imputing NaN and performing initial EDA prior to building a classification model that can power a user-facing frontend.    

__adultIncome\_nb2_classificationModeling.ipynb__  
The objective of this notebook is the initial exploration of various classification algorithms that can power a user-facing frontend where inputs are provide by the user and the probability of an outcome is predicted.  
