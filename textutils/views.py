# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

#***************Basic Code****************
'''
def index(request):
    return HttpResponse("<h1>Hello</h1>")

def about(request):
    return HttpResponse("about harry")
'''


def index(request):
    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuations', 'analyzed_text':analyzed}
        djtext = analyzed 
        

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UpperCase', 'analyzed_text':analyzed}
        djtext = analyzed 
        
    
    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines', 'analyzed_text':analyzed}
        djtext = analyzed 
        

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):            
                analyzed = analyzed + char
        params = {'purpose':'removing extra space', 'analyzed_text':analyzed}
        djtext = analyzed 
        

    if(charcount == 'on'):
        analyzed = 0
        for char in djtext:
            if char !=" ":
                analyzed = analyzed + 1
        params = {'purpose':'Count no of char', 'analyzed_text': analyzed}
        djtext = analyzed
        

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Error")
    

    return  render(request, 'analyze.html', params)

