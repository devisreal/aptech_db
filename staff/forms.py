from django import forms
from .models import Staff


class EditStaffForm(forms.ModelForm):

   name = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={
            "placeholder": "", 
            "class": "border border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-10 p-2.5",
            "id": "name"
         }
      )
   )

   contact_no = forms.CharField(
      label='', 
      max_length=14,
      widget=forms.TextInput(
         attrs={
            "placeholder": "", 
            "class": "border border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-10 p-2.5",
            "id": "name",
            "maxlength": 14
         }
      )
   )

   email = forms.EmailField(
      label='',
      widget=forms.EmailInput(
         attrs={
            'placeholder': '',
            "class": "border border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-10 p-2.5",
            "id": "email"
         }
      )
   )

   role = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={
            "placeholder": "", 
            "class": "border border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-10 p-2.5",
            "id": "role"
         }
      )
   )

   date_employed = forms.DateField(
      label="",
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "border border-gray-300 text-gray-900 sm:text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-10 p-2.5  datepicker-input",
            "placeholder":"Date enrolled"

         }
      )
   )

   class Meta:
      model = Staff
      fields = ('name', 'contact_no', 'email', 'role', 'date_employed')
