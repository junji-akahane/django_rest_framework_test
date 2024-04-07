from rest_framework import serializers
from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author', 'author_id')

    def create(self, validated_data):
        validated_data['author'] = validated_data.get('author_id', None)

        if validated_data['author'] is None:
            raise serializers.ValidationError("user not found.") 

        del validated_data['author_id']

        return Entry.objects.create(**validated_data)
