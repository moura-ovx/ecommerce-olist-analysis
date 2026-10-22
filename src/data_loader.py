import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    #Tabelas
    orders = pd.read_csv('data/raw/olist_orders_dataset.csv')
    items = pd.read_csv('data/raw/olist_order_items_dataset.csv')
    products = pd.read_csv('data/raw/olist_products_dataset.csv')
    customers = pd.read_csv('data/raw/olist_customers_dataset.csv')
    payments = pd.read_csv('data/raw/olist_order_payments_dataset.csv')