
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.novels.tests.factories import NovelFactory
from apps.chapters.tests.factories import ChapterFactory
from apps.novels.models import Novel
import markdown
import lorem


class Command(BaseCommand):
    help = 'Initialize test data for novels and chapters'

    def handle(self, *args, **options):
        self.create_novels()
        self.create_chapters()

    def create_novels(self):
        with transaction.atomic():
            for i in range(10):
                novel = NovelFactory()
                self.stdout.write(self.style.SUCCESS(f'Created novel {i}'))

    def create_chapters(self):
        with transaction.atomic():
            for novel in Novel.objects.all():
                for i in range(30):
                    chapter = ChapterFactory(
                        novel=novel, text=self.generate_markdown_lorem_ipsum())
                    self.stdout.write(self.style.SUCCESS(
                        f'Created chapter {i} for novel {novel.title}'))

    def generate_markdown_lorem_ipsum(self):
        lorem_text = lorem.text()
        markdown_text = markdown.markdown(lorem_text)
        return markdown_text
