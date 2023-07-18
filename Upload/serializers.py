from rest_framework import serializers
from .models import *
import shutil



class Filelist_serializer(serializers.Serializer):

    class Meta:
        model = uploaded_files
        fields = "__all__"


class Filelist_serializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(allow_empty_file = False)
    )

    folder = serializers.CharField(required = False)


    def zip_file(self,folder):
        shutil.make_archive(f'media/zip_folders/{folder}','zip',f'media/uploaded_files/{folder}')




    def create(self, validated_data):

        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = uploaded_files.objects.create(folder = folder, file = file)
            files_objs.append(files_obj)

        self.zip_file(folder.uid)

        return {'files' : files_objs, 'folder' : str(folder.uid)}