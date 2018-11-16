# coding=utf-8
from haystack import indexes
from models import tinymceTest1


class tinymceTest1Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return tinymceTest1

    def index_queryset(self, using=None):
        return self.get_model().objects.all()