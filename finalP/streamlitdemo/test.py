
import streamlit as st
from PIL import Image
from nflx import nflx



def main():
    
    
    options = ['Home', 'Netflix', 'Apple', 'Google', 'Tesla', 'Toyota']
    choice = st.sidebar.selectbox('Menu',options, key='1')
    
    if (choice == 'Home'):
        st.title('Welcome to the Stock Predictor') 
        st.image('./images/143dc05c-65f4-46f3-bf39-a7c0ec9e27a2.jpeg')
        
        
        st.text('There are 5 stocks in this study, Netflix, Apple, Google, Tesla, and Toyota')
        
        pass
    
    elif (choice == 'Netflix'):
        st.title('Netflix Zone') 
        st.image('./images/05cItXL96l4LE9n02WfDR0h-5.jpeg')
        nflx()
        pass
    
    elif (choice == 'Apple'):
        st.title('Apple Zone') 
        st.image('./images/Apple-Logo-History-1920x1080.jpeg')
        aapl()
        pass
    
    elif (choice == 'Google'):
        st.title('Google Zone') 
        st.image('./images/JF-US-GOOGLE-EVOLUTION-COMP-02.jpeg')   
        goog()
        pass
    
    elif (choice == 'Tesla'):
        st.title('Tesla Zone') 
        st.image('./images/s-l1600.jpeg')
        tsla()
        pass
    
    elif (choice == 'Toyota'):
        st.title('Toyota Zone') 
        st.image('./images/WpcTavg99b5XpK6STzSLZ8.jpeg')
        tm()
        pass
    
    else:
        st.stop()

main()








