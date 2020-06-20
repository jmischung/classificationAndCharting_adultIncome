"""
Created on Fri Jun 19
7:00:00 2020
Last Updated: 2020-06-20

@author(s): Josh Mischung


Module Description
-------------------
The `eda` module within the `knoasis_do` package contains functions used to
visually assess distributions and relationships within a dataset.
"""

# Imports
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Environment settings
sns.set(style='ticks', color_codes=True)

# Functions
# ---------

### Data cleaning ###
def distribution_impute(df, col):
    # Record distribution
    attribute_dist = df[col].value_counts(normalize=True)

    # Impute NaN
    nulls = df[col].isna()
    df.loc[nulls, col] = np.random.choice(attribute_dist.index, size=len(df[nulls]),
                                                        p=attribute_dist.values)

    
### Plotting ###
def bar_chart(df, col):
    # Create plotting variables
    plotting_df = df.copy()
    if (plotting_df[col].dtype == int) or (plotting_df[col].dtype == float):
        plotting_df[col].fillna('Null', inplace=True)
    cat_dict = plotting_df[col].value_counts(dropna=False).to_dict()
    x = list(cat_dict.keys())
    y = list(cat_dict.values())
    
    # Create bar chart
    fig = go.Figure(data=[go.Bar(x=x, y=y, text=y, textposition='auto')])
    
    # Label plot
    fig.update_layout(
        title=go.layout.Title(text=f'{col} - Counts by Value'),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(
                              text='Categories')),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(
                              text='Counts')))
    
    # Show bar chart
    fig.show();

    
def grouped_bar_chart(df, feature, target):
    """Produce a plotly based vertical bar chart of feature occurences
    grouped by possible values of target.

    Parameters
    ----------
    df : pandas dataframe
        Typical dataset.

    feature : str, categorical or ordinal  variable
        Column to use for x-axis values of bar chart.

    target : str, categorical or ordinal variable
        Column to use for groupings by feature value.

    Yields
    ------
    plotly grouped bar chart : Bar chart showing occurences of passed in feature grouped
        by passed in target.

    Examples
    --------
    >>> eda.grouped_bar_chart(autos_df, 'cylinders', 'rc_mechanical')
    
    Notes
    -----
    Additional variants of plotly bar charts:
        https://plot.ly/python/bar-charts/
    """

    try:
        assert (type(df) == pd.DataFrame), "ERROR: This function only accepts Pandas DataFrames. Please convert your data to a pd.DataFrame and retry..."
        assert ((type(feature) == str) & (type(target) == str)), "ERROR: Please pass column names as strings..."
        assert (feature in df.columns), "ERROR: The column passed in for feature is not in the passed in dataframe..."
        assert (target in df.columns), "ERROR: The column passed in for target is not in the passed in dataframe..."

    except AssertionError as error:
        print(error)

    else:    
        # Values and counts
        x_vals = df[feature].value_counts().index.tolist()
        y_vals = sorted(df[target].unique().tolist())

        counts_dict = {}
        data = []

        # Create dict of counts by grouping
        for y_val in y_vals:
            counts_dict[y_val] = []
            for x_val in x_vals:
                counts_dict[y_val].append(((df[feature] == x_val) & (df[target] == y_val)).sum())

        # Create list of plotly objects
        for y_val in y_vals:
            data.append(go.Bar(name=y_val, x=x_vals, y=counts_dict[y_val]))

        # Create plot
        fig = go.Figure(data=data)
        fig.update_layout(barmode='group')

        # Label plot
        fig.update_layout(
            title=go.layout.Title(text=f'{feature} Grouped by {target} - Counts by Value'),
            xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(
                                text='Categories')),
            yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(
                                text='Counts')))

        # Show grouped bar chart
        fig.show();
        

def hist_plot(df, col):
    """Produce a pandas-matplotlib based histogram plot with automated calculation
    of number of bins.

    Parameters
    ----------
    df : pandas dataframe
        Typical dataset.

    col : str, continuous variable
        Column to use for histogram.

    Yields
    ------
    matplotlib histogram : Histogram plot showing distribution of passed in feature.

    Examples
    --------
    >>> eda.hist_plot(autos_df, 'perc_profit')
    """

    try:
        assert (type(df) == pd.DataFrame), "ERROR: This function only accepts Pandas DataFrames. Please convert your data to a pd.DataFrame and retry..."
        assert (type(col) == str), "ERROR: Please pass the column name as a string..."
        assert (col in df.columns.tolist()), "ERROR: The column passed is not in the passed dataframe..."

    except AssertionError as error:
        print(error)
    
    else:
        # Create figure
        plt.figure(figsize=(10, 6))
        
        # Create histogram
        df[col].plot(kind='hist')
        
        # Label plot
        plt.title(f"{col} - Histogram")
        plt.xlabel(col)
        plt.show();


def dist_plot(df, col):
    """Produce a seaborn based distribution plot with KDE plot
    imposed on top of histogram plot with automated calculation
    of number of bins.

    Parameters
    ----------
    df : pandas dataframe
        Typical dataset.

    col : str, continuous variable
        Column to use for distribution plot.

    Yields
    ------
    seaborn distribution plot : KDE and histogram plot showing distribution of passed in feature.

    Examples
    --------
    >>> eda.dist_plot(autos_df, 'perc_profit')
    """

    try:
        assert (type(df) == pd.DataFrame), "ERROR: This function only accepts Pandas DataFrames. Please convert your data to a pd.DataFrame and retry..."
        assert (type(col) == str), "ERROR: Please pass the column name as a string..."
        assert (col in df.columns.tolist()), "ERROR: The column passed is not in the passed dataframe..."

    except AssertionError as error:
        print(error)
    
    else:
        # Address Nulls
        null_count = df[col].isna().sum()
        print(f"{null_count} records are null, and not included in the distribution plot.")
        plotting_df = df.loc[df[col].notna(), :]
        
        # Create figure
        plt.figure(figsize=(10, 6))
        
        # Create distribution plot
        sns.distplot(plotting_df[col])
        
        # Label plot
        plt.title(f"{col} - Distribution Plot")
        plt.xlabel(col)
        plt.ylabel("Density")
        plt.show();
        
        
def grouped_box_plot(df, feature, target):
    """Produce a pandas-matplotlib based box plot grouped by
    a specificed feature.

    Parameters
    ----------
    df : pandas dataframe
        Typical dataset.

    feature : str, categorical or ordinal variable
        Column by which to group box plots.

    target : str, continuous variable
        Column to use for box plots.

    Yields
    ------
    matplotlib box plots : Box plots showing distribution of passed in target grouped
        by passed in feature.

    Examples
    --------
    >>> eda.grouped_box_plot(autos_df, 'cylinders', 'perc_profit')
    """

    try:
        assert (type(df) == pd.DataFrame), "ERROR: This function only accepts Pandas DataFrames. Please convert your data to a pd.DataFrame and retry..."
        assert ((type(feature) == str) & (type(target) == str)), "ERROR: Please pass column names as strings..."
        assert (feature in df.columns), "ERROR: The column passed in for feature is not in the passed in dataframe..."
        assert (target in df.columns), "ERROR: The column passed in for target is not in the passed in dataframe..."

    except AssertionError as error:
        print(error)

    else:
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create grouped boxplot
        df.loc[:, [feature, target]].boxplot(by=feature, ax=ax)
        
        # Label plot
        ax.set_title(f"Box plot of {target}") # Plot main title
        plt.xticks(rotation=45)
        ax.set_ylabel(target)
        plt.show();