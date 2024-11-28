from rest_framework.views import APIView
from .utils import convert_to_file
from django.http import FileResponse
from rest_framework.permissions import AllowAny
import io


class DownloadChapterSliceOfNovelAPI(APIView):
    permission_classes = (AllowAny,)

    FORMAT_TYPES_TO_FILE_TYPES = {
        "epub": "epub3",
        "docx": "docx",
        "fb2": "fb2",
        "markdown": "md",
        "pdf": "pdf",
    }

    def get(self, request, slug: str, chapters_slice: tuple[int], file_format: str):
        file = convert_to_file(chapters_slice, slug, file_format)

        if isinstance(file, str):
            file = bytes(file, "utf-8")

        byte_stream = io.BytesIO(file)
        byte_stream.seek(0)

        response = FileResponse(
            byte_stream,
            as_attachment=True,
            filename=f"{slug}-from-chpater-\
                            {chapters_slice[0]}-to-{chapters_slice[1]}.\
                            {self.FORMAT_TYPES_TO_FILE_TYPES[file_format]}",
        )

        response["Content-Type"] = "application/octet-stream"

        return response
