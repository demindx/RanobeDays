from .models import Chapter
from django.db.models import QuerySet, ObjectDoesNotExist
import django_filters


class ChapterFilter(django_filters.FilterSet):
    novel = django_filters.NumberFilter(field_name='novel')
    order_by = django_filters.OrderingFilter(
        fields=(
            ('updated_at', 'updated'),
            ('created_at', 'added')
        )
    )

    class Meta:
        model = Chapter
        fields = ('novel', )


def get_chapters_list(*, novel_slug) -> QuerySet[Chapter]:
    result = Chapter.objects.filter(novel__slug=novel_slug)

    if result.exists():
        return result

    raise ObjectDoesNotExist(f'Novel with slug - {novel_slug} does not exist')


def get_chapter_by_id(pk: int) -> Chapter:
    return Chapter.objects.get(pk=pk)


def get_chapter_list_by_slice(slice: tuple[int], novel_slug: str) -> QuerySet[Chapter]:
    chapters = get_chapters_list(novel_slug=novel_slug)

    return chapters[slice[0]:slice[1]]
