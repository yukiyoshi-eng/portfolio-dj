from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
    template_name = "pf_template/index.html"

    def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context["message"] = "Template Viewの変数"
         return context