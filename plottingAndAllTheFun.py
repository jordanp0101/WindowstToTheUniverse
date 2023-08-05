import numpy as np
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd


# Creating exception so user can exit at any point
class ExitProgramException(Exception):
    pass

# Load dataset
df_planets = pd.read_csv('data/solarPlanets.csv')

# Dataset cleanup and preparation
df_planets = df_planets.rename_axis("planets")
df_planets = df_planets.reset_index(drop=True)
df_planets = df_planets.rename(columns={'Unnamed: 0': 'Planet'}, inplace=False)
df_planets['rotation period (in Earth days)'] = df_planets['rotation period (in Earth days)'].str.rstrip('*')
df_planets['rotation period (in Earth days)'] = df_planets['rotation period (in Earth days)'].apply(float)


def display_info(df_planets):
    """Display information about specific planets or attributes of all planets.

    Args: 
        df_planets: dataset of the planets in our solar system
    
    Returns:
        None (Displays information to the user)
    
    """
    
    planet_num = ''     # Variable to store the planet number selected by the user
    info_output = ''    # Variable to store the information to be displayed
    data_or_planet = '' # Variable to store the user's choice of displaying information
    
    # Loop until the user decides to exit ('x')
    while data_or_planet != 'x':

        data_or_planet = input("Type (1) for information on a specific planet and (2) to see attributes about all planets\n"+
                               "Type (x) to exit and (b) to go back\n")

        if data_or_planet == 'x':
            raise ExitProgramException
        
        elif data_or_planet == 'b':
            run_program(df_planets)
    
        elif data_or_planet == "1":
            # User wants information on a specific planet
            planet_num = input('Press: \n' + 
                                '(0) - Mercury\n' +
                                '(1) - Venus\n' +
                                '(2) - Earth\n' +
                                '(3) - Mars\n' +
                                '(4) - Jupiter\n' +
                                '(5) - Saturn\n' +
                                '(6) - Uranus\n' +
                                '(7) - Neptune\n')
            match planet_num:
                case "0":
                    info_output = print(df_planets.loc[[0]].T) 
                case "1":
                    info_output = print(df_planets.loc[[1]].T)
                case "2":
                    info_output = print(df_planets.loc[[2]].T)
                case "3":
                    info_output = print(df_planets.loc[[3]].T)
                case "4":
                    info_output = print(df_planets.loc[[4]].T)
                case "5":
                    info_output = print(df_planets.loc[[5]].T)
                case "6":
                    info_output = print(df_planets.loc[[6]].T)
                case "7":
                    info_output = print(df_planets.loc[[7]].T)
                case 'x':
                    ExitProgramException
                case _:
                    print('Please enter a value from 0 to 7, or alternatively x to exit \n')

        elif data_or_planet == "2":
            # User wants to compare attributes of all planets
            planet_num = input('Press: \n' + 
                                '(0) to compare the spatial attributes\n' +
                                '(1) to compare movement attributes\n' +
                                '(2) to compare planetary attributes\n'+
                                '(x) to exit\n')
            match planet_num:
                case "0":
                    info_output = print(df_planets.iloc[:, [0, 2, 3, 4, 16]])
                case "1":
                    info_output = print(df_planets.iloc[:, [0, 5, 6, 7, 8, 9]])
                case "2":
                    info_output = print(df_planets.iloc[:, [0, 10, 11, 12, 13, 14]])
                case "x":
                    ExitProgramException
                case _:
                    planet_num = input('Please enter either 0, 1, or 2, alternatively x to exit')
        
        else:
            print("Invalid input, only 1, 2, or x are allowed \n")
        
    return print(info_output)



def plot_general(df_planets):
    """Plots different attributes of the planets in the solar system.

    Args: 
        df_planets (pd.DataFrame): Dataset containing information about the planets in our solar system.

    Returns:
        Prints the selected plot.
    
    """
        
   
    correct_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    # Sort the DataFrame based on the correct order of the planets
    df_planets['Planet'] = pd.Categorical(df_planets['Planet'], categories=correct_order, ordered=True)
    df_planets = df_planets.sort_values('Planet')
    # Applying colours to each planet
    custom_colors = ['grey', 'brown', 'navy', 'red', 'green', 'yellow', 'cyan', 'blue']


    # User input to decide which attribute they want to compare
    while True: 
        plot_choice = input('Press: \n' + 
                                '(0) to see a plot of the diameters \n' +
                                '(1) to see a plot of the mass\n' +
                                '(2) to see a plot of the mean distances from the sun\n' +
                                '(3) to see a plot of the orbital periods in earth years\n' +
                                '(4) to see a plot of the orbital eccentricities\n' +
                                '(5) to see a plot of the mean orbital velocities\n' +
                                '(6) to see a plot of the rotation periods in earth days\n' +
                                '(7) to see a plot of the inclination of axes\n' +
                                '(8) to see a plot of the gravities at equators\n' +
                                '(9) to see a plot of the escape velocities\n' +
                                '(10) to see a plot of the mean densities\n' +
                                '... of all planets\n' +
                                '(x) to exit or (b) to go back\n')
        
        if plot_choice == 'x':
            
            raise ExitProgramException
        
        elif plot_choice == 'b':
            run_program(df_planets)
        
        else:

        # match case based on given user input
            match plot_choice:
                case "0":
                    #adjusting plot appearance
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'diameter (Earth=1)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors) #applying custom color scheme
                    #+ scale_y_continuous(limits=(-5,max(df_planets['diameter (Earth=1)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'), # Setting plot background to black
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),  # Setting legend text color to white
                    plot_title=element_text(color='white'),  # Add plot title with white text
                    )
                    + labs(title="Planet mass (Earth=1)")
                    )
                    print(plot1)
                case "1":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'mass (Earth=1)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(0,max(df_planets['mass (Earth=1)']))) # Setting the min and max value shown on y-axis
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet mass (Earth=1)"))
                    print(plot1)
                case "2":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'mean distance from Sun (AU)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(0,max(df_planets['mean distance from Sun (AU)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + ggtitle("Planet mean distance from Sun (AU)")) 
                    print(plot1)
                case "3":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'orbital period (Earth years)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(0,max(df_planets['orbital period (Earth years)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet orbital period (Earth years)")) 
                    print(plot1)
                case "4":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'orbital eccentricity', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(0,max(df_planets['orbital eccentricity'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet orbital eccentricity")) 
                    print(plot1)
                case "5":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'mean orbital velocity (km/sec)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(0,max(df_planets['mean orbital velocity (km/sec)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet mean orbital velocity (km/sec)")) 
                    print(plot1)
                case "6":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'rotation period (in Earth days)', color = 'Planet'))
                    + geom_point(size = 5)
                    + geom_text(aes(label='rotation period (in Earth days)'), va='top',color='white', nudge_y=-8)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(-300,max(df_planets['rotation period (in Earth days)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet rotation period (in Earth days))")) 
                    print(plot1)
                case "7":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'inclination of axis (degrees)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet inclination of axis (degrees)")) 
                    print(plot1)
                case "8":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'gravity at equator (Earth=1)', color = 'Planet'))
                    + geom_point(size = 5)
                    + geom_text(aes(label='gravity at equator (Earth=1)'), va='top',color='black', nudge_y=-8)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(-1,max(df_planets['gravity at equator (Earth=1)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),
                    plot_title=element_text(color='white', size=20)  # Setting legend text color to white
                    )
                    + labs(title="Planet gravity at equator (Earth=1")) 
                    print(plot1)
                case "9":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'escape velocity (km/sec)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + scale_y_continuous(limits=(0,max(df_planets['escape velocity (km/sec)'])))
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),  # Setting legend text color to white
                    plot_title=element_text(color='white', size=20))
                    + labs(title="Planet escape velocity (km/sec)")) 
                    print(plot1)
                case "10":
                    plot1 = (ggplot(df_planets, aes(x='Planet', y = 'mean density (water=1)', color = 'Planet'))
                    + geom_point(size = 5)
                    + scale_color_manual(values=custom_colors)
                    + theme(panel_background=element_rect(fill='black'),
                    plot_background=element_rect(fill='black'),
                    axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color to white
                    axis_text_y=element_text(color='white'),  # Setting y-axis text color to white
                    axis_title_x=element_text(color='white'),  # Setting x-axis title color to white
                    axis_title_y=element_text(color='white'),  # Setting y-axis title color to white
                    legend_title=element_text(color='black'),  # Setting legend title color to white
                    legend_text=element_text(color='black'),  # Setting legend text color to white
                    plot_title=element_text(color='white', size=20))
                    + labs(title="Planet mean density (water=1)")) 
                    print(plot1)
                
                case _: 
                    print("Please enter a number between (0) and (11)") # Invalid input case
            
    
#still need docstring
def run_program(df_planets):
    '''Run the Windows to the Universe program to view information and compare attributes of planets in the solar system.

    Args:
        df_planets (pd.DataFrame): DataFrame containing information about the planets in the solar system.

    Returns:
        None'''
    
    # Initialize info_view variable
    info_view = ''

    # User prompt to select an action
    info_view = input("Welcome to the Windows to the Universe \n" + 
                    'What would you like to do? \n' +
                    'View general information on planets in the solar system (Press 1) \n' +
                    'Compare an attribute across all planets in graphical form (Press 2) \n')


    try:
        while True:  # Infinite loop to keep the program running until 'x' is entered
            if info_view == 'x':
                print("Exiting the program.")
                break  # Break the loop and exit the program if 'x' is entered

            if info_view == '1':
                display_info(df_planets)  # Call the display_info() function
            elif info_view == '2':
                plot_general(df_planets)  # Call the plot_general() function
            else:
                info_view = input("Invalid input. Please enter 1, 2, or x.\n")  # Prompt for valid input
    except ExitProgramException:
        print("Exiting the program.")





if __name__ == "__main__":

    run_program(df_planets) 


   












    







