from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from .serializers import UserSerializer, PlaceSerializer, PortfolioSerializer, CategorySerializer
from .models import Place, Portfolio, Category
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PortfolioFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class PortfolioViewSet(viewsets.ModelViewSet):
    #queryset = Portfolio.objects.all()
    #queryset = Portfolio.objects.select_related("cat").all()
    queryset = Portfolio.objects.select_related("cat").order_by("-begin")
    serializer_class = PortfolioSerializer
    #filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]
    #filter_backends = [DjangoFilterBackend]
    #filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #filterset_fields = {'cat': ['exact'],'begin': ['exact', 'gte', 'lte'],'finish': ['exact', 'gte', 'lte'],'location': ['exact', 'icontains'],'specialization': ['exact', 'icontains'],}
    #filterset_fields = ['location', 'specialization', 'cat']
    #filterset_class = PortfolioFilter
    #search_fields = ['location','specialization','responsibilities','progress',]
    search_fields = [
        "location",
        "specialization",
        "responsibilities",
        "progress",
        "cat__name",
    ]
    #ordering = ['-begin']
    #ordering_fields = '__all__'
    #ordering_fields = ['begin', 'finish', 'location']
    #ordering_fields = ['begin','finish','location','specialization',]
    ordering_fields = [
        "begin",
        "finish",
        "specialization",
    ]
    def get_queryset(self):
        #queryset = Portfolio.objects.all()
        queryset = super().get_queryset()
        specialization = self.request.query_params.get("specialization")
        if specialization:
            queryset = queryset.filter(
                specialization__icontains=specialization
            )
        return queryset
    #@action(detail=False, methods=['get'])
    #def latest(self, request):
        #return Response({"message": "Последние проекты"})
        #count = request.query_params.get('count', 3)
    #    try:
    #        count = int(request.query_params.get("count", 3))
    #    except ValueError:
    #        count = 3
    #    if count < 1:
    #        count = 1
    #    if count > 20:
    #        count = 20
        #projects = Portfolio.objects.order_by('-id')[:3]
    #    projects = Portfolio.objects.order_by('-id')[:int(count)]
        #serializer = PortfolioSerializer(projects, many=True)        
    #    serializer = self.get_serializer(projects, many=True)
    #    return Response(serializer.data)
    #def tech(self, request):
    #    queryset = Portfolio.objects.filter(
    #        specialization__icontains="Технический специалист."
    #    )
    #    serializer = PortfolioSerializer(queryset, many=True)
    #    return Response(serializer.data)
    #@action(detail=True, methods=['get'])
    #def info(self, request, pk=None):
    #    project = self.get_object()
    #    serializer = self.get_serializer(project)
    #    return Response(serializer.data)
    @action(detail=True, methods=["post"])
    def duplicate(self, request, pk=None):
        project = self.get_object()
        project.pk = None
        project.save()
        serializer = self.get_serializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
def contents(request):
    #print('Кто-то зашёл на главную!')
    content = Portfolio.objects.all()
    return render(request, "index.html", {"content": content})