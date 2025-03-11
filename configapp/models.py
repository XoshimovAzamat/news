from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='news')
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="get_news")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NEW"
        verbose_name_plural = "NEWS"
        ordering = ['-created_ed']

    @staticmethod
    def search_news(query):
        return News.objects.filter(
            Q(title__icontains=query) |
            Q(context__icontains=query)
        )

