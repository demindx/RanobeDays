from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from apps.common.services import delete_model

from .models import Library, LibraryItem

from .types import (
    LibraryItemObject,
    LibraryObject
)

from .permissions import (
    IsLibraryOwner,
    IsLibraryItemOwner
)

from .serializers import (
    LibrarySerializer,
    LibraryCreateUpdateSerializer,
    LibraryItemSerializer,
    LibraryItemCreateUpdateSerializer,
    LibraryFilterSerializer
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

    permission_classes = (IsLibraryOwner | IsAdminUser, )

    def get(self, request) -> Response:
        filter_serializer = LibraryFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        libraries = get_libraries(filters=filter_serializer.validated_data)

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

    permission_classes = (IsLibraryOwner | IsAdminUser,)

    def get(self, request, library_id: int) -> Response:
        library = get_library(library_id)

        data = LibrarySerializer(library).data

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, library_id: int) -> Response:
        library = get_library(library_id)
        self.check_object_permissions(library, request)

        serializer = LibraryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        library_object = LibraryObject(
            name=serializer.validated_data['name'], user=request.user)

        library = update_library(library_id, library_object)

        data = LibrarySerializer(library).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, library_id: int) -> Response:
        library = get_library(library_id)
        self.check_object_permissions(library, request)

        delete_model(model=Library, pk=library_id)

        return Response(data={}, status=status.HTTP_200_OK)


class LibraryItemAPI(APIView):
    """API thats return list of LibraryItem instances or
    creates the instance"""

    permission_classes = (IsLibraryItemOwner | IsAdminUser, )

    def get(self, request, library_id: int):
        items = get_library_items(library_id)

        data = LibraryItemSerializer(items, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, library_id: int):
        serializer = LibraryItemCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_object = LibraryItemObject(**serializer.validated_data)
        item_object.library = library_id

        item = create_library_item(item_object)

        data = LibraryItemSerializer(item).data
        return Response(data=data, status=status.HTTP_200_OK)


class LibraryItemDetailAPI(APIView):
    """API for getting, updating, deleting the instance of Library"""

    permission_classes = (IsLibraryItemOwner | IsAdminUser,)

    def get(self, request, library_id: int, library_item_id: int):
        item = get_library_item(library_item_id)

        data = LibraryItemSerializer(item).data
        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, library_id: int, library_item_id: int):
        serializer = LibraryItemCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item_object = LibraryItemObject(**serializer.validated_data)
        item = update_library_item(library_item_id, item_object)

        data = LibraryItemSerializer(item).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, library_id: int, library_item_id: int):
        delete_model(model=LibraryItem, pk=library_item_id)

        return Response(data={}, status=status.HTTP_200_OK)
