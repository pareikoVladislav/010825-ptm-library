from rest_framework import serializers
from library.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff',
                   'is_superuser',
                   'is_active',
                   'groups',
                   'user_permissions',
                   'password',
                   'first_name',
                   'last_name',
                   'phone',
                   'birth_date',
                   'age',

                   ]