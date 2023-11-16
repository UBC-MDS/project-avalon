
---

# Project Avalon: DSCI-522 Group 23

Welcome to the repository for Project Avalon, a part of the DSCI-522 course by Group 23 in the MDS-V Cohort 8 at UBC.

## ⭐️ Project Summary

This project aims to perform statistical analyses on the crimes committed in the City of Vancouver and develop a classification algorithm to determine the types of crime given a set of parameters.

## 📘 Data Source

[Crime Data Download, the Vancouver Police Department](https://geodash.vpd.ca/opendata/)

## 📋 Dependencies

All required dependencies are listed in this [conda environment file](environment.yaml).

## 🧑‍💻 How to run the notebook

1. (Suggested) Create a new conda environment based on the provided [YAML file](environment.yaml).
  - Run `conda env create --name avalon --file=environment.yaml`
  - Then switch to `avalon` env by clicking the drop-down, and select `avalon`
    <img width="455" alt="image" src="https://github.com/UBC-MDS/project-avalon/assets/18610590/95c2c615-b7e3-42bd-93ad-a61861bd7d3a">
  - Note:
    - If you need the `avalon` env locally, run  `conda activate avalon`
    - If you added a new package in your local `environment.yaml`, you need to run `conda env update --name avalon --file=environment.yaml` to update your local env.
2. Ensure all dependencies are installed.
3. Open Jupyter Notebook or JupyterLab to run the [analysis notebook](milestone_1.ipynb)

## 🌟 Stakeholders

Our team, in alphabetical order:

- **Orix Au Yeung**
- **Ben Chen**
- **Mo Norouzi**
- **Yiwei Zhang**

## 📌 Useful URLs

Here are some handy links for quick access:

- **Course Releases**: [DSCI_522 Course Releases](https://github.ubc.ca/MDS-2023-24/DSCI_522_dsci-workflows_students/tree/master/release)
- **Course Notes**: [Reproducible and Trustworthy Workflows for Data Science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/README.html)
- **Slack Channel**: [522_dsci-workflows on Slack](https://ubc-mds.slack.com/messages/522_dsci-workflows)

## 📖 License

This project is released under [MIT License](LICENSE.md).

---
