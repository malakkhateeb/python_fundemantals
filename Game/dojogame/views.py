import random
from django.shortcuts import render,redirect

def great(request):
    if 'randnum' not in request.session: 
        request.session['randnum']=random.randint(1, 100)
    if'result' not in request.session:
        request.session['result']=""
    context={
            'result': request.session['result'],
            'color': request.session.get('color', '')
        }
    return render(request, 'game.html', context )

def randNum(request):
    rand_form=int(request.POST['rand_num'])	
    if rand_form > request.session['randnum']:
        request.session['result']='too high'
        request.session['color']= "blue"
    elif  rand_form <  request.session['randnum']:
        request.session['result']='too low'
        request.session['color']= "red"
    else: 
        request.session['result']= 'correct'
        request.session['color']= "green"
    print( request.session['result'])
    print( request.session['randnum'])

    return redirect('/') 

def clearData(request):
    request.session.flush() 
    return redirect('/')
