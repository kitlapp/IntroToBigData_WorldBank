# Exploring Global Development Trends Using World Bank Indicators: A Data Analysis of Health and Environmental Metrics Across Regions from 2008 to 2019

 ===========================================================================

### 1. Project Description

World Bank data are well suited for analyzing socioeconomic, health and environmental indicators, among others. Such analyses are commonly used to inform policy design, program planning and the monitoring of development outcomes by international organizations, including the United Nations and the World Bank. While these analyses may be conducted internally, they are also frequently carried out by external partners, such as Data and Technology companies, that support these organizations through data infrastructure development, data management and analytical services.

We selected five health and three environmental indicators. Their metadata descriptions are provided both in main_cleaning_ingestion.ipynb and in the project report.


 ===========================================================================

### 2. Files Included

1) original_data_and_region_mapping folder: It contains the raw data as well as region_list.csv, which was created to map countries to global regions.
2) main_cleaning&ingestion.ipynb: It contains all scripts required for raw data ingestion and cleaning, as well as database creation and table population.
3) custom_functions.py: This file is a companion to main_cleaning_ingestion.ipynb, the notebook cannot be executed without it.
4) countries.csv, indicators.csv and values.csv: These are the exported database tables. They contain cleaned data, as the tables were populated only after the data cleaning process.
5) AnalysisinPandas_andVisualizations.ipynb: This notebook contains all scripts required for the analysis and is fed with the cleaned datasets described above.
6) PandasAnalysis.py: This file is a companion to AnalysisinPandas_andVisualizations.ipynb, the notebook cannot be executed without it.
7) requirements.yml: This file is used to replicate our computing environment on any machine.
8) README.md


 ===========================================================================

### 3. How to Set Up the Environment

**Use the provided requirements.yml file**
Extract all files creating your project directory. Open Anaconda Prompt and navigate to the directory where the .yml file is located (or provide the full path to it). Then:
1) Run the following command to create the environment: “conda env create -f requirements.yml". The environment will be created with the name DereeIntroBigData.
2) Once the environment is created, activate it: “conda activate DereeIntroBigData” 
3) Launch Jupyter Lab by typing "jupyter-lab”
6) In Jupyter Lab, navigate to the directory where the project scripts are stored. You can then execute the notebooks and review the results.


 ===========================================================================

### 4. How to Run the 2 .ipynb Files

Provided that you have kept the directory structure exactly as it was extracted:
1) Restart kernel and run all cells of main_cleaning&ingestion.ipynb
2) Restart kernel and run all cells of AnalysisinPandas_andVisualizations.ipynb

**The steps for generating the cleaned datasets have been commented out to prevent creating unexpected files in your project directory. All necessary datasets are already included.**


===== Thank you =====


