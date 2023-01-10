from rest_framework import serializers
from watchlist_app.models import StreamPlatform, WatchList, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


# Using ModelSerializer we can see we do not have to explicitly map every variable in model,
# all the fields in WatchList are mapped automatically below re "__all__"
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="watch_detail")

    class Meta:
        model = StreamPlatform
        fields = "__all__"


# NOTE: Previously had some validations here, but ModelSerializer has some built in validations, see page 41 in my notes.
