# I have created this file : Rahul Gaur
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    guru={'name':'Rahul', 'place':'Shivpuri'}
    return render(request, 'index.html',guru)

def analyze(request):
    # get the text form the form
    textareabalatext = request.POST.get('textarea','default')
    checkbox = request.POST.get('checkbox','default')
    capital = request.POST.get('capital','default')
    spaceremover = request.POST.get('spaceremover','default')


    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    finaltext = ""

    if checkbox == "on":

      for char in textareabalatext:
        if char not in punctuations:
            finaltext = finaltext + char

      textareabalatext = finaltext


    if capital == "on":
        finaltext = textareabalatext.upper()
        textareabalatext = finaltext

    if spaceremover == "on":
        finaltext = ""
        l = len(textareabalatext)
        for index, char in enumerate(textareabalatext):
            if index == l-2 and textareabalatext[index] ==" " and textareabalatext[index+1] == " ":
                break

            if not(textareabalatext[index] == " " and textareabalatext[index+1] == " "):
                finaltext = finaltext + char


    if ( checkbox != "on" and capital != "on" and spaceremover != "on" ):
        return HttpResponse("Please Check Any Option!")


    textlist = {'text':finaltext}
    return render(request,'analyzer.html',textlist)


