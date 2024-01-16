import pandas as pd
from logger import logging
from exception import CustomException
from typing import Union, Tuple, List
import warnings
import sys

warnings.filterwarnings(action='ignore')


CSV_FILE_PATH = "G:\JoJo\Accenture\Inventory management\src\Inventory_Data\inventory_table.csv"


# Imports the Inventory data CSV file
def import_data()->pd.DataFrame:
    """Function to import data from CSV file

    Returns: DataFrame"""
    try:
        logging.info("Importing data from the CSV file")
        data=pd.read_csv(CSV_FILE_PATH)
        return data
    except Exception as e:
        logging.error("Error occured while importing data from CSV file")
        raise CustomException(e, sys)
        

# Exports the Inventory data to CSV file
def export_data(data)->None:
    """Function to export data to CSV file 

    Args: Dataframe: Dataframe to export
    
    Returns: None
    """
    try:
        logging.info("Exporting the data to CSV format")
        return data.to_csv(CSV_FILE_PATH,index=False)
    except Exception as e:
        logging.error("Error occured while exporting the data to CSV format")
        raise CustomException(e, sys)

# Gets the list of available products
def get_available_products()->Tuple:
    """
    Function to get the list of available product names

    Returns: Tuple of unique product names
    """
    try :
        logging.info("Checking the available products in the inventory")
        data=import_data()
        return tuple(data["Product_Name"].unique())
    except Exception as e:
        logging.error("Error occured while getting the list of available products in the inventory")
        raise CustomException(e, sys)


def add_new_product(name:str, category:str, price:int, quantity:int) -> str:
    """
    Function to add new product to inventory management table
    
    Args:
    name: Product name
    category: Type of product category
    price: MRP of product
    quantity: Number of quantities available

    Returns: String
    """
    try:
        data=import_data()
        available_prod=get_available_products()
        if name in available_prod:
            logging.info("Product name already exists, please update it if needed.")
            return "Product name already exists, please update it if needed."
        logging.info("New product added to inventory table")
        data.loc[len(data)] = [name,category,price,quantity]
        export_data(data)
        return "The product detail is added successfully!"
    except Exception as e:
        logging.error("Error ocuured while adding a new product into the inventory table")
        raise CustomException(e, sys)
        
# Updates the existing product details
def update_product(name:str, field_to_update:str, value:Union[int,str])-> None:
    """
    Function to update the existing product to inventory table
    
    Args:
    name: Product name
    field_to_update: Field name to be updated
    value: Value to be updated

    Returns: None
    """
    try:
        data=import_data()
        logging.info("Updating existing product details in inventory table")
        data.loc[data["Product_Name"]==name,field_to_update] = value
        export_data(data)
        return "Record updated successfully!"
    except Exception as e:
        logging.error("Error while updating existing product details in inventory table")
        raise CustomException(e, sys)


# Displays the Inventory data file
def display_inventory_details()->pd.DataFrame:
    """
    Function to display the inventory details 

    Returns: DataFrame
    """
    try:
        data=import_data()
        logging.info("Displaying the current inventory table ")
        return data[["Product_Name","Quantity"]]
    except Exception as e:
        logging.error("Error while display the record present in the inventory table")
        raise CustomException(e, sys)


# sales of the inventory products
def sales_of_product(name:str,quantity:int)-> List:
    """
    Function to allow for the sale of products and to update the inventory accordingly.

    Args:
    name: Product name
    quantity: Quantity

    Returns: String  
    
    """

    try:
        data=import_data()
        available_quantity=int(data.loc[data["Product_Name"]==name,"Quantity"])
        
        if available_quantity<quantity:
            return ["Fail",f"Sorry, we have only {available_quantity} quantities available for {name}"]
        else:
            logging.info("Allowing for sale of products available in inventory table")
            data.loc[data["Product_Name"]==name,"Quantity"]=int(data.loc[data["Product_Name"]==name,"Quantity"]-int(quantity))
            export_data(data)
            return ["Success","Sales action completed successfully"]
    except Exception as e:
        logging.error("Error occurred while processing the sales of products in inventory table")
        raise CustomException(e, sys)

# Generates alert if the product quantity is below the threshold
def generate_alert(threshold=20) -> Union[list,pd.DataFrame]:
    """Function to generate an alert if the product quantity is less than threshold
    
    Args:
    threshold: number
    default threshold: 20

    Returns: 
    List
    """
    try:
        data=import_data()
        product=list(data[data["Quantity"]<threshold]["Product_Name"])
        df = data[data["Quantity"]<threshold][["Product_Name","Quantity"]]
        logging.info("Generating alert for the products available below the threshold value")
        return (f"{product} has to be restocked. It's quantity is below {threshold}."),df
    except Exception as e:
        logging.error("Error occured while generating the alert for the products available below the threshold value")
        raise CustomException(e, sys)