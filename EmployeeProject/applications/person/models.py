from django.db import models

from applications.department.models import Department

from ckeditor.fields import RichTextField



class Skills(models.Model):
    skill = models.CharField('Skill', max_length=50)

    class Meta:
        verbose_name= 'Skill'
        #verbose_name_plural= 'Employee Skills'
        ordering= ['id']


    def __str__(self):
        return  self.skill  


class Employee(models.Model):
    
    """ Model for employee table """

    JOB_CHOICES= (

        ('0', 'Developer'), 
        ('1', 'Administrator'), 
        ('2', 'Support technician'), 
        ('3', 'Web designer'),
        ('5', 'Community Manager'),
        ('4', 'Others'),
 )   

    first_name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    full_name = models.CharField('Full Name', max_length=100, blank= True)
    job = models.CharField('Job', max_length=1, choices= JOB_CHOICES)
    # con esto relacionamos la db del models.py de department a este models
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee', blank= True, null= True)
    skills= models.ManyToManyField(Skills)
    #cv= RichTextField(blank= True)
 
    

    class Meta:
        verbose_name= 'My Employee'
        #verbose_name_plural= 'Company Employes'
        ordering= ['first_name']
        #unique_together= ('first_name')

    def __str__(self):
        return '-' + self.first_name +' '+ self.last_name