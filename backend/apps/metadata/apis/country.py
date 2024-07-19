from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.views import APIView
from rest_framework import status

from apps.metadata.models import Country
from apps.metadata.types import CountryObject
from apps.metadata.serializers import CountrySerializer
from apps.common.services import delete_model

from apps.metadata.selectors import (
    country_list,
    get_country
)


from apps.metadata.services import (
    update_country,
    create_country
)


class CountryAPI(APIView):
    """API for getting list of tags or creating instances"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request) -> Response:
        queryset = country_list()

        data = CountrySerializer(queryset, many=True).data

        return Response(data)

    def post(self, request) -> Response:
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_country(CountryObject(**serializer.validated_data))

        data = CountrySerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class CountryDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk: int) -> Response:
        tag = get_country(pk=pk)

        data = CountrySerializer(tag).data

        return Response(data)

    def patch(self, request, pk: int) -> Response:

        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = update_country(pk=pk, data=CountryObject(
            **serializer.validated_data))

        data = CountrySerializer(instance).data

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        delete_model(model=Country, pk=pk)

        return Response(data={
            "message": f"The tag with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)
