
def nflx():
   
    import pandas as pd 
    import streamlit as st
    import matplotlib.pyplot as plt

#     st.title('Netflix Zone') 
#     st.image('./images/05cItXL96l4LE9n02WfDR0h-5.jpeg')
    
    nflx = pd.read_csv('../nflx.csv')
    history = pd.read_csv('../nflxrealclose.csv')
                       
    responses = ['History', 'Predictions', 'Both']        
    choice = st.selectbox('Do you want to see graphs of the history, LSTM model predictions, or a comparison of both?:  ',responses, key = '2')                   
     
        
    if (choice == 'History'):    
#         fig1 = plt.subplots(figsize=(20,10))
#         plt.title('Stock Prices History')
#         plt.plot(history['Close'], label='Close')
#         plt.xlabel('Date')
#         plt.ylabel('Prices ($)')
#         fig1.show()
        st.line_chart(history, x=history['Date'], y=history['Close'])
#         plt.show(fig1)
#         st.pyplot(fig1)
#         st.markdown('history')
    
    
    elif (choice == 'Predictions'):
        fig2 = plt.subplots(figsize=(20,10))                   
        plt.title('Stock Price Close v Predicted')
        plt.plot(nflx['Close'], label='Actual Close')
        plt.plot(nflx['predict'], label='Predicted')
        plt.xlabel('Date')
        plt.ylabel('Prices ($)')
        plt.legend()
        fig2.show()
#         plt.show(fig2)
#         st.markdown('pred')
    
    elif (choice == 'Both'):
        fig3 = plt.figure(figsize=(20, 10))
        plt.title('Stock Price History & Close v Predicted')
        plt.plot(history['Close'], label='History')
        plt.plot(nflx['Close'], label='Actual Close')
        plt.plot(nflx['predict'], label='Predicted')
        plt.xlabel('Date')
        plt.ylabel('Prices ($)')
        fig3.show()
#         plt.show(fig3)
#         st.pyplot(fig3)
#         st.markdown('both')
                       
                   
