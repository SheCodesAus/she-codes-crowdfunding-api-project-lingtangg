from wsgiref import validate
from rest_framework import serializers
from .models import Project, Pledge

class ProjectSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  title = serializers.CharField(max_length=200)
  description = serializers.CharField(max_length=None)
  main_language = serializers.CharField(max_length=100)
  secondary_language = serializers.CharField(max_length=100)
  time_required = serializers.IntegerField()
  location = serializers.CharField(max_length=100)
  image = serializers.URLField()
  is_open = serializers.BooleanField()
  date_created = serializers.DateTimeField()
  owner = serializers.ReadOnlyField(source='owner.id')

  def create(self, validated_data):
    return Project.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  time_pledged = serializers.IntegerField()
  comment = serializers.CharField(max_length=200)
  date_created = serializers.DateTimeField()
  supporter = serializers.ReadOnlyField(source='supporter.id')
  project_id = serializers.IntegerField()
  
  def create(self, validated_data):
    # validated_data['project'] = Project.objects.get(id=validated_data['project'])
    return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
  pledges = PledgeSerializer(many=True, read_only=True)

  # for updating a single project
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.main_language = validated_data.get('main_language', instance.main_language)
    instance.secondary_language = validated_data.get('secondary_language', instance.secondary_language)
    instance.time_required = validated_data.get('time_required', instance.time_required)
    instance.location = validated_data.get('location', instance.location)
    instance.is_open = validated_data.get('is_open', instance.is_open)
    instance.owner = validated_data.get('owner', instance.owner)
    instance.save()
    return instance

class PledgeDetailSerializer(PledgeSerializer):
  projects = ProjectSerializer(read_only=True)

  # for updating single pledge
  def update(self, instance, validated_data):
    instance.time_pledged = validated_data.get('time_pledged', instance.time_pledged)
    instance.comment = validated_data.get('comment', instance.comment)
    instance.supporter = validated_data.get('supporter', instance.supporter)
    instance.project = validated_data.get('project', instance.project)
    instance.save()
    return instance