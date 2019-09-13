from django.shortcuts import render

def home(request):
   # it will get all the jobobjects from db and turn them to
                            # python objects and then u can use inside of the code
    return render(request, 'products/home.html')
