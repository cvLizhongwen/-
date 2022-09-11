from datetime import datetime

from django.db import models
# from users.models import UserProfile


# 定义种质model
class Server(models.Model):
    # 种质类型
    Gtype = models.ForeignKey('servers.ServerType', on_delete=models.CASCADE)
    ipaddress = models.CharField(max_length=100, verbose_name='存放地址', blank=True)
    description = models.CharField(max_length=50, verbose_name='相关信息描述', blank=True)

    Gke = models.CharField(max_length=50, verbose_name='科中文名', blank=True)
    # Gkel = models.CharField(max_length=50, verbose_name='科拉丁名', blank=True)
    Gs = models.CharField(max_length=50, verbose_name='属中文名', blank=True)
    # Gsl = models.CharField(max_length=50, verbose_name='属拉丁名', blank=True)
    Gz = models.CharField(max_length=50, verbose_name='种中文名', blank=True)
    # Gzl = models.CharField(max_length=50, verbose_name='种拉丁名', blank=True)
    Gnumber = models.CharField(max_length=50, verbose_name='种编号', blank=True)
    Gname = models.CharField(max_length=50, verbose_name='种子中文名', blank=True)
    # Gnamel = models.CharField(max_length=50, verbose_name='种子拉丁名', blank=True)
    Gyear = models.CharField(max_length=50, verbose_name='采集年份', blank=True)
    Gaddress = models.CharField(max_length=50, verbose_name='采集地', blank=True)

    Gdrought = models.CharField(max_length=50, verbose_name='抗旱性', blank=True)
    Gcold = models.CharField(max_length=50, verbose_name='抗寒性', blank=True)
    Gsalt = models.CharField(max_length=50, verbose_name='耐盐性', blank=True)
    Gfrost = models.CharField(max_length=50, verbose_name='耐霜冻性', blank=True)
    Gheat = models.CharField(max_length=50, verbose_name='耐热性', blank=True)
    Ginseck = models.CharField(max_length=50, verbose_name='抗虫害性性', blank=True)
    Gdisease = models.CharField(max_length=50, verbose_name='抗病性', blank=True)
    predisposingType = models.CharField(max_length=50, verbose_name='易感病型', blank=True)
    rootType = models.CharField(max_length=50, verbose_name='根系类型', blank=True)

    stem = models.CharField(max_length=50, verbose_name='茎状', blank=True)
    understem = models.CharField(max_length=50, verbose_name='地下茎', blank=True)
    leafType = models.CharField(max_length=50, verbose_name='叶的类型', blank=True)
    phyllotaxis = models.CharField(max_length=50, verbose_name='叶序', blank=True)
    vein = models.CharField(max_length=50, verbose_name='脉序', blank=True)
    leafShape = models.CharField(max_length=50, verbose_name='叶片形状', blank=True)
    anthotaxy = models.CharField(max_length=50, verbose_name='花序', blank=True)
    fruitType = models.CharField(max_length=50, verbose_name='果实类型', blank=True)

    zcnumber = models.CharField(max_length=50, verbose_name='种子现存重量', blank=True)
    owner = models.ForeignKey('users.UserProfile', on_delete=models.SET_NULL, null=True, blank=True)
    undernet = models.CharField(max_length=10, verbose_name='所在状况')

    comment = models.CharField(max_length=300, verbose_name='备注', blank=True)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')

    class Meta:
        verbose_name = '种质表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.undernet


# 定义种质类型model
class ServerType(models.Model):
    Gtype = models.CharField(max_length=20, verbose_name='种质类型')

    class Meta:
        verbose_name = '种质类型表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Gtype


# 定义种质历史model
class ServerHis(models.Model):
    serverid = models.IntegerField(verbose_name='种子ID')
    Gtype = models.CharField(max_length=20, verbose_name='种子类型')
    Gke = models.CharField(max_length=50, verbose_name='科中文名', blank=True)
    # Gkel = models.CharField(max_length=50, verbose_name='科拉丁名', blank=True)
    Gs = models.CharField(max_length=50, verbose_name='属中文名', blank=True)
    # Gsl = models.CharField(max_length=50, verbose_name='属拉丁名', blank=True)
    Gz = models.CharField(max_length=50, verbose_name='种中文名', blank=True)
    # Gzl = models.CharField(max_length=50, verbose_name='种拉丁名', blank=True)
    Gnumber = models.CharField(max_length=50, verbose_name='种编号', blank=True)
    Gname = models.CharField(max_length=50, verbose_name='种子中文名', blank=True)
    # Gnamel = models.CharField(max_length=50, verbose_name='种子拉丁名', blank=True)
    Gyear = models.CharField(max_length=50, verbose_name='采集年份', blank=True)
    Gaddress = models.CharField(max_length=50, verbose_name='采集地', blank=True)

    Gdrought = models.CharField(max_length=50, verbose_name='抗旱性', blank=True)
    Gcold = models.CharField(max_length=50, verbose_name='抗寒性', blank=True)
    Gsalt = models.CharField(max_length=50, verbose_name='耐盐性', blank=True)
    Gfrost = models.CharField(max_length=50, verbose_name='耐霜冻性', blank=True)
    Gheat = models.CharField(max_length=50, verbose_name='耐热性', blank=True)
    Ginseck = models.CharField(max_length=50, verbose_name='抗虫害性性', blank=True)
    Gdisease = models.CharField(max_length=50, verbose_name='抗病性', blank=True)
    predisposingType = models.CharField(max_length=50, verbose_name='易感病型', blank=True)
    rootType = models.CharField(max_length=50, verbose_name='根系类型', blank=True)

    stem = models.CharField(max_length=50, verbose_name='茎状', blank=True)
    understem = models.CharField(max_length=50, verbose_name='地下茎', blank=True)
    leafType = models.CharField(max_length=50, verbose_name='叶的类型', blank=True)
    phyllotaxis = models.CharField(max_length=50, verbose_name='叶序', blank=True)
    vein = models.CharField(max_length=50, verbose_name='脉序', blank=True)
    leafShape = models.CharField(max_length=50, verbose_name='叶片形状', blank=True)
    anthotaxy = models.CharField(max_length=50, verbose_name='花序', blank=True)
    fruitType = models.CharField(max_length=50, verbose_name='果实类型', blank=True)

    ipaddress = models.CharField(max_length=100, verbose_name='存放地址', blank=True)
    description = models.CharField(max_length=50, verbose_name='相关信息描述', blank=True)

    zcnumber = models.CharField(max_length=50, verbose_name='种子现存重量', blank=True)
    owner = models.CharField(max_length=20, verbose_name='管理人员')
    undernet = models.CharField(max_length=10, verbose_name='所在状况')
    comment = models.CharField(max_length=300, verbose_name='备注', blank=True)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')

    class Meta:
        verbose_name = '种质历史表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Gtype
