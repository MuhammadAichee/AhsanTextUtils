# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request,'index.html')

# def capitalize(request):
#     return HttpResponse('''<h1>Capitalize</h1><button onclick="window.location.href = 'index'">Back</button>''')

# def removepunctuate(request):
#     djText=(request.POST.get('text','default'))
#     RemovePunc=(request.POST.get('remove','off'))
#     fullcaps=(request.POST.get('fullcaps','off'))
#     punct='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     analyzed=''
#     if RemovePunc =='on':
#         for char in djText:
#             if char not in punct:
#                 analyzed = analyzed + char
#         params={'analyzed_text':analyzed}          
#         return render(request,'index.html',params)
#     elif (fullcaps == 'on'):
#         analyzed=""
#         for char in djText:
#             analyzed=analyzed+char.upper()
#         params={'analyzed_text':analyzed}
#         return render(request,'index.html',params)
# def spaceremove(request):
#     return HttpResponse('''<h1>Space Remove</h1><button onclick="window.location.href = 'index'">Back</button>''')
    
# def charcount(request):    
#     return HttpResponse('''<h1>Character Count</h1><button onclick="window.location.href = 'index'">Back</button>''')
from django.http import HttpResponse
from django.shortcuts import render
    

def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
