import json
import pickle
import numpy as np
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Global variables for data columns, location names, and the model
__data_columns = None
__locations = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    """
    Estimate the price of a property based on location, square footage, bedrooms, and bathrooms.
    """
    try:
        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
    except Exception as e:
        print(f"Error finding location index: {e}")
        loc_index = -1

    # Create an input array of zeros
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Return the model's prediction rounded to two decimal places
    return round(__model.predict([x])[0], 2)

def get_location_names():
    """
    Fetch the list of available location names.
    """
    return __locations

def get_data_columns():
    """
    Fetch the list of all data columns.
    """
    return __data_columns

def load_saved_artifacts():
    """
    Load the model and columns data from artifacts.
    """
    print("Loading artifacts...")

    global __data_columns
    global __locations
    global __model

    # Paths to artifacts
    columns_file_path = r"F:\Machine Learning all Algorithms\Previous Company Project\Real Estate Price Prediction\server\artifacts\columns.json"
    model_file_path = r"F:\Machine Learning all Algorithms\Previous Company Project\Real Estate Price Prediction\server\artifacts\bangalore_home_prices_model.pickle"

    # Load columns.json
    with open(columns_file_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Exclude sqft, bath, bhk

    # Load the model
    with open(model_file_path, "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully.")
