from django.shortcuts import render
import requests
import os


def button(request):

    return render(request,'page2_new.html')

def output(request):
	os.system("python3 C:\\Users\\rashm\\Music\\buttonpython\\Exact\\main_algo_exact_full.py")
	print("Wordcloud image is created...")
	data= "Hey Rashmi"
	return render(request,'page2_new.html',{'data':data})