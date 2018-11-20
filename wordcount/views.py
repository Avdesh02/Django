from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html',{'thisisit':'Avdesh Kumar Sharma'})

worddictionary = {}
def firstpage(request):
    fulltext = request.GET['fulltext']
    count = fulltext.split()

    for word in count:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    return render(request, 'count.html',{'fulltext':fulltext, 'count': len(count), 'worddictionary': worddictionary.items()})

def about_us(request):
    return render(request,"about.html")
