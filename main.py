import streamlit as st
import plotly.express as px
#commit: plotly: plot fake data dynamically Sec32

st.title('Weather forecast for the next days')
place=st.text_input('Place: ')
days=st.slider('Forecast Days',min_value=1,max_value=5,
               help='Select the number of days of forecast days')
option=st.selectbox('Select data to view',
                    ('Temparature','Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

def get_data(numdays):
    # x and y shd be arrays of same size!!!
    dates=['2022-25-10','2022-26-10','2022-27-10']
    temperatures=[10,11,15]
    # make the fig dynamic!!!
    temperatures=[numdays*i for i in temperatures]
    return(dates,temperatures)

d,t=get_data(days)

# x and y shd be arrays of same size!!!
figure=px.line(x=d,y=t,labels={'x':'Dates','y':'Temparature (C)'})
st.plotly_chart(figure_or_data=figure)
