from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):

#    Serializer for Genre model
#class Meta:
#    verbose_name = "Genre"
#    verbose_name_plural = "Genres"

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    ### Serializer for Movie

#    class Meta:
#       verbose_name = "Movie"
 #      verbose_name_plural = "Movies"


    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')
