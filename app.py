import streamlit as st
import pickle
import numpy as np

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Define a function for the problem statement and laptop image page
def problem_and_image():
    st.title("Bussiness Problem")
    # Write your problem statement here
    st.write("""
    In an increasingly diverse laptop market, consumers face a daunting challenge: selecting the perfect laptop amidst a myriad of options, each boasting unique specifications and features. To address this, we endeavor to develop a sophisticated machine learning model capable of predicting laptop prices with unparalleled accuracy.
             
This project aims to predict the price of laptops based on various features such as brand, type, RAM, CPU, GPU, etc.
    
Objective:
Our aim is to empower consumers with invaluable insights into laptop pricing dynamics.

Impact:
This project not only serves as a testament to the capabilities of machine learning in the realm of consumer electronics but also promises tangible benefits to end-users. By offering reliable price estimations for laptops of diverse configurations and features, we aspire to streamline the decision-making process, empowering consumers to navigate the labyrinth of options with confidence and ease.
             
Source-https://www.kaggle.com/ionaskel/laptop-prices

    
![Laptop Image](https://i.ytimg.com/vi/A1eU51jPpXQ/mqdefault.jpg)
    """)

# Define a function for the model prediction page
def model_prediction():
    st.title("Laptop Price Predictor")

    # brand
    company = st.selectbox('Brand', df['Company'].unique())

    # type of laptop
    type = st.selectbox('Type', df['TypeName'].unique())

    # Ram
    ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

    # weight
    weight = st.number_input('Weight of the Laptop')

    # Touchscreen
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

    # IPS
    ips = st.selectbox('IPS', ['No', 'Yes'])

    # screen size
    screen_size = st.number_input('Screen Size', min_value=1.0, step=0.1)

    # resolution
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

    # CPU
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())

    # HDD
    hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

    # SSD
    ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

    # GPU
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())

    # OS
    os = st.selectbox('OS', df['os'].unique())

    if st.button('Predict Price'):
        # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        
        if screen_size == 0:
            st.error("Screen Size must be greater than 0.")
            return
        
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

        query = query.reshape(1, 12)
        st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

# Define a function for the contact page
def contact():
    st.title("Contact Information")
    st.write("""
    - **Name**: Sahil Tiwari
    - **Email**: sahiltiwari1222@gmail.com
    - **Phone**: +91 8670558757,8959688436
    - **Address**: Jogni Nagar,Jabalpur, India

    ### Social Media
    - [LinkedIn](https://www.linkedin.com/in/sahil-tiwari-b2269b27a/)
    - [GitHub](https://github.com/sahilTiwariiii)
    - [Twitter](https://twitter.com/sahil_tiwa96610)
    """)

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Problem Statement", "Model Prediction", "Contact"])

# Display the selected page
if page == "Problem Statement":
    problem_and_image()
elif page == "Model Prediction":
    model_prediction()
else:
    contact()
