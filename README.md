# Remote sensing data projects  
### This folder contains analyses carried out on satellite data.  
**Each project will have a dedicated Jupyter notebook file.**


### Project 1: Analysis of wave height along italian coasts
**File name:  italy-wave-height-analysis.ipynb**  
This script performs an API call to the Copernicus Marine Server and fetches data for the months of Jan and Feb 2021 around the coasts of Italy.  
The fetched data is then saved into a pandas DataFrame. 
Descriptive statistics are calculated and basic relationship between variables explored. 

*Product identifier:* MEDSEA_MULTIYEAR_WAV_006_012  
*Product name:* Mediterranean Sea Waves Reanalysis  
*Dataset:* cmems_mod_med_wav_myint_4.2km_PT1H-i   

**Variables**:
- Sea surface wave significant height [VHM0]
- Sea surface primary swell wave significant height [VHM0_SW1]
- Sea surface secondary swell wave significant height [VHM0_SW2]
- Sea surface wind wave significant height [VHM0_WW]