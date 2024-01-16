import streamlit as st
import utils

#Create Streamlit Application

def main():
    st.title("Welcome to Inventory Management System")
    # display options
    st.sidebar.title("Actions")
    option=st.sidebar.selectbox("Select an operation",("Insert","Display","Update","Sale","Alert","Export"))
    # Perform operation
    if option=="Insert":
        st.sidebar.subheader("Inserts new product into the Inventory Table")
        st.subheader("Insert new product")
        name=st.text_input("Enter the product name")
        category=st.text_input("Enter the product category")
        price=st.text_input("Enter the price of the product")
        quantity=st.text_input("Enter the quantity of the product")
        if st.button("Insert"):
            res=utils.add_new_product(name, category, price, quantity)
            st.success(res)


    elif option=="Display":
        st.sidebar.subheader("Displays all the records present in the Inventory Table")
        st.subheader("Reads Inventory Table")
        if st.button("Display"):
            st.dataframe(utils.display_inventory_details())
            st.success("The inventory table displayed successfully")
            

    elif option=="Update":
            products_list = utils.get_available_products()
            st.sidebar.subheader("Update the product information in the Inventory Table")
            st.subheader("Updates the existing product details")

            product=st.selectbox("Select the product name to update",products_list)
            choice=st.selectbox("Select the field you want to update",("Product_Name","Category","Price","Quantity"))
            value=st.text_input(f"Enter the new value for {choice} to update")
            
            if st.button("Update"):
                res=utils.update_product(product,choice,value)
                st.success(res)


    elif option=="Sale":
        products_list = utils.get_available_products()
        st.sidebar.subheader("Sales of the product")
        st.subheader("Gives the sale details")
        product=st.selectbox("Enter the product to purchase",products_list)
        quantity=st.number_input("Number of quantity to purchase")
        if st.button("Sale"):
            msg=utils.sales_of_product(product,quantity)
            if msg!=None and msg[0]=="Fail":
                st.error(msg[1])
            if msg!=None and msg[0]=="Success":
                st.success(msg[1])
    

    elif option=="Alert":
        st.sidebar.subheader("Generation alert for the products less than the threshold value")
        st.subheader("Alert Generation")
        Threshold=st.number_input("Enter the threshold value")
        if st.button("Alert"):
            msg,df=utils.generate_alert(Threshold)
            st.warning(msg)
            st.dataframe(df)
            st.success("Alert generated successfully!")

    elif option=="Export":
        st.sidebar.subheader("Exports the products details from inventory to CSV file")
        st.subheader("Export products details")
        data=utils.import_data()
        if st.button("Export"):
            res=utils.export_data(data)
            st.success(f"Data exported successfully to path\n\n{utils.CSV_FILE_PATH}!")


if __name__=="__main__":
    main()