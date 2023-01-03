
#! Framework İmport
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


#! My import
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer


#! ########################<<<<Function Based View>>>>################################## !#


@api_view()  # default GET
def home(requst):
    return Response({'home': 'This is home page...'})


# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# - delete (dB de kayıt silme)
# - patch (kısmi update)

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    # print(students)
    serializer = StudentSerializer(students, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student created succesfully....'
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_detail(request, pk):

    student = get_object_or_404(Student, id=pk)
    # student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)


#############################################################

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk): 
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)

#! ########################<<<<Class Based View>>>>################################## !#

#! APIVIEW

class StudentListCreate(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
            "message": f'Student created succesfully....'
        }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_obj(self,pk):
        return get_object_or_404(Student, pk=pk)
    def get(self,request,pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self,request,pk):
        student=self.get_obj(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message": f'Student updated succesfully....'
             }
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            "message": f'Student {student.last_name} deleted succesfully'
        }
        return Response(data)

#! GENERİCAPI View

class StudentGAV(mixins.ListModelMixin,mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
         return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#! Concrete View 
# Concrete View hakkında detaylı bilgi(https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)
#! ListCreateAPIView ve RetrieveUpdateDestroyAPIView import edilmeli
class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer

class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#! ViewSets
# - Django REST Framework, ViewSet adı verilen tek bir classta bir dizi ilgili view için mantığı birleştirmenize olanak tanır.

# - Tipik olarak, views'ları urlconf'taki bir view kümesine açıkça kaydetmek yerine, view kümesini sizin için urlconf'u otomatik olarak belirleyen bir Router sınıfına kaydedersiniz.

# ViewSet sınıfını kullanmanın View sınıfını kullanmaya göre iki ana avantajı vardır.

# - Tekrarlanan mantık tek bir classta birleştirilebilir. Yukarıdaki örnekte, sorgu kümesini yalnızca bir kez belirtmemiz yeterlidir ve birden çok views'da  kullanılacaktır.
# - Router'larler kullanarak, artık URL yapılandırmasını kendi başımıza bağlamaklar uğraşmamıza gerek yok.

# Bunların her ikisi de bir değiş tokuşla gelir. Normal views'ları ve URL yapılandırmalarını kullanmak daha açıktır ve size daha fazla kontrol sağlar. Hızlı bir şekilde çalışmaya başlamak istiyorsanız veya büyük bir API'niz varsa ve baştan sona tutarlı bir URL yapılandırması uygulamak istiyorsanız, ViewSet'ler yardımcı olur.

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False,methods=['GET'])
    def student_count(self,request):
        count = {
            "Student-Count:" : self.queryset.count()
        }
        return Response(count)

class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    @action(detail=True)
    def student_names(self,request,pk=None):
        path =self.get_object()
        students = path.students.all()
        return Response([i.first_name for i in students])
