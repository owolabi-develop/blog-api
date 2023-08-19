from rest_framework import serializers
from . models import Articles,ArticleUser,Category,Comments,Tag


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ['articles','user','content']


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Articles
        fields = ['id','headlines','content','image','category','tags','author','comments']
    


class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','articles']

class TagSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = ['id','name','articles']




class UserSerialzier(serializers.ModelSerializer):
   articles = ArticleSerializer(many=True, read_only=True)
   
   class Meta:
        model = ArticleUser
        fields = ['email','password','articles']
        extra_kwargs = {'password': {'write_only': True}}

   def create(self, validated_data):
        user = ArticleUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




## token sserializers

class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
    


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()   