from django import forms
from .models import Plan, Object

# class Writing(forms.ModelForm):
#     class Meta:
#         model = Plan
#         fields = ['title', 's1', 'd1', 's2', 'd2', 's3', 'd3', 's4', 'd4', 's5', 'd5', 's6', 'd6', 's7', 'd7', 's8', 'd8', 's9', 'd9', 's10', 'd10', 'memo']


#     def __init__(self, *args, **kwargs):
#         super(Writing, self).__init__(*args, **kwargs)
#         self.fields['s1'].required = False
#         self.fields['s2'].required = False
#         self.fields['s3'].required = False
#         self.fields['s4'].required = False
#         self.fields['s5'].required = False
#         self.fields['s6'].required = False
#         self.fields['s7'].required = False
#         self.fields['s8'].required = False
#         self.fields['s9'].required = False
#         self.fields['s10'].required = False
#         self.fields['d1'].required = False
#         self.fields['d2'].required = False
#         self.fields['d3'].required = False
#         self.fields['d4'].required = False
#         self.fields['d5'].required = False
#         self.fields['d6'].required = False
#         self.fields['d7'].required = False
#         self.fields['d8'].required = False
#         self.fields['d9'].required = False
#         self.fields['d10'].required = False
#         self.fields['memo'].required = False

class Writing(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 's1', 'd1', 's2', 'd2', 's3', 'd3', 's4', 'd4', 's5', 'd5', 's6', 'd6', 's7', 'd7', 's8', 'd8', 's9', 'd9', 's10', 'd10', 'memo']

    def __init__(self, *args, **kwargs):
        super(Writing, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': '제목을 입력하세요.'})
        for i in range(1, 11):
            self.fields[f's{i}'].required = False
            self.fields[f'd{i}'].required = False
        self.fields['memo'].required = False
        
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if Plan.objects.exclude(id=self.instance.id).filter(title=title).exists():
    #         raise forms.ValidationError('중복된 이름은 사용할 수 없습니다.')
    #     return title
    

class Checking(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10']


class GoalForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['description_1', 'description_2', 'description_3', 'description_4', 'description_5']


class Time(forms.ModelForm):
    class Meta:
        model = Plan
        prefixes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2]

        fields = [f"t{prefix}_{suffix}" for prefix in prefixes for suffix in range(1,7)]

