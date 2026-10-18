import django_filters
from .models import Portfolio, Category
class PortfolioFilter(django_filters.FilterSet):
    begin_after = django_filters.DateFilter(field_name='begin', lookup_expr='gte')
    #begin_before = django_filters.DateFilter(field_name='begin', lookup_expr='lte')
    #finish_after = django_filters.DateFilter(field_name='finish', lookup_expr='gte')
    finish_before = django_filters.DateFilter(field_name='finish', lookup_expr='lte')
    #location = django_filters.CharFilter(lookup_expr='icontains')
    #specialization = django_filters.CharFilter(lookup_expr='icontains')
    specialization = django_filters.CharFilter(
        field_name="specialization",
        lookup_expr="icontains"
    )
    location = django_filters.CharFilter(
        field_name="location",
        lookup_expr="icontains"
    )       
    #category = django_filters.CharFilter(
    #    field_name="cat__name",
    #    lookup_expr="icontains"
    #)
    category = django_filters.ModelChoiceFilter(
        field_name="cat",
        queryset=Category.objects.all(),
        to_field_name="name"
    )
    begin_after = django_filters.DateFilter(
        field_name="begin",
        lookup_expr="gte"
    )

    begin_before = django_filters.DateFilter(
        field_name="begin",
        lookup_expr="lte"
    )

    finish_after = django_filters.DateFilter(
        field_name="finish",
        lookup_expr="gte"
    )

    finish_before = django_filters.DateFilter(
        field_name="finish",
        lookup_expr="lte"
    )
    class Meta:
        model = Portfolio
        #fields = ['cat']
        #fields = ["category","location","specialization",]
        #fields = ['location','specialization','cat','category',]
        fields = []