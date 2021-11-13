from django.db import models
from django.contrib.auth.models import User #User는 어드민용
##모델 테이블
class Member(models.Model):
    id = models.BigAutoField(help_text="Member ID", primary_key=True)
    name = models.CharField(max_length=144, null=True) #얼굴 모델 등록시 사용한 이름
    phoneNum = models.CharField(max_length=144, blank=True, null=True)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.name)

class Enterance(models.Model):
    eid = models.BigAutoField(help_text= "Enterance ID", primary_key = True)
    memberID = models.ForeignKey(Member, related_name="member",on_delete=models.CASCADE, db_column='memberID')
    enterance_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.enterance_time)
