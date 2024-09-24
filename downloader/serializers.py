from rest_framework import serializers

class URLSerializer(serializers.Serializer):
    url = serializers.URLField()
    format_type = serializers.CharField(required=False, default='all')

class FormatSerializer(serializers.Serializer):
    format_id = serializers.CharField()
    resolution = serializers.CharField()

class DownloadSerializer(serializers.Serializer):
    url = serializers.URLField()
    format_id = serializers.CharField()