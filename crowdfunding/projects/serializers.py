from wsgiref import validate
from rest_framework import serializers
from .models import Project, Pledge

class ProjectSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  title = serializers.CharField(max_length=200)
  description = serializers.CharField(max_length=None)
  goal = serializers.IntegerField()
  image = serializers.URLField()
  is_open = serializers.BooleanField()
  date_created = serializers.DateTimeField()
  owner = serializers.ReadOnlyField(source='owner.id')

  def create(self, validated_data):
    return Project.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  amount = serializers.IntegerField()
  comment = serializers.CharField(max_length=200)
  anonymous = serializers.BooleanField()
  supporter = serializers.ReadOnlyField(source='supporter.id')
  project = serializers.IntegerField()
  
  def create(self, validated_data):
    validated_data['project'] = Project.objects.get(id=validated_data['project'])
    return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
  pledges = PledgeSerializer(many=True, read_only=True)

  # for updating a single project
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.is_open = validated_data.get('is_open', instance.is_open)
    instance.date_created = validated_data.get('date_created', instance.date_created)
    instance.owner = validated_data.get('owner', instance.owner)
    instance.save()
    return instance

class PledgeDetailSerializer(PledgeSerializer):
  projects = ProjectSerializer(read_only=True)

  # for updating single pledge
  def update(self, instance, validated_data):
    instance.amount = validated_data.get('amount', instance.amount)
    instance.comment = validated_data.get('comment', instance.comment)
    instance.anonymous = validated_data.get('anonymous', instance.anonymous)
    instance.supporter = validated_data.get('supporter', instance.supporter)
    instance.project = validated_data.get('project', instance.project)
    instance.save()
    return instance