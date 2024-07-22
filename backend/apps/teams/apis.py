from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from apps.common.services import delete_model

from .permissions import IsTeamUser
from .models import Team
from .serializers import (
    TeamSerializer,
    TeamCreateSerializer,
    TeamUpdateSerializer
)

from .types import TeamObject

from .services import (
    create_team,
    update_team,
)

from .selectors import (
    get_teams,
    get_team,
)


class TeamsAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,
                          (IsAdminUser | IsTeamUser))

    def get(self, request):
        teams_list = get_teams()
        data = TeamSerializer(teams_list, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeamCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = create_team(
            TeamObject(**serializer.validated_data))

        data = TeamSerializer(instance).data

        return Response(data=data, status=status.HTTP_201_CREATED)


class TeamsDetailAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,
                          (IsAdminUser | IsTeamUser))

    def get(self, request, pk: int):
        team = get_team(pk)

        data = TeamSerializer(team).data

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        team = get_teams(pk)
        self.check_object_permissions(request, team)

        delete_model(model=Team, pk=pk)

        return Response(data={}, status=status.HTTP_200_OK)

    def patch(self, request, pk: int):
        team = get_teams(pk)
        self.check_object_permissions(request, team)

        serializer = TeamUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        team = update_team(
            pk, TeamObject(**serializer.validated_data))

        data = TeamSerializer(team).data

        return Response(data=data, status=status.HTTP_200_OK)