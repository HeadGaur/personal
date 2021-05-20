from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['FullText']
    wordlist = fulltext.split(" ")
    worddic = {}
    for item in wordlist:
        if item in worddic:
            worddic[item]+=1
        else:
            worddic[item]=1
    sortedwords = sorted(worddic.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})