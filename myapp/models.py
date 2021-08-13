from django.db import models
from admin_api.fields import PasswordField

class City(models.Model):
    name = models.CharField('名称', max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '城市'

class Member(models.Model):
    name = models.CharField('名称', max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '成员'

        
class DemoField(models.Model):
    # 基础字段
    field_bool = models.BooleanField('BooleanField', default=True)
    field_char = models.CharField('CharField', max_length=10)
    field_date = models.DateField('DateField', blank=True, null=True)
    field_datetime = models.DateTimeField('DateTimeField', blank=True, null=True)
    field_number = models.DecimalField('DecimalField', max_digits=3, decimal_places=2, blank=True, null=True)
    field_duration = models.DurationField('DurationField', blank=True, null=True)
    field_email = models.EmailField('EmailField', blank=True, null=True)
    field_file = models.FileField('FileField', blank=True, null=True)
    field_image = models.ImageField('ImageField', blank=True, null=True)
    field_int = models.IntegerField('IntegerField', blank=True, null=True)
    field_ip = models.GenericIPAddressField('GenericIPAddressField', blank=True, null=True)
    field_text = models.TextField('TextField', blank=True, null=True)
    field_time = models.TimeField('TimeField', blank=True, null=True)
    # 关联字段
    field_m1 = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='ForeignKey', blank=True, null=True)
    field_m2 = models.ManyToManyField(Member, verbose_name='ManyToManyField', blank=True)
    # 密码
    field_password = PasswordField('密码', max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.field_char
    
    class Meta:
        verbose_name = '字段演示'
