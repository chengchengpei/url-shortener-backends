from api.models import Link
from api.serializers import LinkSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from django.conf import settings
from django.http import Http404, HttpResponseRedirect, HttpResponsePermanentRedirect

class LinkView(APIView):
    
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        print request.data
        long_url = request.data['long_url']
        print 'long_url = %s' % long_url
        if Link.objects.filter(long_url=long_url).exists():
            return Response({'err': 'URL already exists.'},
                    status=status.HTTP_400_BAD_REQUEST)

        link = Link.objects.create(long_url=long_url)
        serializer = LinkSerializer(link)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LinkDetailView(APIView):

    renderer_classes = (TemplateHTMLRenderer,)
    
    def get_object(self, code):
        try:
            return Link.objects.get(short_url=settings.SITE_BASE_URL+code)
        except Link.DoesNotExist:
            raise Http404 # NotFound

    def get(self, request, code):
        print 'code:', code
        link = self.get_object(code)
        link.visit_count += 1
        link.save()
        return HttpResponsePermanentRedirect(link.long_url)





