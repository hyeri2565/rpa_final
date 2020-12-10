from django.db import models
class Information(models.Model):
    RegName=models.CharField(max_length=5,help_text='Enter Registration customer name',null=False)
    FaxNum=models.CharField(max_length=12,help_text='Enter Fax number',null=False)
    PhNum=models.CharField(max_length=13,help_text='Enter Phone number',null=True)
    Cus_num=models.CharField(max_length=12,help_text='Enter Customer Number',null=False,primary_key=True)

class Content(models.Model):
    Order=models.CharField(max_length=5,help_text='Contents Order Number',null=False,primary_key=True)
    Main=models.TextField(help_text='real contents',null=False)
    def __str__(self):
        return self.Order
#field
# TextField 큰 임의 길이 문자열
# IntegerField 정수 값 저장함
# DataField 날짜 및 날짜/ 시간 정보 저장
#모델관리
#레코드 생성 및 수정
#record=Information(RegName='',FaxNum='')
#record=Information()
#record.PhNum=''
#record.save()
#레코드 검색하는 방법
#all_Infor=Information.objects.all()
#지정된 텍스트 또는 숫자 필드와 일치하도록 필터링
#sepcial_infor=Information.abjects.filter(RegName='김수정')

'''
    class Meta:
        ordering=['-my_field_name']
    def get_absolute_url(self):
        return reverse('model-detail-view',args=[str(self.id)])

    def __str__(self):
        return self.field_name
'''
# Create your models here.
