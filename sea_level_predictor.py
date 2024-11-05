import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    min_year = df['Year'].min()
    x = [min_year+n for n in range(0,2050-min_year+1)]
    y = [lin.slope*val + lin.intercept for val in x]
    ax.plot(x,y,color='r')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    lin = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    x = [2000+n for n in range(0,2050-2000+1)]
    y = [lin.slope*val + lin.intercept for val in x]
    ax.plot(x,y,color='g')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()