import pandas as pd
from typing import Union, Tuple, List
import warnings
warnings.filterwarnings(action='ignore')


CSV_FILE_PATH = "G:\JoJo\Accenture\Inventory management\src\Inventory_Data\inventory_table.csv"


# Imports the Inventory data CSV file
def import_data()->pd.DataFrame:
    """Function to import data from CSV file
    Returns: DataFrame"""
    data=pd.read_csv(CSV_FILE_PATH)
    return data


# Adds new product into Inventory data
def add_new_product(name:str, category:str, price:int, quantity:int) -> None:
    """
    Function to add new product to inventory management table
    
    Args:
    name: Product name
    category: Type of product category
    price: MRP of product
    quantity: Number of quantities available

    Returns: None
    """
    data=import_data()
    data.loc[len(data)] = [name,category,price,quantity]
    export_data(data)


# Gets the list of available products
def get_available_products()->Tuple:
    """
    Function to get the list of available product names

    Returns: Tuple of unique product names
    """
    data=import_data()
    return tuple(data["Product_Name"].unique())


# Updates the existing product details
def update_product(name:str, field_to_update:str, value:Union[int,str])-> None:
    """
    Function to update the existing product to inventory management table
    
    Args:
    name: Product name
    field_to_update: Field name to be updated
    value: Value to be updated

    Returns: None
    """
    data=import_data()
    data.loc[data["Product_Name"]==name,field_to_update] = value
    export_data(data)


# Displays the Inventory data file
def display_inventory_details()->pd.DataFrame:
    """
    Function to display the inventory details
    Returns: DataFrame
    """
    data=import_data()
    return data[["Product_Name","Quantity"]]


# sales of the inventory products
def sales_of_product(name:str,quantity:int)-> List:
    """
    Function to allow for the sale of products and to update the inventory accordingly.

    Args:
    name: Product name
    quantity: Quantity

    Returns: String  
    
    """
    data=import_data()
    available_quantity=int(data.loc[data["Product_Name"]==name,"Quantity"])
    
    if available_quantity<quantity:
        return ["Fail",f"Sorry, we have only {available_quantity} quantities available for {name}"]
    else:
        data.loc[data["Product_Name"]==name,"Quantity"]=data.loc[data["Product_Name"]==name,"Quantity"]-quantity
        export_data(data)
        return ["Success","Sales action completed successfully"]
    

# Generates alert if the product quantity is below the threshold
def generate_alert(threshold=20) -> Union[list,pd.DataFrame]:
    """Function to generate an alert if the product quantity is less than threshold
    
    Args:
    threshold: number
    default threshold: 20

    Returns: 
    List

    """
    data=import_data()
    product=list(data[data["Quantity"]<threshold]["Product_Name"])
    df = data[data["Quantity"]<threshold][["Product_Name","Quantity"]]
    return (f"{product} has to be restocked. It's quantity is below {threshold}."),df


# Exports the Inventory data to CSV file
def export_data(data):
    return data.to_csv(CSV_FILE_PATH,index=False)
