from django.shortcuts import render, redirect
from .models import principal, faculty, student
from .forms import principalform
from .serializers import facultyserializers, studentserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def home(request):
    return render (request, 'home.html')

def principalhome(request):
    return render (request, 'principalhome.html')

def facultyhome(request):
    return render (request, 'facultyhome.html')

def principallogin(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=principal.objects.get(username=unm)
        print("Name", fnm.firstname)
        
        user=principal.objects.filter(username=unm, password=pas)
        if user:
            print("Login succesful")
            return redirect('principalhome')
        else:
            print("Error")
    return render (request, 'principallogin.html')

def facultylogin(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=faculty.objects.get(username=unm)
        print("Name", fnm.firstname)

        user=faculty.objects.filter(username=unm, password=pas)
        if user:
            print("Login succesful")
            return redirect ('facultyhome')
        else:
            print("Error")
    return render (request, 'facultylogin.html')

@api_view(['GET'])
def facultydata(request):
    if request.method=='GET':
        fdata=faculty.objects.all()
        serial=facultyserializers(fdata, many=True)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])  
def studentdata(request):
    if request.method=='GET':
        stdata=student.objects.all()
        serial=studentserializers(stdata, many=True)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    else:
        return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addfacultydata(request):
    if request.method=='POST':
        fdata=facultyserializers(data=request.data)
        if fdata.is_valid():
            fdata.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addstudentdata(request):
    if request.method=='POST':
        stdata=studentserializers(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)
        
def deletefaculty(request):
    if request.method=='GET':
        fdata=faculty.objects.all()
        serial=facultyserializers(fdata, many=True)
        return render (request, 'deletefaculty.html', {'fdata':serial.data})
    else:
        return Response (status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE', 'GET']) 
def deletefacultyid(request,id):
    try:
        fid=faculty.objects.get(id=id)
    except faculty.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=facultyserializers(fid)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        faculty.delete(fid)
        return Response (status=status.HTTP_202_ACCEPTED)

def deletestudent(request):
    if request.method=='GET':
        stdata=student.objects.all()
        serial=studentserializers(stdata, many=True)
        return render (request, 'deletestudent.html', {'stdata':serial.data})
    else:
        return Response (status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE', 'GET'])
def deletestudentid(request, id):
    try:
        stid=student.objects.get(id=id)
    except student.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studentserializers(stid)
        return Response (data=serial.data, status=status.HTTP_200_OK)

    if request.method=='DELETE':
        student.delete(stid)
        return Response (status=status.HTTP_202_ACCEPTED)
    
def editstudent(request):
    if request.method=='GET':
        stdata=student.objects.all()
        serial=studentserializers(stdata, many=True)
        return render (request, 'editstudent.html', {'stdata':serial.data})
    else:
        return Response (status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT', 'GET'])
def editstudentid(request,id):
    try:
        stid=student.objects.get(id=id)
    except student.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studentserializers(stid)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        stserial=studentserializers(data=request.data, instance=stid)
        if stserial.is_valid():
            stserial.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_403_FORBIDDEN)

def editfaculty(request):
    if request.method=='GET':
        fdata=faculty.objects.all()
        serial=facultyserializers(fdata, many=True)
        return render (request, 'editfaculty.html', {'fdata':serial.data})
    else:
        return Response (status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT', 'GET'])
def editfacultyid(request,id):
    try:
        fid=faculty.objects.get(id=id)
    except faculty.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=facultyserializers(fid)
        return Response (data=serial.data, status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        facultyserial=facultyserializers(data=request.data, instance=fid)
        if facultyserial.is_valid():
            facultyserial.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_403_FORBIDDEN)
        