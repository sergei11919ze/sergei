from rest_framework import serializers
from .models import Seq


class SeqSerializers(serializers.ModelSerializer):
    model = Seq
    fields = ('id',)