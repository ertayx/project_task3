from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["user"] = instance.user.username
        return dict_