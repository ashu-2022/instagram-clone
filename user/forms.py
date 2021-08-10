from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'picture','full_name','username','email',
            'bio','website','phone_number','gender',
            'is_private_account',
        )

        # change the label name manually 
        labels ={
            'is_private_account':'Do you want to make your account private ?',
            'phone_number':'Phone',
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            if field =='picture':
                self.fields[field].widget.attrs.update({'class':'form-control-file'})
            elif field == 'is_private_account':
                self.fields[field].widget.attrs.update({'class':'form-control'})
            else:
                self.fields[field].widget.attrs.update({'class':'form-control form-control-sm '})


