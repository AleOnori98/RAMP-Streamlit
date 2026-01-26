# **RAMP Demand Simulator – Streamlit Application**
*A lightweight, interactive workflow for generating high-resolution load demand profiles using the RAMP framework.*

<p align="center">
  <img src="config/assets/ramp.png" width="320" alt="RAMP for Bottom-Up Load Demand Simulation">
</p>

The **RAMP Demand Simulator** is a fully interactive Streamlit application designed to simplify the entire workflow of preparing inputs, generating daily stochastic demand profiles, assembling a synthetic “full year,” and visualizing the resulting minute-resolution curves.  
Instead of manually preparing multiple spreadsheets and calling Python scripts, this interface guides the user through a clean, intuitive, and reproducible process. With RAMP’s stochastic engine under the hood and Streamlit providing an intuitive UI, the tool enables fully transparent and modular bottom-up load simulation at **one-minute resolution**.


---

# **Features**

The application provides an end-to-end modelling pipeline:

### **Flexible time-structure definition**
Users can configure the structure of the year in a natural, human-friendly way:
- 1–4 **seasons**, with freely assigned calendar months  
- Optional **within-week differentiation**, such as:
  - *Weekday vs Weekend*
  - Custom week-classes (up to 7)
- Each combination of *(season × week-class)* defines a **day archetype**

### **Input building directly from a RAMP Excel file**
- Upload RAMP input files (one per archetype or a single one for the whole year)
- The app automatically expands each into a **full RAMP-compatible Excel**, exactly as required by `ramp.core`
- Configurations are saved so they persist across sessions

### **Two simulation modes**
The app supports both workflows typically used in RAMP:

**Single-archetype mode**  
A single input file is used for the whole year. RAMP generates `num_days` independent daily profiles and the app fits them to a 365-day matrix.

**Multi-archetype mode**  
Each archetype corresponds to one stochastic pool (season × week-class).  
A synthetic year is assembled day-by-day by selecting a random day from the appropriate pool.

### **Rich data visualization**
- Daily average curve at minute resolution  
- Cloud of all days + min–max variability band  
- Seasonal / weekly filtering (if defined)  
- Inspect any specific simulated day  
- Hourly averages with downloadable CSVs  
- Automatic support for aggregated vs per-category curves

<p align="center">
  <img src="docs/images/workflow_diagram.png" width="650" alt="Workflow Diagram">
</p>

These plots provide an immediate, intuitive understanding of behavioural variability, peak periods, and seasonal patterns.

### **Clean output structure**
All outputs are automatically generated in tidy CSV files, making integration with energy system models (e.g., MicroGridsPy, OSeMOSYS, PyPSA, Autarky) immediate.

---

# **📁 Repository Structure**
```bash

project/
│
├── app.py # Main Streamlit application
├── config/
│ ├── ramp_template.xlsx 
│ ├── path_manager.py # 
│ └── assets/ # Logo and UI images
│
├── core/
│ ├── utils.py # Helper utilities
│ └── ramp_core.py # Orchestration of RAMP execution
│
├── inputs/
│ ├── archetypes/ # Generated archetype Excel files
│ ├── year_structure.yaml # Saved configuration
│ └── ramp_input.xlsx # Full single-archetype input
│
├── outputs/
│ ├── profile_*.csv # Per-category final daily profiles
│ └── profile_aggregated.csv # Final aggregated (365×1440)
│
├── requirements.txt
└── environment.yaml

```

---

# **Inputs**

### **RAMP Input Excel**
A structured spreadsheet containing:
- Category name  
- Appliance attributes  
- Usage windows and probabilities  
- Stochastic behaviour parameters  

A ready-to-use example can be found in:  
**examples/RAMP Excel Inputs Example.xlsx**

### **Year Structure Configuration**
Automatically saved to:
**inputs/year_structure.yaml**

### **Archetype Metadata**
Automatically saved to:
**inputs/archetype_configs.json**

---

# **Outputs**

Outputs are produced in **CSV format** for readability and compatibility.

### **Per user category**
`profile_<category>.csv`  
Shape: **365 × 1440** (days × minutes)

### **Aggregated daily demand**
`profile_aggregated.csv`  
Shape: **365 × 1440**

### **Optional hourly file**
`profile_aggregated_hourly.csv`  
Shape: **365 × 24**

These files can be directly used in MicroGridsPy and other energy modelling frameworks.

# **⚙ Installation**

## **A) Using pip + requirements.txt**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## **B) Using Conda + environment.yaml**
```bash
conda env create -f environment.yaml
conda activate ramp_app
```

---

# **🚀 Running the Streamlit App**
From the project root:
```bash
streamlit run app.py
```
The app will open automatically in the browser, or you can visit:
```bash
http://localhost:8501
```

# 👥 Contacts"

**Alessandro Onori**  
📧 [alessandro.onori@polimi.it](mailto:{alessandro.onori@polimi.it})  
🛠️ *Core backend model, modeling advancements, and Streamlit UI development*  

Technical Advisors
- Riccardo Mereu, Politecnico di Milano  
- Emanuela Colombo, Politecnico di Milano


## License
This is a free software licensed under the “European Union Public Licence" EUPL v1.1. It can be redistributed and/or modified under the terms of this license.