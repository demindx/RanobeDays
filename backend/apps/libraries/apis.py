from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.common.services import delete_model

from .models import Library, LibraryItem

from .types import (
    LibraryItemObject,
    LibraryObject
)

from .serializers import (
    LibrarySerializer,
    LibraryCreateUpdateSerializer,
    LibraryItemSerializer,
    LibraryItemCreateUpdateSerializer
)

from .services import (
    create_library,
    update_library,
    create_library_item,
    update_library_item
)

from .selectors import (
    get_library,
    get_libraries,
    get_library_item,
    get_library_items
)


class LibraryAPI(APIView):
    """API thats return list of Library instances or creates the instance"""

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request) -> Response:
        libraries = get_libraries()

        data = LibrarySerializer(libraries, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        library_object = LibraryObject(
            name=serializer.validated_data["name"], user=request.user)

        library = create_library(library_object)

        data = LibrarySerializer(library).data
        return Response(data=data, status=status.HTTP_200_OK)


class LibraryDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Library"""

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, pk: int) -> Response:
        library = get_library(pk)

        data = LibrarySerializer(library).data

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int) -> Response:
        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        library_object = LibraryObject(
            name=serializer.validated_data['name'], user=request.user)

        library = update_library(pk, library_object)

        data = LibrarySerializer(library).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        delete_model(model=Library, pk=pk)

        return Response(data={}, status=status.HTTP_200_OK)


class LibraryItemAPI(APIView):
    """API thats return list of LibraryItem instances or
    creates the instance"""

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        items = get_library_items()

        data = LibraryItemSerializer(items, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LibraryItemCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_object = LibraryItemObject(**serializer.validated_data)
        item = create_library_item(item_object)

        data = LibraryItemSerializer(item).data
        return Response(data=data, status=status.HTTP_200_OK)


class LibraryItemDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Library"""

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, pk: int):
        item = get_library_item(pk)

        data = LibraryItemSerializer(item).data
        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        serializer = LibraryItemCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_object = LibraryItemObject(**serializer.validated_data)
        item = update_library_item(pk, item_object)

        data = LibraryItemSerializer(item).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        delete_model(model=LibraryItem, pk=pk)

        return Response(data={}, status=status.HTTP_200_OK)
