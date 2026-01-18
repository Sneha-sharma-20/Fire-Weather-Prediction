**Fire Weather Index (FWI) Predictor** \
A Machine Learning–based web application to predict Fire Weather Index (FWI) using environmental and fire-danger parameters.
Developed as part of the Infosys Springboard Virtual Internship Program.\

**Problem Statement**\
Wildfires pose a serious threat to ecosystems, human life, and property. The Fire Weather Index (FWI) is a globally used indicator to estimate forest fire danger based on weather conditions and fuel moisture content.

This project aims to develop an end-to-end Fire Weather Index prediction system using machine learning. The system processes key meteorological and fire-related parameters, predicts the FWI value, classifies fire risk levels, and presents the results through a user-friendly Flask web application. The goal is to support early warning, risk assessment, and informed decision-making for wildfire management.\

**Project Outcomes**

* Trained a Ridge Regression model to predict Fire Weather Index

* Applied StandardScaler for consistent feature normalization

* Evaluated multiple regression models and selected the best performer

* Deployed the trained model using a Flask web application

* Displayed predicted FWI value along with fire risk level, causes, and precautions

**Features Used** 

* Temperature
* Relative Humidity (RH)
* Wind Speed
* Rainfall
* FFMC (Fine Fuel Moisture Code)
* DMC (Duff Moisture Code)
* DC (Drought Code)
* ISI (Initial Spread Index)
* BUI (Build-Up Index)

**System Requirements**\
Hardware
* Processor: Intel Core i3 or higher
* RAM: Minimum 4 GB (8 GB recommended)
* Storage: At least 10 GB free disk space

Software

* Python 3.9+
* Flask
* Required Python libraries (see requirements.txt)

**Workflow**<img width="1024" height="1536" alt="ChatGPT Image Jan 19, 2026, 12_28_22 AM" src="https://github.com/user-attachments/assets/85d3ad61-265d-4806-ad91-9e6ea00ffc7a" />

**Web Application Output Screens**

Home page <img width="1855" height="856" alt="Screenshot 2026-01-18 054134" src="https://github.com/user-attachments/assets/1e5b131a-bff1-4abf-9b9b-2bed6beac2d6" />

Result page <img width="1905" height="873" alt="Screenshot 2026-01-18 054116" src="https://github.com/user-attachments/assets/1f7c2f55-7ad1-4a18-9d8e-05dd44c90c10" />

FWI <img width="1893" height="874" alt="Screenshot 2026-01-18 054143" src="https://github.com/user-attachments/assets/2526bec9-43f9-418b-b4f3-9e8fc96fbd28" />

Features of FWI <img width="1854" height="874" alt="Screenshot 2026-01-18 054155" src="https://github.com/user-attachments/assets/b7c6ee25-ac7c-42b9-898b-a1db336234f5" />

FWI caluclation <img width="1867" height="896" alt="Screenshot 2026-01-18 054208" src="https://github.com/user-attachments/assets/06c61aa0-e679-42cf-8c0f-526ce65a7cee" />

Articles <img width="1877" height="831" alt="Screenshot 2026-01-18 054218" src="https://github.com/user-attachments/assets/0a796de1-f39a-4089-9442-71f26f2e2c57" />

**How to Run the Project Locally**
1. Clone the Repository
   
3. Create a Virtual Environment
   * Windows
     ```Bash 
     python -m venv venv
     venv\Scripts\activate
   * Macos
     ```
     python3 -m venv venv
     source venv/bin/activate

5. Install Required Dependencies
   ```
   pip install -r requirements.txt

7. Run the Flask Application
   ```
   python app.py

9. Open in Browser

**Conclusion**

This project successfully demonstrates an end-to-end Fire Weather Index prediction system, integrating data preprocessing, feature scaling, machine learning modeling, evaluation, and Flask-based deployment. By combining accurate prediction with interpretability through risk levels and precautions, the system provides a practical tool for wildfire risk assessment and early warning support.
