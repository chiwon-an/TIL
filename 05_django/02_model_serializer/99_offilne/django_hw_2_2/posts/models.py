from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시 자동 기록
    updated_at = models.DateTimeField(auto_now=True)      # 저장 시마다 자동 갱신

    def __str__(self):
        return self.title