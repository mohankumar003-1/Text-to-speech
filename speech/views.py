from django.shortcuts import render,HttpResponse
from .models import speech
from .code import textspeech
def tts(request):
    #return HttpResponse("<h1>HI</h1>")

        if request.method == 'POST':
                text = request.POST.get('text')
                a = speech(text=text)
                a.save()
                b = textspeech(text)

        return render(request,'index.html')
# Create your views here.
