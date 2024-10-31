# import pandoc
from pandoc.types import *
from apps.chapters.selectors import get_chapter_list_by_slice
from apps.chapters.models import Chapter
from django.db.models import QuerySet
from django.utils.text import slugify


def _get_data(chapters: QuerySet[Chapter]):
    meta = Meta({})
    meta[0]['title'] = MetaInlines([Str(chapters[0].novel.title)])
    blocks = []
    for chapter in chapters:
        blocks.append(Header(
            1, (f'chpater-{chapter.volume}-{chapter.number}-{chapter.title}', [], []), [Str(f'{chapter.volume}'), Str('.'), Str(f'{chapter.number}'), Space(), Str(f'{chapter.title}')]))
        for item in pandoc.read(chapter.text)[1]:
            blocks.append(item)

    return Pandoc(meta, blocks)


def convert_to_format(chapters_slice: tuple[int], novel_slug: str):
    chapters = get_chapter_list_by_slice(chapters_slice, novel_slug)
    data = _get_data(chapters)

    with open(f'test.epub2', 'wb') as file:
        file.write(pandoc.write(data, format='epub2'))

        file.close()
