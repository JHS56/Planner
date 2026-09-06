from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# from django.utils import timezone

# import datetime


class Plan(models.Model):
    prefixes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2]
    suffixes = range(1, 7)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    title = models.CharField(max_length=20)
    # pub_date = models.DateTimeField("date published")

    # s 는 과목, d 는 설명
    s1 = models.CharField(max_length=10, blank=True)
    d1 = models.TextField(blank=True)
    s2 = models.CharField(max_length=10, blank=True)
    d2 = models.TextField(blank=True)
    s3 = models.CharField(max_length=10, blank=True)
    d3 = models.TextField(blank=True)
    s4 = models.CharField(max_length=10, blank=True)
    d4 = models.TextField(blank=True)
    s5 = models.CharField(max_length=10, blank=True)
    d5 = models.TextField(blank=True)
    s6 = models.CharField(max_length=10, blank=True)
    d6 = models.TextField(blank=True)
    s7 = models.CharField(max_length=10, blank=True)
    d7 = models.TextField(blank=True)
    s8 = models.CharField(max_length=10, blank=True)
    d8 = models.TextField(blank=True)
    s9 = models.CharField(max_length=10, blank=True)
    d9 = models.TextField(blank=True)
    s10 = models.CharField(max_length=10, blank=True)
    d10 = models.TextField(blank=True)

    memo = models.TextField(blank=True)

    c1 = models.BooleanField(default=False)
    c2 = models.BooleanField(default=False)
    c3 = models.BooleanField(default=False)
    c4 = models.BooleanField(default=False)
    c5 = models.BooleanField(default=False)
    c6 = models.BooleanField(default=False)
    c7 = models.BooleanField(default=False)
    c8 = models.BooleanField(default=False)
    c9 = models.BooleanField(default=False)
    c10 = models.BooleanField(default=False)

    for prefix in prefixes:
        for suffix in suffixes:
            field_name = f"t{prefix}_{suffix}"
            locals()[field_name] = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

    def clean(self):
        # 특정 문자 검증
        forbidden_chars = ['/', "\\", '.']
        if any(char in self.title for char in forbidden_chars):
            raise ValidationError('해당 특수문자는 사용할 수 없습니다.')
    

        # if Plan.objects.filter(title=self.title).exists():
        #     raise ValidationError("중복된 이름은 사용할 수 없습니다.")

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    description_1 = models.CharField(max_length=255, blank=True)
    description_2 = models.CharField(max_length=255, blank=True)
    description_3 = models.CharField(max_length=255, blank=True)
    description_4 = models.CharField(max_length=255, blank=True)
    description_5 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.description_1}, {self.description_2}, {self.description_3}, {self.description_4}, {self.description_5}"
    