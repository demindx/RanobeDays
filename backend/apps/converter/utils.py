import pandoc
from pandoc.types import *
from apps.chapters.selectors import get_chapter_list_by_slice
from apps.chapters.models import Chapter
from django.db.models import QuerySet
from django.conf import settings


def _get_doc(chapters: QuerySet[Chapter]):
    meta = Meta({})

    meta[0]['title'] = MetaInlines([Str(chapters[0].novel.title)])
    meta[0]['author'] = MetaInlines([Str(chapters[0].novel.creator.name)])

    blocks = []
    for chapter in chapters:
        blocks.append(Header(
            1, (f'chpater-{chapter.volume}-{chapter.number}-{chapter.title}', [], []), [Str(f'{chapter.volume}'), Str('.'), Str(f'{chapter.number}'), Space(), Str(f'{chapter.title}')]))
        for item in pandoc.read(chapter.text)[1]:
            blocks.append(item)

    return Pandoc(meta, blocks)


def convert_to_file(chapters_slice: tuple[int], novel_slug: str, format: str = 'epub'):
    chapters = get_chapter_list_by_slice(chapters_slice, novel_slug)
    data = _get_doc(chapters)

    return pandoc.write(data, format=format, options=[
        f'--css={settings.CONVERTER_CSS_FILE}'
    ])
