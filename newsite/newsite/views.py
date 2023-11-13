from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):

    model=open('model.pkl','rb')
    lm=joblib.load(model)
    hours_studied = int(request.GET['HS'])
    previous_test = int(request.GET['PTS'])
    hours_slept = int(request.GET['HSPD'])
    sample_papers = int(request.GET['SQP'])

    ls=[]
    ls.append(hours_studied)
    ls.append(previous_test)
    ls.append(hours_slept)
    ls.append(sample_papers)
    print(ls)
    sp = lm.predict([ls])
    student_performance =  "{:.2f}".format(sp[0])
    return render(request,'result.html',{'hours_studied' : hours_studied, 'previous_test' : previous_test, 'hours_slept' : hours_slept, 
                                         'sample_papers' : sample_papers, 'student_performance': student_performance})

