from .models import Tag, Genre, Language, Country
import django_filters


class TagFilter(django_filters.FilterSet):
    ids = django_filters.BaseInFilter(field_name='pk', lookup_expr='in')


def tag_list(*, filters = None) -> list[Tag]:
    filters = {} or filters
    print(filters)
    qs = Tag.objects.all()

    filter = TagFilter(filters, qs)

    return filter.qs


def get_tag(pk: int) -> Tag:
    return Tag.objects.get(pk=pk)


def get_genre(pk: int) -> Genre:
    return Genre.objects.get(pk=pk)


def genre_list() -> list[Genre]:
    return Genre.objects.all()


def get_language(pk: int) -> Language:
    return Language.objects.get(pk=pk)


def language_list() -> list[Language]:
    return Language.objects.all()


def get_country(pk: int) -> Country:
    return Country.objects.get(pk=pk)


def country_list() -> list[Country]:
    return Country.objects.all()
