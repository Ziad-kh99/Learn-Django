from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        #> Model that we will crate form for:
        model = Project

        #> Fields that we need to include in the form:
        # fields = ['title', 'description']
        fields = '__all__'                      # to include all the fields from model to form.
        exclude = ['vote_total', 'vote_ratio']  # to exculde a specific fields.