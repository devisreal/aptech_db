from django import forms
from .models import Enquires


class AddEnquiryForm(forms.ModelForm):   

   enquiry_no = forms.CharField(
      label='',
      required=False,
      widget=forms.NumberInput(
         attrs={
            "placeholder": "0000", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "enquiry_no"
         }
      )
   )

   surn_name = forms.CharField(
      label='',       
      widget=forms.TextInput(
         attrs={
            "placeholder": "Alakori", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "surn_name"
         }
      )
   )

   first_name = forms.CharField(
      label='',       
      widget=forms.TextInput(
         attrs={
            "placeholder": "Daniel", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "first_name"
         }
      )
   )

   middlename = forms.CharField(
      label='',   
      required=False,    
      widget=forms.TextInput(
         attrs={
            "placeholder": "James", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "middlename"
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

   email = forms.EmailField(
      label='',
      required=False,
      widget=forms.EmailInput(
         attrs={
            'placeholder': 'enquirer@email.com',
            'class': 'border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5',
            'id': 'email'
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

   educational_qualifications_list = [
      ('High School', 'High School'),
      ('Undergraduate', 'Undergraduate'),
      ('Graduate', 'Graduate'),
      ('Vocational School', 'Vocational School'),      
   ]


   eductional_others = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Qualification", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "eductional_others"
         }
      )
   )

   how_you_heard_list = (      
      ('Seminar', 'Seminar'),
      ('Newspapers', 'Newspapers'),
      ('Billboard', 'Billboard'),
      ('Internet', 'Internet'),
      ('Friends/Relatives', 'Friends/Relatives'),
      ('Fliers/Handbills', 'Fliers/Handbills'),      
   )
   

   how_you_heard_others = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "through...", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "eductional_others"
         }
      )
   )

   course_of_interest_list = (      
      ('Software Programming', 'Software Programming'),
      ('System Engineer', 'System Engineer'),
      ('Hardware/Networking', 'Hardware/Networking'),           
   )
   

   course_of_interest_others = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Course", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "course_of_interest_others"
         }
      )
   )

   counselor = forms.CharField(
      label='', 
      required=False,
      widget=forms.TextInput(
         attrs={
            "placeholder": "Mr. Gbadebo", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "counselor"
         }
      )
   )

   remark = forms.CharField(
      label='',
      required=False,
      widget=forms.Textarea(
         attrs={
            "placeholder": "Remark", 
            "class": "border placeholder:font-normal font-semibold mt-1 mb-3 border-gray-300 text-gray-900 text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5",
            "id": "remark",
            'style': 'height: 100px'
         }
      )
   )

   date = forms.DateField(
      label="",
      required=False,
      widget=forms.DateInput(
         attrs={
            "type":"date",
            "class": "font-mulish border border-gray-300 text-gray-900 sm:text-md rounded-lg focus:border-darkBlue focus:ring-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring block w-full pl-3 p-2.5  datepicker-input",
            "placeholder":"",
            "id": 'date'
         }
      )
   )

   class Meta:
      model = Enquires
      fields = (
         'enquiry_no',
         'surn_name',
         'first_name',
         'middlename',
         'address',
         'contact_no',
         'email',
         'date_of_birth',
         'guardians_name',
         'guardians_contact_no',
         'educational_qualifications',
         'eductional_others',
         'how_you_heard',
         'how_you_heard_others',
         'course_of_interest',
         'course_of_interest_others',
         'counselor',
         'remark',
         'date'
      )