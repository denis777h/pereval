from rest_framework import serializers
from .models import (PerevalUser, Image, PerevalLevel, PerevalCoordinate, PerevalAdded)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalUser
        fields = ['email', 'surname', 'name', 'otc', 'phone', 'users', ]
        pass


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title', 'image', ]


class LeverSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalLevel
        fields = ['winter', 'summer', 'autumn', 'spring', 'lever', ]


class CoordinatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalCoordinate
        fields = ['latitude', 'longitude', 'height', 'coordinates', ]
        read_only_fields = ['latitude', 'longitude', 'height', 'coordinates', ]

        pass


class PerevalSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    status = serializers.CharField(read_only=True)
    image = ImageSerializer(many=False, read_only=True)
    lever = LeverSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)
    coordinates = CoordinatSerializer(many=True, read_only=True)

    class Meta:
        model = PerevalAdded
        fields = ('__all__')

        def create(self, validated_data, *args, **kwargs):
            user = validated_data.pop('user')
            coord = validated_data.pop('coord')
            image = validated_data.pop('image')
            coord = PerevalCoordinate.objects.create(**coord)
            pereval = PerevalAdded.objects.create(**validated_data, coord=coord, user=user)
            user = PerevalAdded.objects.get_or_create(**user)
            created = PerevalAdded.objects.get_or_create(**user)

            for image in image:
                title = image.pop('title')
                data = image.pop('data')
                Image.objects.create(pereval=pereval, title=title, data=data)
                pass

            return pereval

        def validate(self, value, instance=None):
            user_data = value['user']
            instance = instance
            if self.instance:
                if (user_data['email'] != self.instance.user.email
                        or user_data['surname'] != self.instance.user.surname
                        or user_data['name'] != self.instance.user.name
                        or user_data['otc'] != self.instance.user.otc
                        or user_data['phone'] != self.instance.user.phone):
                    raise serializers.ValidationError()
                return value
