import streamlit as st
#commit: add widgets Sec32

st.title('Weather forecast for the next days')
place=st.text_input('Place: ')
days=st.slider('Forecast Days',min_value=1,max_value=5,
               help='Select the number of days of forecast days')
option=st.selectbox('Select data to view',
                    ('Temparature','Sky'))
st.subheader(f'{option} for the next {days} days in {place}')


# print('hello world')