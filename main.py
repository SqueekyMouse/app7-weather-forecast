import streamlit as st
import plotly.express as px
from backend import get_data
#commit: done temperature graph and sky pics err handled Sec33

# add title, text input, slider,selectbox and subheader
st.title('Weather forecast for the next days')
place=st.text_input(label='Place: ')
# place=st.text_input(label='Place: ',value='Tokyo')
days=st.slider('Forecast Days',min_value=1,max_value=5,
               help='Select the number of days of forecast days')
option=st.selectbox('Select data to view',
                    ('Temperature','Sky'))

if place:
    # get the temparature or sky data
    filtered_data=get_data(place,days)
    if filtered_data==None:
        st.info('Please recheck the City Name')
    elif option=='Temperature':
        st.subheader(f'{option} for the next {days} days in {place}')
        temperatures=[dict['main']['temp']/10 for dict in filtered_data]
        # print(temperatures)
        dates=[dict['dt_txt'] for dict in filtered_data]
        # create temparature plot
        figure=px.line(x=dates,y=temperatures,labels={'x':'Dates','y':'Temperature (C)'})
        st.plotly_chart(figure_or_data=figure)
    elif option=='Sky':
        sky_conditions=[dict['weather'][0]['main'] for dict in filtered_data]
        images={'Clear':'images/clear.png','Clouds':'images/cloud.png',
                'Snow':'images/snow.png','Rain':'images/rain.png'}
        sky_conditions=[images[condition] for condition in sky_conditions]
        # print(sky_conditions)
        st.image(sky_conditions,width=115)