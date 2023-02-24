import requests
# commit: done api request, get temp and sky list Sec33

API_KEY='664130abedff50a83c4c42004189fc01'
# 2b0b3a2322e55cfbb245ec2dba4bb45b

# http://api.openweathermap.org/data/2.5/forecast?q=tokyo&appid=664130abedff50a83c4c42004189fc01
# http://api.openweathermap.org/data/2.5/forecast?q=Tokyo&appid=2b0b3a2322e55cfbb245ec2dba4bb45b

def get_data(place,forecast_days,kind):
    url=f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response=requests.get(url)
    data=response.json()
    filtered_data=data['list']
    # len(filtered_data) #40
    # 3hr data point 24/3=8 and 8*5=40
    # 8 val for 24 hrs, 40 values for 5 days
    num_of_values=8*forecast_days
    filtered_data=filtered_data[:num_of_values]
    if kind=='Temparature':
        #get list of temparatures
        filtered_data=[dict['main']['temp'] for dict in filtered_data]
    if kind=='Sky':
        #get list of sky condition
        filtered_data=[dict['weather'][0]['main'] for dict in filtered_data]
    return(filtered_data)

if __name__=='__main__':
    print(get_data(place='Tokyo',forecast_days=3,kind='Temparature'))