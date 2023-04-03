import streamlit as st
import pandas as pd
from script import Ledger


st.set_page_config(
page_title = 'Splitvise',
page_icon = ':coin:',
layout = 'wide',
)


def add_data(borrower_name, lender_name, amount_borrowed):
    df = pd.read_csv('database.csv')
    new_data = pd.DataFrame({'Borrower': [borrower_name], 'Lender': [lender_name], 'Amount': [amount_borrowed]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv('database.csv', index=False)
    return df

def show_data():
    df = pd.read_csv('database.csv')
    return df

def calculate_data():
    df = pd.read_csv('database.csv')
    l = Ledger()
    for ind in df.index:
        l.addDebt(df['Borrower'][ind],df['Lender'][ind],df['Amount'][ind])
    results = l.solve()
    return results

def clear_data():
    df = pd.DataFrame(columns=['Borrower','Lender','Amount'])
    df.to_csv('database.csv', index=False)


# st.title("Cash Flow Minimizer")
st.markdown("<h1 style='text-align: center; color: white;'>Cash Flow Minimizer</h1>", unsafe_allow_html=True)
borrower_name = st.text_input("Borrower Name")
lender_name = st.text_input("Lender Name")
amount_borrowed = st.number_input("Amount Borrowed", value=0, step=1)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add"):
        df = add_data(borrower_name, lender_name, amount_borrowed)
        st.success("Data added to the database.")

with col2:
    if st.button("Show"):
        df = show_data()
        st.dataframe(df)

with col3:
    if st.button("Calculate"):
        results = calculate_data()
        for i in results:
            st.markdown(i)

with col4:
    if st.button("Clear"):
        clear_data()

