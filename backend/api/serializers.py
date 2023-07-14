import base64
import imghdr
import uuid

import six
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from reg.models import Categoryes, SpareParts, Manufacturers

from rest_framework import serializers

from users.models import User


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')
            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'position',
            'password',
            'role')
        extra_kwargs = {'password': {'write_only': True}}
        #read_only_fields = 'is_subscribed',

    # def get_is_subscribed(self, obj):
    #     user = self.context.get('view').request.user
    #     return (not (user.is_anonymous or (user == obj))
    #             and user.follower.filter(author=obj).exists())

class SparePartSerializer(serializers.ModelSerializer):
    manufacturer = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = SpareParts
        fields = (
            'id',
            'name',                
            'tmc',
            'manufacturer',
            'category',
            'count',
            'note',
            'place',
            'floor',
            'change_date',
            'create_date',
            'review_date',)
        

class CategoryesPOSTSerializer(serializers.ModelSerializer):

    id = serializers.PrimaryKeyRelatedField(
        source='Categoryes',
        queryset=Categoryes.objects.all()
    )

    class Meta:
        fields = ('id',)
        model = Categoryes

class SparePartPOSTSerializer(serializers.ModelSerializer):
    #manufacturer = serializers.StringRelatedField()
    category = CategoryesPOSTSerializer(many=True,
                                        source='categoryes_set')

    class Meta:
        model = SpareParts
        fields = (
            'id',
            'name',                
            'tmc',
            'manufacturer',
            'category',
            'count',
            'note',
            'place',
            'floor',
            'change_date',
            'create_date',
            'review_date',)

class CategoryesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoryes
        fields = ('name',)

class ManufacturersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturers
        fields = (
            'name',)