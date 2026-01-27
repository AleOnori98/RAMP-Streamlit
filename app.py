import streamlit as st
from config.path_manager import PM

st.set_page_config(page_title="RAMP Demand Simulator", layout="wide")

st.title("RAMP - Bottom-up Demand Simulation")
st.subheader("About RAMP")
<<<<<<< HEAD
=======
st.markdown(
    """
    [RAMP](https://rampdemand.org/) is an open-source software designed for the generation of **high-resolution multi-energy demand profiles** when only limited information about user behaviour is available.

    """)

st.image(PM.assets_dir / "ramp.png")

st.markdown("""
    It allows to:
    - **Characterize users** (households, institutions, services)  
    - Define **appliances** and their **operating windows**  
    - Capture **stochastic user behaviour**  
    - Generate **minute-by-minute load profiles** for each user category  
            
    This bottom-up approach yields finely detailed **energy usage time series** suitable for energy system simulations, techno-economic assessments, and demand-side studies.

    📖 **Documentation:** [rampdemand.readthedocs.io › latest](https://rampdemand.readthedocs.io/en/latest/?badge=latest)  
    💻 **GitHub Repository:** [github.com/RAMP-project/RAMP](https://github.com/RAMP-project/RAMP)

    """)

# ---------------------------------------------------------------------------
# Project files & management
# ---------------------------------------------------------------------------
st.markdown("---")
st.subheader("Project files & management")
>>>>>>> 2e9a7ce77eea0589cf1e29480a09737a0b5d7b0e

st.markdown(
    """
[RAMP](https://rampdemand.org/) is an open-source framework for generating
**high-resolution, stochastic multi-energy demand profiles** when only limited
information on user behaviour is available.

This app wraps the RAMP engine in a streamlined UI, allowing you to:

- Define **seasonal and weekly archetypes** for the year;
- Upload **appliance-level RAMP Excel inputs**;
- Generate **minute-resolution synthetic yearly load profiles**;
- Export **aggregated and per-category time series** for energy system models.
"""
)

st.image(PM.assets_dir / "ramp.png")

st.markdown(
    """
📖 **RAMP docs:** https://rampdemand.readthedocs.io/en/latest  
💻 **RAMP GitHub:** https://github.com/RAMP-project/RAMP
"""
)

st.markdown(
    """
    ### How the app is organised

    The application is structured into **two main workflows**, accessible from the
    Streamlit **sidebar**:

    - **RAMP Simulation**  
      Use this page when you already work with, or want to build, **RAMP-compatible
      Excel inputs** and exploit the full stochastic engine.
      - Configure the **year structure** (seasons, months, and optional week-classes).
      - Upload one or more **simplified RAMP Excel files** (single or multi-archetype).
      - Let the app build the **full RAMP input workbooks** behind the scenes.
      - Run the **stochastic simulation** to generate a synthetic full year at
        **one-minute resolution (365 × 1440)**.
      - Visualise daily profiles with **variability bands** and export:
        - per-category profiles
        - aggregated minute profile
        - aggregated hourly profile for energy system models.

    - **SSA Load Archetypes**  
      Use this page when you want a **fast, bottom-up demand profile** based on
      pre-defined **Sub-Saharan Africa user archetypes**.
      - Specify **location** (latitude) and **cooling regime** to select the climatic zone.
      - Define the number of **households by tier**, **schools**, and **hospital tiers**.
      - Generate a **one-year hourly aggregated load profile (8760 hours)** plus
        optional per-user (tier/facility) profiles.
      - Export ready-to-use CSVs for use in planning and optimisation tools.

    👉 Use the **sidebar navigation** to switch between pages and choose the
    workflow that best matches your case: detailed **RAMP-based stochastic demand**
    or **quick SSA archetype-based demand**.
    """
)

