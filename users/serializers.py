from rest_framework import serializers
from users.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'membership_date']

