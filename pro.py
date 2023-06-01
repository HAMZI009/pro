import requests
from bs4 import BeautifulSoup
import streamlit as st

# Fetch the HTML content from the URL
url = 'https://autodeals.pk/new-cars'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract the car details
car_list = soup.find_all('div', class_='car-detail')
car_data = []

for car in car_list:
    title = car.find('h2').text.strip()
    price = car.find('div', class_='car-price').text.strip()
    car_data.append({'Title': title, 'Price': price})

# Create a Streamlit web app
st.title('Car Details')

for car in car_data:
    st.write('##', car['Title'])
    st.write('Price:', car['Price'])
    st.write('---')
