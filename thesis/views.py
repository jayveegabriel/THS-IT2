from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'temperature': reverse('unodosmattress:temperature-list', request=request, format=format),
       'bed': reverse('unodosmattress:bed-list', request=request, format=format),
       'heartRate': reverse('unodosmattress:heartRate-list', request=request, format=format),
       'position': reverse('unodosmattress:position-list', request=request, format=format),
       'heartRateEveryMin': reverse('unodosmattress:heartRateEveryMin-list', request=request, format=format),
       'temperatureEveryMin': reverse('unodosmattress:temperatureEveryMin-list', request=request, format=format),
       'RFID': reverse('unodosmattress:rfid-list', request=request, format=format),
       # 'notification': reverse('unodosmattress:notification-list', request=request, format=format),
})
