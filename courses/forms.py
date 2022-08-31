from django import forms
from . import models

class EditCourseForm(forms.ModelForm):

   name = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={
            "placeholder": "", 
            "class": "w-full text-md py-2 pl-3 mt-3 pr-4 text-gray-700 bg-white border border-gray-300 rounded-md  focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring",
            "id": "name"
         }
      )
   )

   duration = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={
            "placeholder": "", 
            "class": "w-full text-md py-2 pl-3 mt-3 pr-4 text-gray-700 bg-white border border-gray-300 rounded-md  focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring",
            "id": "duration"
         }
      )
   )

   description = forms.CharField(
      label='',
      widget=forms.Textarea(
         attrs={
            'placeholder': '',
            'class': 'w-full text-md py-2 pl-3 mt-3 pr-4 text-gray-700 bg-white border border-gray-300 rounded-md  focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring',
            'id': 'description',
            'rows': '7',         
         }
      )
   )

   price = forms.CharField(
      label='',
      widget=forms.NumberInput(
         attrs={
            "placeholder": "",
            "class": "w-full text-md py-2 pl-3 mt-3 pr-4 text-gray-700 bg-white border border-gray-300 rounded-md  focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring",
            "id": "price"
         }
      )
   )


   class Meta:
      model = models.Courses
      fields = ('name', 'duration', 'description', 'price')