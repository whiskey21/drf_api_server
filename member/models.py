from django.db import models
from django.contrib.auth.models import User #User는 어드민용
##모델 테이블
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #어떤 어드민계정에서 추가되었는지 확인용
    id = models.BigAutoField(help_text="Member ID", primary_key=True)
    name = models.CharField(max_length=144, null=True) #얼굴 모델 등록시 사용한 이름
    phoneNum = models.CharField(max_length=144, blank=True, null=True)    #email

    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.name)
#
# class Enterance(models.Model):
#     eid = models.BigAutoField(help_text= "Enterance ID", primary_key = True)
#     memberID = models.ForeignKey(Member, related_name="member",on_delete=models.CASCADE, db_column='memberID')
#     enterance_time = models.