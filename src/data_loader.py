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


    df = items.merge(orders, on='order_id', how='inner')
    
    df = df.merge(products, on='product_id', how='left')
    
    df = df.merge(customers, on='customer_id', how='left')
    
    payments_agg = payments.groupby('order_id').agg({
        'payment_type': lambda x: ', '.join(x.unique()),
        'payment_value': 'sum'
    }).reset_index()
    
    df = df.merge(payments_agg, on='order_id', how='left')

    colunas_data = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    
    for col in colunas_data:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])

    df['order_year_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

    df['product_category_name'] = df['product_category_name'].fillna('não_definido')

    return df