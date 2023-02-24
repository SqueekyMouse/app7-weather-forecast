import streamlit as st
import plotly.express as px
from backend import get_data
#commit: plotly: plot fake data dynamically Sec32

st.title('Weather forecast for the next days')
place=st.text_input('Place: ')
days=st.slider('Forecast Days',min_value=1,max_value=5,
               help='Select the number of days of forecast days')
option=st.selectbox('Select data to view',
                    ('Temparature','Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

data=get_data(place,days,option)

d,t=get_data(place)

# x and y shd be arrays of same size!!!
figure=px.line(x=d,y=t,labels={'x':'Dates','y':'Temparature (C)'})
st.plotly_chart(figure_or_data=figure)
