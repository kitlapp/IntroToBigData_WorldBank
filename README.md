# Exploring Global Development Trends Using World Bank Indicators: A Data Analysis of Health and Environmental Metrics Across Regions Over the Last Decades

===========================================================================
 
**QUICK NOTE**

Not all files are part of the main project. Some folders contain optional experimental material. The following additional experiments were conducted:
1) Daily Data 1st Approach: "Daily_Mean_Analysis_EXTRA_EXPERIMENTAL_Approach_1"
2) Daily Data 2nd Approach: "Daily_Mean_Analysis_EXTRA_EXPERIMENTAL_Approach_2"
3) Weekly Data: "Weekly_Mean_Analysis_EXTRA_EXPERIMENTAL"

---> The main project script folder is: "MAIN_Project_Hourly_Mean_Analysis" <---


 ===========================================================================

### 1. Introduction

Electricity plays a crucial role in modern life. Energy providers, policymakers, and energy-intensive businesses rely on accurate predictions of energy usage(load) to ensure reliability and cost effectiveness and optimize production. Yet it is not simple to predict. Many factors can affect energy load, including weather, human behavior, and socioeconomic trends. Thus, forecasting models must account for both short- and long-term fluctuations to predict usage trends.  

 This project explores the time-series analysis & analytics of hourly energy demand (MW) for Greece. Incorporating data from 9 additional neighboring countries is done to be exploited in a methodology widely used to refine the accuracy of the final forecast. This is Actual to Forecast (A/F Bias Limitation).


 ===========================================================================

### 2. Files Included

The experimental folders have already been described, while the main project scripts have been defined. Here are the additional general files:
1) README.md
2) ITC6002B1_Duesing_Lappas_Logothetis_Psallida_Project.pdf: The project report
3) ITC6002B1_Duesing_Lappas_Logothetis_Psallida_Project.ppt: The project Power Point presentation
4) GitHub_Guide.pdf (OPTIONAL): A guide with instructions on basic GitHub actions and how to set up GitHub Desktop. This was created to ensure full alignment, and we also included it for convenience.
5) hourly_environment.yml: The Conda environment file for the project, specifying required packages, versions and dependencies.


 ===========================================================================

### 3. How to Set Up the Environment

**OPTION A (using the provided .yml file - Recommended)**
Extract all files to your project directory. Place the .yml file in your user directory, e.g., C:\Users\Your_User_Name. Then:
1) Open Anaconda Prompt
3) Run the following command to create the environment: “conda env create -f hourly_environment.yml -n <Your Environment’s Name>” 
4) Once the environment is created, activate it: “conda activate <Your Environment’s Name>” 
5) Launch Jupyter Lab by typing "jupyter-lab”
6) In Jupyter Lab, navigate to the directory where the project scripts are stored. You can then execute the notebooks and review the results.

**OPTION B (without using our .yml environment file - Not Recommended)**
Assumption: You are an Anaconda user.
1) Open the Anaconda Prompt and run: 
"conda create -n YourEnvName -c conda-forge python=3.12 pandas numpy matplotlib seaborn
scipy statsmodels scikit-learn plotly"
2) Activate your environment and install Jupyter Lab using "conda install -c conda-forge jupyterlab"


 ===========================================================================

### 4. How to Run the MAIN_Project_Hourly_Mean_Analysis Files

1) Keep the data files in the same directory as the .ipynb files to ensure that relative dataset paths work correctly.
2) Execute the notebooks in alphabetical order, based on their filenames: first A, then B, then C and finally E.

All notebooks run without issues. The cleaned dataset generation steps have been commented out to prevent the creation of unexpected files in your project directory.


===== Thank you =====


