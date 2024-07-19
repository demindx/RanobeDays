from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.views import APIView
from rest_framework import status

from apps.metadata.models import Language
from apps.metadata.types import LanguageObject
from apps.metadata.serializers import LanguageSerializer
from apps.common.services import delete_model

from apps.metadata.selectors import (
    language_list,
    get_language
)


from apps.metadata.services import (
    update_language,
    create_language
)


class LanguageAPI(APIView):
    """API for getting list of tags or creating instances"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request) -> Response:
        queryset = language_list()

        data = LanguageSerializer(queryset, many=True).data

        return Response(data)

    def post(self, request) -> Response:
        serializer = LanguageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_language(LanguageObject(**serializer.validated_data))

        data = LanguageSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class LanguageDetailAPI(APIView):
    """API for getting, deletin, updating the instance of tag"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk: int) -> Response:
        tag = get_language(pk=pk)

        data = LanguageSerializer(tag).data

        return Response(data)

    def patch(self, request, pk: int) -> Response:

        serializer = LanguageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = update_language(pk=pk, data=LanguageObject(
            **serializer.validated_data))

        data = LanguageSerializer(instance).data

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        delete_model(model=Language, pk=pk)

        return Response(data={
            "message": f"The tag with id {pk} was successfuly deleted"
        },
            status=status.HTTP_200_OK)
