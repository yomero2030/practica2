from rest_framework import routers, serializers, viewsets

#---------------- AGREGANDO MODELOS ---------------------
from Login.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('__all__')