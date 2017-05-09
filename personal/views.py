from django.shortcuts import render


def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you wold like to contact me, please email me', 'thuyettiensinh@gmnail.com']})

def about(request):
	return render(request, 'personal/about.html', {
		'content':[
			'This example page about for Django', 
			'about me about me about me about me about me about me ',
			'about me about me about me about me about me about me about me ',
			]})



