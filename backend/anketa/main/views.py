from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContentItem
from rest_framework import serializers

class ContentItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ContentItem
        fields = ['title', 'text', 'date', 'image']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

@api_view(['GET'])
def content_view(request, section):
    items = ContentItem.objects.filter(section=section)
    serializer = ContentItemSerializer(items, many=True, context={'request': request})
    return Response(serializer.data)