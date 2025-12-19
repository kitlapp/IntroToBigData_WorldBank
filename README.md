# Exploring Global Development Trends Using World Bank Indicators: Data Cleaning, Database Creation, and Analysis of Health and Environmental Metrics Across Regions (2008–2019)

NOTE: All files were removed from our personal branches to ensure that no database passwords were accidentally left behind.

 ===========================================================================

### 1. Project Description

World Bank data are well suited for analyzing socioeconomic, health, and environmental indicators, among others. Such analyses are commonly used to inform policy design, program planning, and the monitoring of development outcomes by international organizations, including the United Nations and the World Bank. While these analyses may be conducted internally, they are also frequently carried out by external partners, such as data and technology companies, which support these organizations through data infrastructure development, data management, and analytical services.

For this project, we assume the role of such a company, with the World Bank requesting insights for specific indicators. Accordingly, we selected five health and three environmental indicators. Their metadata descriptions are provided in both main_cleaning.ipynb and the project report.


 ===========================================================================

### 2. Files Included

1) rawData_and_region_mapping: It contains the raw data as well as region_list.csv, which was created to map countries to global regions.
2) main_cleaning.ipynb: It contains all scripts required for raw data ingestion and cleaning, as well as database creation and table population.
3) custom_functions.py: This file is a companion to main_cleaning_ingestion.ipynb, the notebook cannot be executed without it.
4) countries.csv, indicators.csv and values.csv: These are the exported database tables. They contain cleaned data, as the tables were populated only after the data cleaning process.
5) main_analysis.ipynb: This notebook contains all scripts required for the analysis and is fed with the cleaned datasets described above.
6) PandasAnalysis.py: This file is a companion to AnalysisinPandas_andVisualizations.ipynb, the notebook cannot be executed without it.
7) requirements.yml: This file is used to replicate our computing environment on any machine.
8) README.md


 ===========================================================================

### 3. How to Set Up the Environment

These instructions are related to the zipped folder which contains the entire project inside. Alternatively, we included all files separately at GitHub repo: https://github.com/kitlapp/IntroToBigData_WorldBank. Note that main_analysis.ipynb is very large to be uploaded outside of a zipped folder. Therefore, it exists only inside allProjects.zip. We strongly recommend to download the zipped folder and follow the instructions below.

**Use the provided requirements.yml file:**  

Download the zipped folder and extract all files creating your project directory. Open Anaconda Prompt and navigate to the extracted folder (project directory) or provide the full path to it. Then:
1) Run the following command to create the environment: “conda env create -f requirements.yml". Give permissions if prompted. The environment will be created with the name DereeIntroBigData.
2) Once the environment is created, activate it: “conda activate DereeIntroBigData” 
3) Launch Jupyter Lab by typing "jupyter-lab”. The project directory will open directly in Jupyter Lab’s interface.
6) You can then execute the notebooks main_cleaning.ipynb and main_analysis.ipynb to review the results. Please do not change the directory structure, as this may break the paths to the datasets.

**The steps for generating the cleaned datasets have been commented out to prevent creating unexpected files in your project directory. All necessary datasets are already included.**


===== Thank you =====


