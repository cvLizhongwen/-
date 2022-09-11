from django import forms

from .models import Server, ServerType


# 定义资产表单验证
class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['Gtype', 'Gnumber', 'Gname', 'Gz', 'Gs', 'Gke', 'Gyear', 'Gaddress',
                  'Gdrought', 'Gcold', 'Gsalt', 'Gfrost', 'Gheat', 'Ginseck', 'Gdisease', 'predisposingType',
                  'rootType', 'stem', 'understem', 'leafType', 'phyllotaxis', 'vein', 'leafShape',
                  'ipaddress', 'description', 'undernet', 'anthotaxy', 'fruitType',
                  'comment']

# 定义种质类型表单验证
class ServerTypeForm(forms.ModelForm):
    class Meta:
        model = ServerType
        fields = ['Gtype']

