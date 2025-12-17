# Exploring Global Development Trends Using World Bank Indicators: A Data Analysis of Health and Environmental Metrics Across Regions from 2008 to 2019

 ===========================================================================

### 1. Project Description

World Bank data are well suited for analyzing socioeconomic, health and environmental indicators, among others. Such analyses are commonly used to inform policy design, program planning and the monitoring of development outcomes by international organizations, including the United Nations and the World Bank. While these analyses may be conducted internally, they are also frequently carried out by external partners, such as Data and Technology companies, that support these organizations through data infrastructure development, data management and analytical services.

We selected five health and three environmental indicators. Their metadata descriptions are provided both in main_cleaning_ingestion.ipynb and in the project report.


 ===========================================================================

### 2. Files Included

The experimental folders have already been described, while the main project scripts have been defined. Here are the additional general files:
1) original_data_and_region_mapping folder: It contains the raw data as well as region_list.csv, which was created to map countries to global regions.
2) main_cleaning&ingestion.ipynb: It contains all scripts required for raw data ingestion and cleaning, as well as database creation and table population.
3) custom_functions.py: This file is a companion to main_cleaning_ingestion.ipynb, the notebook cannot be executed without it.
4) countries.csv, indicators.csv and values.csv: These are the exported database tables. They contain cleaned data, as the tables were populated only after the data cleaning process.
5) README.md
6) ITC6002B1_Duesing_Lappas_Logothetis_Psallida_Project.pdf: The project report
7) ITC6002B1_Duesing_Lappas_Logothetis_Psallida_Project.ppt: The project Power Point presentation
8) GitHub_Guide.pdf (OPTIONAL): A guide with instructions on basic GitHub actions and how to set up GitHub Desktop. This was created to ensure full alignment, and we also included it for convenience.
9) hourly_environment.yml: The Conda environment file for the project, specifying required packages, versions and dependencies.


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


