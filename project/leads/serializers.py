from rest_framework import serializers
from leads.models import Lead

#Maps the Leads model to a serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__' #same as ('id', 'name', 'email', 'message')