
---

# Crime Forecast in Vancouver
  - DSCI-522 Group 23
  - Alias: Project Avalon
    
Welcome to the repository for Project Avalon, a part of the DSCI-522 course by Group 23 in the MDS-V Cohort 8 at UBC.

## ⭐️ Project Summary

This project aims to perform statistical analyses on the crimes committed in the City of Vancouver and develop a classification algorithm to determine the types of crime given a set of parameters.

Latest report: [Crime Forecast In Vancouver.pdf](https://github.com/UBC-MDS/project-avalon/blob/main/notebooks/crime_forecasting.pdf)

## 📘 Data Source

[Crime Data Download, the Vancouver Police Department](https://geodash.vpd.ca/opendata/)

## 📋 Dependencies

All required dependencies are listed in this [conda environment file](environment.yaml).

## 🧪 Test Automation

To run tests, execute the following command in the project root directory:
```
python3 tests/run_all_tests.py
```

## 🧑‍💻 How to run the notebook

### Docker/Docker compose (recommended)

Link to [DockerHub Image](https://hub.docker.com/repository/docker/solosynth1/project-avalon/general)

1. Make sure Docker Engine/Desktop is installed and running.
1. Go to the project root folder.
2. Run `docker compose pull && docker compose up` to bring up the container.
4. Use browser to visit http://localhost:8888 and supply the generate token.

**Important Notes:**
- (For Docker Desktop users) The created container will require more than 4GB of RAM to run the analysis notebook. Please ensure the settings in Docker Desktop enables provisioning at least 8GB of RAM to the container.
- (For Apple Silicon users) Please enable the feature "Use Rosetta for x86/amd64 emulation on Apple Silicon" inside the setting menu. Otherwise, the kernel will not be properly run.

### Local conda environment
1. Create a new conda environment based on the provided [YAML file](environment.yaml).
  - Run `conda env create --name avalon --file=environment.yaml`
  - Then switch to `avalon` env by clicking the drop-down, and select `avalon`
    <img width="455" alt="image" src="https://github.com/UBC-MDS/project-avalon/assets/18610590/95c2c615-b7e3-42bd-93ad-a61861bd7d3a">
  - Note:
    - If you need the `avalon` env locally, run  `conda activate avalon`
    - If you added a new package in your local `environment.yaml`, you need to run `conda env update --name avalon --file=environment.yaml` to update your local env.
    - In case that jupyter does not recognize the new conda environment, Install ipykernel's kernel spec thru the following command:
```
conda activate avalon
python -m ipykernel install --user --name avalon --display-name "Python (avalon)"
```
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
- **Our GitHub Project**: [Project Kaban](https://github.com/orgs/UBC-MDS/projects/86)
<img width="1439" alt="image" src="https://github.com/UBC-MDS/project-avalon/assets/18610590/9e46d78d-b383-4413-80a4-fac120a29658">


## 📖 License

This project is released under [MIT License](LICENSE.md).

---
