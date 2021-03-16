from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.apperance import apperance


data = { 
    'lesson': [1594663200, 1594666800], 
    'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
    'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
}


@api_view(['GET', ])
def index(request):
    result = apperance(data)
    return Response({'apperance': result})