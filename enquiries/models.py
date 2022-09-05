from django.db import models
from multiselectfield import MultiSelectField
from django.template.defaultfilters import slugify

class Enquires(models.Model):
   educational_qualifications_list = (      
      ('High School', 'High School'),
      ('Undergraduate', 'Undergraduate'),
      ('Graduate', 'Graduate'),
      ('Vocational School', 'Vocational School'),      
   )
   how_you_heard_list = (      
      ('Seminar', 'Seminar'),
      ('Newspapers', 'Newspapers'),
      ('Billboard', 'Billboard'),
      ('Internet', 'Internet'),
      ('Friends/Relatives', 'Friends/Relatives'),
      ('Fliers/Handbills', 'Fliers/Handbills'),      
   )
   course_of_interest_list = (      
      ('Software Programming', 'Software Programming'),
      ('System Engineer', 'System Engineer'),
      ('Hardware/Networking', 'Hardware/Networking'),           
   )

   enquiry_no = models.PositiveIntegerField(blank=True, unique=True)
   surn_name = models.CharField(max_length=100)
   first_name = models.CharField(max_length=100)
   middlename = models.CharField(max_length=100, blank=True)
   address = models.CharField(max_length=200, blank=True)
   contact_no = models.CharField(max_length=14, blank=True)
   email = models.EmailField(max_length=100, blank=True)
   date_of_birth = models.DateField(blank=True, null=True)
   guardians_name = models.CharField(max_length=200, blank=True)
   guardians_contact_no = models.CharField(max_length=14, blank=True)
   educational_qualifications = MultiSelectField(choices=educational_qualifications_list, blank=True)
   eductional_others = models.CharField(max_length=200, blank=True)
   how_you_heard = MultiSelectField(choices=how_you_heard_list, blank=True)
   how_you_heard_others = models.CharField(max_length=200, blank=True)
   course_of_interest = MultiSelectField(choices=course_of_interest_list, blank=True)
   course_of_interest_others = models.CharField(max_length=200, blank=True)
   
   counselor = models.CharField(max_length=200, blank=True)
   remark = models.TextField(blank=True)
   date = models.DateField(blank=True, null=True)
   
   date_posted = models.DateTimeField(auto_now_add=True)
   slug = models.SlugField(null=True, blank=True)

   def __str__(self):
      return f"{self.first_name} {self.surn_name} on {self.date}"

   def save(self, *args, **kwargs):
      self.slug = slugify(self.enquiry_no)
      super().save(*args, **kwargs)

   class Meta:
      verbose_name = 'Enquiry'
      verbose_name_plural = 'Enquiries'