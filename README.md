# Windows to the universe 
**by Jordan Peters, Leona Feierabend and Greta Niemeyer (Group 12)**

 ## Installations on Mac

To use this program on your Mac, you need to ensure that you have installed the correct versions of all libraries used. The installations will be done using the 'pip' package manager, which comes with Python. We will guide you through the installation process step-by-step.

### Step 1: Open the Terminal
- Press `Command + Spacebar` on your keyboard to open Spotlight Search.
- Type `Terminal` and press Enter to open the Terminal app.
- The Terminal is a command-line interface that allows you to interact with your Mac using text commands.

### Step 2: Check if Python is Installed (Optional)
- By default, macOS comes with Python pre-installed.
- To check if Python is already installed, type `python3 --version` in the Terminal and press Enter.
- If Python is not installed or the version is outdated, you can download the latest version from the official Python website (https://www.python.org/downloads/).

### Step 3: Install the Required Libraries
- To install the required libraries, use the 'pip' package manager in the Terminal.
- The following packages are required:
  - Numpy (version 1.24.2)
  - Pandas (version 2.0.0)
  - Plotnine (version 0.12.1)
  - Matplotlib (version 3.7.1)
  - Requests (version 1.24.2)
  - BeautifulSoup4 (version 2.29.0)

- To install each library, type the following command in the Terminal and press Enter:
  - For Numpy: `pip install numpy`
  - For Pandas: `pip install pandas`
  - For Plotnine: `pip install plotnine`
  - For Matplotlib: `pip install matplotlib`
  - For Requests: `pip install requests`
  - For BeautifulSoup4: `pip install beautifulsoup4`

- Your Terminal will now download and install the libraries. Wait for each installation to complete before moving on to the next one.

### Step 4: Verify the Installed Library Versions
- After all the installations are complete, you can verify the installed versions of the libraries.
- To check the version of a library, type the following command in the Terminal and press Enter:
  - For example, to check the version of Numpy: `pip show numpy version`
  - Do this for each library you installed to make sure they are the correct versions.

### Step 5: Update a Library (if Needed)
- If you find that any of the installed libraries are not the required versions, you can update them.
- To update a library to the latest version, type the following command in the Terminal and press Enter:
  - For example, to update Numpy: `pip install --upgrade numpy`
  - Replace `numpy` with the name of the library you want to update.
  - Your Terminal will update the library to the latest version.

You have now installed and verified the required libraries to use the program on your Mac. You can now run the program and enjoy its functionalities. If you encounter any issues during installation or while using the program, don't hesitate to search for solutions online or seek help from the Python community.


## Installations on Windows PC

To use this program, you need to ensure that you have installed the correct versions of all libraries used. The installations will be done using the 'pip' package manager, which comes with Python. We will guide you through the installation process step-by-step.

### Step 1: Open the Command Prompt
- Press the `Windows key + R` on your keyboard to open the Run dialog box.
- Type `cmd` or `cmd.exe` in the Run dialog box and press Enter.
- This will open the Command Prompt, which is a terminal-like interface on Windows.

### Step 2: Install Python (if not already installed)
- Before installing the required libraries, ensure you have Python installed on your Windows PC.
- To check if Python is already installed, type `python --version` in the Command Prompt and press Enter.
- If Python is not installed, you can download the latest version from the official Python website (https://www.python.org/downloads/).
- During installation, make sure to check the option to add Python to your PATH so that you can use it from the Command Prompt.

### Step 3: Install the required libraries
- To install the required libraries, use the `pip` package manager in the Command Prompt.
- The following packages are required:
  - Numpy (version 1.24.2)
  - Pandas (version 2.0.0)
  - Plotnine (version 0.12.1)
  - Matplotlib (version 3.7.1)
  - Requests (version 1.24.2)
  - BeautifulSoup4 (version 2.29.0)

- To install each library, type the following command in the Command Prompt and press Enter:
  - For Numpy: `pip install numpy`
  - For Pandas: `pip install pandas`
  - For Plotnine: `pip install plotnine`
  - For Matplotlib: `pip install matplotlib`
  - For Requests: `pip install requests`
  - For BeautifulSoup4: `pip install beautifulsoup4`

- Your terminal will now download and install the libraries. Wait for each installation to complete before moving on to the next one.

### Step 4: Verify the installed library versions
- After all the installations are complete, you can verify the installed versions of the libraries.
- To check the version of a library, type the following command in the Command Prompt and press Enter:
  - For example, to check the version of Numpy: `pip show numpy version`
  - Do this for each library you installed to make sure they are the correct versions.

### Step 5: Update a library (if needed)
- If you find that any of the installed libraries are not the required versions, you can update them.
- To update a library to the latest version, type the following command in the Command Prompt and press Enter:
  - For example, to update Numpy: `pip install --upgrade numpy`
  - Replace `numpy` with the name of the library you want to update.
  - Your terminal will update the library to the latest version.

You have now installed and verified the required libraries to use the program on your Windows PC. You can now run the program and enjoy its functionalities. If you encounter any issues during installation or while using the program, don't hesitate to search for solutions online or seek help from the Python community.

## How to use this program

1. Once you have downloaded the program and saved it on your local device, you will need to open your terminal or command prompt again and use the command 'cd *folder path*' to navigate to where you have saved the file.
2. From here you must first run the program 'ourSolarSystem.py' which will display a dataset of information regarding the planets in our solar system.
  - Type 'python ourSolarSystem.py'
3. Depending on what interests you next, you maybe decide which program to run next, if you would like to compare the data about the solar system planets and see graphical representations on them, then run the program 'plottingAndAllTheFun.py'. If you would prefer to see the values and a scale of how habitable planets in our solar system and exoplanets are, run the program 'exoplanets_formula.py'
  - Type 'python plottingAndAllTheFun.py'
  - Type 'python exoplanets_formula.py'
4. When you are finished with either one, feel free to have a look at the other one.
5. If you would like some more detailed information on this project and an idea of how to interpret the outputs better, please look at the documentation included in the files.



## Here are some general infos regarding the planetary attributes that may be interesting when viewing the datasets

### Planet parameters :
        *Mass (MJup/MEarth)* : mass of the planet
        soon coming Msini (MJup/MEarth) : minimum mass of the planet due to inclination effect
        *Radius (RJup/Rearth)* : radius of the planet
        *Period (day)* : orbital period of the planet
        *a (AU)* : semi-major axis of the planet orbit (major axis of an ellipse is its longest diameter, semi-major axis is one half of the major axis)
        *e* : eccentrity of the planet orbit from 0, circular orbit, to almost 1, very elongated orbit
        i (deg) : inclination of planet orbit, angle between the planet orbit and the sky plane
        *Ang. dist.(arcsec)* : formal star-planet angular separation given by a/Distance (= distance/angle between two point objects as viewed from an observer)
        *Discovery* : year of discovery at the time of acceptance of a paper
        *Update* : date of the update of data
        ω (deg)* : periapse longitude : angle between the periapse and the line nodes in the orbit plane (maybe important?)
        Tperi (JD) : time of passage at the periapse for eccentric orbits
        Tconj(JD) : time of the star-planet upper conjunction
        *T0 (JD) : time of passage at the center of the transit light curve for the primary transit
        T0-sec (JD) : time of passage at the center of the transit light curve for the secondary transit
        λ Ang. (deg) :  sky-projected angle between the planetary orbital spin and the stellar rotational spin (Rossiter-McLaughlin anomaly).
        Impact Param b (%) : minimum, in stellar radius units, of distance of the planet to the stellar center for transiting planets
        TVR (JD) : time of zero, increasing, radial velocity (i.e. when the planet moves toward the observer) for circular orbits
        K (m/s) :semi-amplitude of the radial velocity curve
        *Tcalc (K)* :planet temperature as calculated by authors, based on a planet model
        *Tmeas (K)* : planet temperature as measured by authors
        Hot pt (deg) : longitude of the planet hottest point (cf. equator)
        **Ag : Albedo (Rückstrahlvermögen, maybe helps to detect surface/atmosphere)
        *Log(g)* : Surface gravity
        *Disc./Det Method* : Methods of discovery/detection of the planet (RV, transit, TTV, lensing, astrometry, imaging. The first method is the discovery one.
        Mass Meas method : Method of measurement of the planet mass (RV, astrometry, planet model for direct imaging)
        Radius Meas method : Method of measurement of the planet radius (transit, planet model for direct imaging)
        Alternate names : alternatives names of the same planet
        *Molecules* : Species detected in the planet

                    Number of planets in the system : 5442 planets




### Stellar parameters :
        *Star name :
        α2000 (hh :mm :ss) : Right Ascension
        δ2000 (hh :mm :ss) : Declination
        mV : apparent magnitude in the V band
        mI : apparent magnitude in the I band
        mJ : apparent magnitude in the J band
        mH : apparent magnitude in the H band
        mK : apparent magnitude in the K band
        *Distance (pc) : distance of the star to the observer
        Metallicity : decimal logarithm of the massive elements (« metals ») to hydrogen ratio in solar units  (i.e. Log [(metals/H)star/(metals/H)Sun] )
        Mass (Msun) : star mas in solar units
        Radius (Rsun) : star radius in solar units
        Sp. Type : stellar spectral type
        *Age (Gy) : stellar age
        Teff : effective stellar temperature 
        Detected disc :  (direct imaging or IR excess) disc detected
        Magnetic field (Yes/No) : stellar magnetic field detected

