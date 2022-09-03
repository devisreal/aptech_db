from django import forms
from courses.models import Courses
from .models import Student


class AddStudentForm(forms.ModelForm):

   studentId = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Student1234567", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "studentId"
         }
      )
   )

   first_name = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={
            "placeholder": "Adekunle", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "first_name"
         }
      )
   )

   middle_name = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Usman", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "middle_name"
         }
      )
   )

   last_name = forms.CharField(
      label='', 
      widget=forms.TextInput(
         attrs={
            "placeholder": "Okorocha", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "last_name"
         }
      )
   )

   gender_choices =  [      
      ('Male', 'Male'),
      ('Female', 'Female'),
      ('Custom', 'Custom'),
   ]

   gender = forms.ChoiceField(
      choices=gender_choices,
      widget=forms.Select(
         attrs={
            'class': 'font-mulish font border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full px-3 p-2.5',
            'id': 'gender'
         }
      )
   )  

   email = forms.EmailField(
      label='',
      required=False,
      widget=forms.EmailInput(
         attrs={
            'placeholder': 'student@email.com',
            'class': 'border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5'
         }
      ),
   )

   date_of_birth = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "border border-gray-300 text-gray-900 sm:text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5  datepicker-input",
            "placeholder":"",
            "id": 'date_of_birth'
         }
      )
   )

   address = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "1, Abuja Street, Banana Island", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "address"
         }
      )
   )

   contact_no = forms.CharField(
      label='',
      max_length=14,
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "+234...",             
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "contact_no",
            "maxlength": 14
         }
      )
   )

   date_enrolled = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "border border-gray-300 text-gray-900 sm:text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5  datepicker-input",
            "placeholder":"",
            "id": 'date_enrolled'
         }
      )
   )

   guardians_name = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Mr. James Bond", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "guardians_name"
         }
      )
   )

   guardians_contact_no = forms.CharField(
      label='',
      max_length=14,
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "+234...",             
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "guardians_contact_no",
            "maxlength": 14
         }
      )
   )

   courses = forms.ModelMultipleChoiceField(      
      label='',
      queryset=Courses.objects.all(),
      widget=forms.SelectMultiple(         
         attrs={
            'class': 'border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5',
            'id': 'courses'
         }
      )
   )   

   class Meta:
      model = Student
      fields = (
         'studentId',
         'first_name',
         'middle_name',
         'last_name',
         'gender',
         'email',
         'date_of_birth',
         'address',
         'contact_no',
         'guardians_name',
         'guardians_contact_no',
         'courses',
         'completed_programs',
         'date_enrolled',         
      )