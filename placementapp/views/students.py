
import requests
from django.shortcuts import render
from django.http import HttpResponse

from placementproject import settings

def get_details(request):

    url = r"http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students/"
    data = requests.get(url)
    url=r"http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/departments/"
    dept = requests.get(url)
    return render(request, 'placementapp/students.html', {'c': data.json(),'d': dept.json()})





def details(request,page_number):

    url = r"http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students/"
    data = requests.get(url)
    url=r"http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/departments/"
    dept = requests.get(url)
    msg = data.json()['message']
    page_number=page_number*25
    required_data=[]
    c=0
    for i in msg:

        if i['id']==page_number and c<25:
            print(page_number)
            required_data.append(i)
            c = c + 1
            page_number=page_number+1
            print(c)




    print(required_data)

    return render(request, 'placementapp/first.html', {'c': required_data,'d': dept.json()})