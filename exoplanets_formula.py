import numpy as np
from plotnine import *
import pandas as pd
import math
import os
import sys
from ourSolarSystem import *


# Loading dataset
d = pd.read_csv('data/exoplanet.eu_catalog.csv', index_col=0)
df_planets = pd.read_csv('data/solarPlanets.csv')

def clean_exo_dataset(d):
    """Cleans exoplanet dataset.
    
    Args:
        d: data from csv file.
        
    Returns:
        Cleaned dataframe.
    """
    
    exoplanets = pd.DataFrame(d)
    
    # extract most important parameters for our purpose
    exoplanets = exoplanets[["planet_status", "mass", "radius", "orbital_period", "semi_major_axis", "eccentricity", "angular_distance", "discovered", "updated", "tzero_tr", "temp_calculated", "detection_type", "star_name", "star_age", "star_radius", "star_distance", "star_teff", "star_mass"]]

    exoplanets.reset_index(inplace=True)
    exoplanets.index = exoplanets.index + 1


    # which parameters should be NaN-free?
    exoplanets.dropna(subset= ["mass", "radius", "eccentricity", "tzero_tr", "temp_calculated", "star_radius", "star_teff", "star_distance", "star_mass"], inplace=True) # too many NaNs but also relevant factors: "log_g", "angular_distance", "temp_measured", "temp_calculated, "molecules"

    return exoplanets

def habitility_parameters(planet):
    """Calculates habitability parameters.
    
    Args:
        planet: The planet to calcutalte the habitility of.
        
    Returns:
        Mass, distance to habitable zone, orbit of planet
    """
    
    mass = planet["mass"]
    hz = calculate_habitable_zone(planet)
    orbit = planet["eccentricity"]
    
    return mass, hz, orbit


def calculate_habitable_zone(planet):
    """Calculates the distance of a planet to the habitable zone.
    
    Args:
        planet: The planet to calculate the habitable zone of.
        
    Returns:
        Hz distance
    """

    #calculate luminosities
    l_sun = pow(1, 3) # mass of sun = 1
    l_star = pow(planet["star_mass"], 3) # luminosity of star = mass of star to the power of 3

    #calculate distance to habitable zone
    d = math.sqrt(l_star/l_sun) #d = optimal habitable zone, formula from Wikipedia
    star_dist = float(planet["star_distance"]) #actual mean distance to star
    dist_hz = abs(star_dist - d) # difference star_dist to habitable zone

    return dist_hz


def habits_earth(df_planets):
    """Prepares and cleans the solar system planets dataset for habitability analysis.

    Args:
        df_planets (pd.DataFrame): DataFrame containing information about the solar system planets.

    Returns:
        pd.DataFrame: Cleaned DataFrame with necessary columns for habitability analysis.
    """

    # Reset the index of the DataFrame
    df_planets = df_planets.reset_index()

    # Rename the columns for better readability
    df_planets = df_planets.rename(columns={"Unnamed: 0": "# name", "mass (Earth=1)": "mass", "mean distance from Sun (AU)": "star_distance", 
                                          "orbital eccentricity": "eccentricity"}, inplace=False)

    # Select only the necessary columns for habitability analysis
    df_planets = df_planets[["# name", "mass", "star_distance", "eccentricity"]]

    # Add a column for the star mass, which is the same for all planets in the solar system (unity is solar masses)
    df_planets["star_mass"] = 1

    return df_planets


def make_habit_df():
    """Makes habitility dataframe for exoplanets and/or solar system planets.
    
    Args:
        None
        
    Returns:
        :return habitility dataframe with necessary parameters for Formula
    """

    #exoplanet dataframe
    d = pd.read_csv('data/exoplanet.eu_catalog.csv', index_col=0)
    exoplanets = clean_exo_dataset(d) 
    exoplanets = exoplanets[["# name", "mass", "star_distance", "star_mass", "eccentricity"]]
    exoplanets = exoplanets.reset_index(drop=True)

    # solar system dataframe
    solar_system = habits_earth(df_planets) 

    # both dataframes merged
    all_exoplanets = pd.concat([exoplanets, solar_system], axis=0, ignore_index=True) 
    
    #lists for dataframe
    names = []
    masses = []
    hzs = []
    orbits = []
    massr = []

    # filling new dataframe with habitility values
    for planet in all_exoplanets.index: 
        values = habitility_parameters(all_exoplanets.loc[planet])
        names.append(all_exoplanets["# name"][planet])
        masses.append(float(values[0]))
        hzs.append(float(values[1]))
        orbits.append(float(values[2]))
        massr.append(1 if (0.1 < float(values[0])<5.0) else 0) #habitable between 0.1 and 5.0 earth masses

    #naming columns
    data = {"Name": names, 
              "Mass": masses,
              "HZ": hzs,
              "Orbit": orbits,
              "Mass_range": massr}
    habits = pd.DataFrame(data) # actual habitility dataframe

    
    return habits

def plot_habitability(habitable_plot):
    """Plots the 20 most habitable planets and exoplanets

    Args:
        habitable_plot (pd.DataFrame): DataFrame containing information the habitability of planets and exoplanets.

    Returns:
        Printed plot
    """

    # Create the scatter plot
    custom_colors = ["red", "orange", "yellow", "green", "blue"]

    plot1 = (
        ggplot(habitable_plot, aes(x='Name', y='Formula', color='Formula'))
        + geom_point(size=5)
        + scale_y_log10()
        + scale_color_gradient(low=custom_colors[0], high=custom_colors[-1]) # Scale the color gradient of the points using the custom colors defined above
        + theme_minimal() # Using a minimal theme for the plot
        + theme(
        # Adjusting the plot size
        figure_size=(15, 8),
        # Customizing background and text colors
        panel_background=element_rect(fill='black'),
        plot_background=element_rect(fill='black'),
        axis_text_x=element_text(angle=45, hjust=1, color='white'),  # Rotating x-axis labels and setting text color
        axis_text_y=element_text(color='white'),  # Setting y-axis text color 
        axis_title_x=element_text(color='white'),  # Setting x-axis title color 
        axis_title_y=element_text(color='white'),  # Setting y-axis title color 
        legend_title=element_text(color='white'),  # Setting legend title color 
        legend_text=element_text(color='white'), # Setting legend text color
        plot_title=element_text(color='white', size=20), # Setting caption color and size
        plot_caption=element_text(color='white') # Setting caption color
        )
        + labs(title="Most habitable planets and exoplanets") # Setting plot title
        # Setting a caption
        + labs(caption="Note: The formula values are normalised for exoplanets, therefore planets in our solar system have a much higher value and have therefore all been divided by 10 and Earth set to 50 as its value is infinite.")

                            )
    
    return print(plot1)

# make habitility dataframe
habits = make_habit_df() 

#FORMULA is normalized for exoplanets, that´s why values for solar system planets are so high. 
# Values for exoplanets in range 0 (not habitable) to 1 (very habitable).
# Formula based on distance to habitable zone, orbit and mass, normalized for exoplanets
habits["Formula"] = 6.77047/habits["HZ"] * (1-habits["Orbit"]) * habits["Mass_range"] 

# Formula without taking mass into account
habits["Formula_easy"] = 6.77047/habits["HZ"] * (1-habits["Orbit"]) 

# In this small section we adjust the higher values of planets in our solar system to fit into the graph 
# Replacing any infinite values to 50
habits.replace([np.inf], 50, inplace=True)
# Dividing any values over 1 by 10 
habits['Formula'] = np.where(habits['Formula'] > 1, habits["Formula"]/10, habits['Formula'])

# Prints the dataframe, sorted by highest habitability value
print(habits.sort_values(by = "Formula", ascending = False).head(30)) 
# Saves DataFrame to csv file
habits.sort_values(by = "Formula", ascending = False).to_csv('data/habitability.csv')
# Saves the first 20 entries of the DataFrame to variable    
habitable_plot = habits.sort_values(by = "Formula", ascending = False).head(20)

if __name__ == "__main__":

    plot_habitability(habitable_plot)    





    
    




