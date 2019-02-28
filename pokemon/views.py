from rest_framework import viewsets

from pokemon.filters import (AbilityFilter, ItemFilter, MoveFilter,
                             PokemonFilter, TypeFilter)
from pokemon.models import Ability, Item, Move, Pokemon, Type
from pokemon.pagination import PokemonPagination
from pokemon.permissions import IsAdminOrReadOnly
from pokemon.serializers import (AbilitySerializer, ItemSerializer,
                                 MoveSerializer, PokemonSerializer,
                                 TypeSerializer)


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    pagination_class = PokemonPagination
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = AbilityFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PokemonPagination
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = ItemFilter


class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    pagination_class = PokemonPagination
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = MoveFilter


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    pagination_class = PokemonPagination
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = PokemonFilter


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    pagination_class = PokemonPagination
    permission_classes = (IsAdminOrReadOnly,)
    filterset_class = TypeFilter
