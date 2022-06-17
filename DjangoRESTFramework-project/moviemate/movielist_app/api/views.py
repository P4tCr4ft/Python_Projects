from uuid import RESERVED_FUTURE
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movielist_app.models import Movie
from movielist_app.api.serializers import MovieSerializer


# @api_view()
# def movie_list(request):
#     temp_list = []
#     movies = Movie.objects.all()
#     for item in list(movies.values()):
#         movie = Movie.objects.get(pk=item['id'])
#         serializer = MovieSerializer(movie)
#         temp_list.append(serializer.data)
#     return Response({'movies': temp_list})

# I was on the right track above, dealing with individual movie. But it is this simple ...
@api_view(['GET', 'POST'])
def movie_list(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)