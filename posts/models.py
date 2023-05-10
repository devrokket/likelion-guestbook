from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True) # 챌린지 과제: filter orm을 이용하기. 더미데이터를 만들어서 get으로 불러오는데 시간을 조건으로 해서 불러오기. 

    class Meta:
        abstract = True

class Post(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    writer = models.CharField(verbose_name="작성자", max_length=30)
    content = models.TextField(verbose_name="내용")
