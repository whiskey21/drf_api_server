from django.db import models
from django.contrib.auth.models import User #User는 어드민용
##모델 테이블
class Member(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #어떤 어드민계정에서 추가되었는지 확인용
    id = models.BigAutoField(help_text="Member ID", primary_key=True)
    name = models.CharField(max_length=144) #얼굴 모델 등록시 사용한 이름
    email = models.CharField(max_length=144, blank=True)    #email
    info = models.TextField()   #추가정보
    created_at = models.DateTimeField(auto_now_add=True)    #생성일시

    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.name)