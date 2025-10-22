**ABSTRACT**

This repository contains the complete experimental package for a study focused on the analysis, characterization, and monitoring of software development activities, particularly issues and pull requests, across multiple projects.
The goal is to process, organize, and analyze data extracted from real-world repositories to better understand the behavior, evolution, and management of production and test projects.

The dataset and scripts are structured to enable full reproducibility of the analyses performed, including data preprocessing, filtering, characterization, and the generation of analytical reports using R and Python.

### 📁 Repository Structure

- **`Experiment Kit/`** — Main directory containing all study-related files.  
  - **`Experiment/`** — Core directory containing experiment data, scripts, and reports.  
    - **`.RData`** — Saved R workspace data (variables and objects).  
    - **`.Rhistory`** — Log of executed R commands.  
    - **`.Rproj.user/`** — RStudio user-specific project settings.  
    - **`README.md`** — Local documentation for the Experiment folder.  
    - **`Step_5.Rproj`** — Main RStudio project configuration file.  
    - **`data/`** — Folder containing all datasets used in the study.  
      - **`Processed_Issues/`** — Processed issue-tracking data and related scripts.  
      - **`PRs_Monitoring/`** — Data and scripts related to pull request monitoring.  
      - **`PRs_Characterization/`** — Data and scripts related to pull request characterization.  
    - **`reports/`** — R Markdown files used for analyses and reporting.  
      - `characterizing_prs.Rmd` — Pull request characterization analysis.  
      - `issues_characterization.Rmd` — Issue characterization analysis.  
      - `monitoring_analysis.Rmd` — Monitoring analysis of PRs.  
      - `rq_answers.Rmd` — Answers to research questions (RQs).  
- **`.gitmodules`** — Git configuration for submodules.  
- **`README.md`** — Main documentation file with project overview and usage instructions.
