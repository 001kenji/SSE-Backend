from django.shortcuts import render
import asyncio, random
# Create your views here.
from django.http import StreamingHttpResponse
from django.shortcuts import render
import json,time,datetime

def get_live_data_point() :
    val1 = random.randrange(10,20)
    val2 = random.randrange(20,40)
    val3 = random.randrange(40,60)
    val4 = random.randrange(60,80)
    val5 = random.randrange(80,90)

    arrayVal = [val1,val2,val3,val4,val5]

    result = random.choice(arrayVal)
    return result



def get_date():
    dateNow = datetime.datetime.now()
    year = dateNow.year
    valMonth = dateNow.month
    date = "{0}-{1}-{2}"
    valDay = dateNow.day
    
    result = date.format(year,valMonth,valDay)
    print(result)
    return result
    
#print(datetime.datetime.today())

async def trial1(request):
    async def event_tream():
        
        while True:
            
            
            data = json.dumps({"x": get_date(), "y": get_live_data_point()})
            yield f'data: {data}\n\n'
           
            await asyncio.sleep(2) 

    return StreamingHttpResponse(event_tream(),content_type='text/event-stream')


def index(request):
    return render(request, 'data.html')