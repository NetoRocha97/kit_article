**ABSTRACT**

This repository contains the complete experimental package for a study focused on the analysis, characterization, and monitoring of software development activities, particularly issues and pull requests, across multiple projects.
The goal is to process, organize, and analyze data extracted from real-world repositories to better understand the behavior, evolution, and management of production and test projects.

The dataset and scripts are structured to enable full reproducibility of the analyses performed, including data preprocessing, filtering, characterization, and the generation of analytical reports using R and Python.

### 📁 Repository Structure

- **`kit_article/`** — Main directory containing all study-related files, datasets, scripts, and reports.  
  - **`.RData`** — R workspace data, storing variables and objects created during analysis.  
  - **`.Rhistory`** — History of executed R commands.  
  - **`.Rproj.user/`** — RStudio project-specific configuration files.  
  - **`README.md`** — Documentation describing the repository contents and experiment purpose.  
  - **`Step_5.Rproj`** — RStudio project file used to manage and organize the study.  
  - **`data/`** — Folder containing all datasets used in the experiment.  
    - **`Processed_Issues/`** — Processed data related to issue tracking.  
      - `filtered_production_processed_issues.csv` — Filtered processed issues from production projects.  
      - `filtered_test_processed_issues.csv` — Filtered processed issues from test projects.  
      - `processed_issues.csv` — Consolidated dataset of all processed issues.  
      - `filtered_production.py` — Python script for filtering production issue data.  
      - `filtered_test.py` — Python script for filtering test issue data.  
      - **`per_production_project/`** — Individual CSV files for each analyzed production project.  
      - **`per_test_project/`** — Individual CSV files for each analyzed test project.  
    - **`PRs_Monitoring/`** — Data related to pull request (PR) monitoring.  
      - `2_filtered_test_prs_monitoring.csv` — Filtered dataset of test PRs used for monitoring analysis.  
      - `prs_monitoring.csv` — Complete dataset with all monitored PRs.  
      - `filtered_monitoring_test.py` — Python script for preprocessing and filtering monitoring data.  
    - **`PRs_Characterization/`** — Data related to pull request (PR) characterization.  
      - `3_filtered_production_prs_characterization.csv` — Filtered dataset of production PRs for characterization.  
      - `3_filtered_test_prs_characterization.csv` — Filtered dataset of test PRs for characterization.  
      - `prs_characterization.csv` — Combined dataset with all PR characterization data.  
      - `filtered_characterization_prod.py` — Python script for filtering production PR characterization data.  
      - `filtered_characterization_test.py` — Python script for filtering test PR characterization data.  
  - **`reports/`** — R Markdown reports generated during the study.  
    - `characterizing_prs.Rmd` — R Markdown file describing pull request characterization analyses.  
    - `issues_characterization.Rmd` — R Markdown file describing issue characterization analyses.  
    - `monitoring_analysis.Rmd` — R Markdown file for monitoring data analysis.  
    - `rq_answers.Rmd` — R Markdown file containing the answers to the research questions (RQs).  
- **`.gitmodules`** — Git configuration file defining repository submodules.  
- **`README.md`** — Main documentation file providing an overview of the entire repository.

