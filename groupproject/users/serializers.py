from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from users.models import SKILLS

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    cv = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=200)
    interview_notes = serializers.CharField(max_length=2000)
    feedback_for_mentors = serializers.CharField(max_length=2000)
    mentor_comments = serializers.CharField(max_length=2000)
    position = serializers.CharField(max_length=200)
    skills = serializers.MultipleChoiceField(choices=SKILLS)
    status = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.cv = validated_data.get('cv', instance.cv)
        instance.state = validated_data.get('state', instance.state)
        instance.interview_notes = validated_data.get('interview_notes', instance.interview_notes)
        instance.feedback_for_mentors = validated_data.get('feedback_for_mentors', instance.feedback_for_mentors)
        instance.mentor_comments = validated_data.get('mentor_comments', instance.mentor_comments)
        instance.status = validated_data.get('status', instance.status)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.position = validated_data.get('position', instance.position)

        if "password" in validated_data.keys():
            instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance
