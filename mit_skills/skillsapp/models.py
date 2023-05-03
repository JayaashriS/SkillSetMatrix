from django.db import models

# Create your models here.

class Member(models.Model):
    username=models.CharField(primary_key=True,max_length=30)

    def __str__(self):
        return self.username
    
class SkillSet(models.Model):
    skill_Id=models.IntegerField()
    Skill_Category=models.CharField(max_length=200)
    Skills_Name= models.CharField(primary_key=True,max_length=200)

    def __str__(self):
        return self.Skill_Category
    
class Skillsmatrix(models.Model):

    Skills_Name=models.ForeignKey(SkillSet,on_delete=models.CASCADE)
    username=models.ForeignKey(Member,on_delete=models.CASCADE)
    proficiency= models.CharField(max_length=200)
    Is_Trained=models.CharField(max_length=4)
    Is_Certified=models.CharField(max_length=4)
    total_experience=models.CharField(max_length=10)
    certifications=models.CharField(max_length=100)
    assessment_date=models.DateField(auto_now=False, auto_now_add= False,blank= True, null=True)

    updated_at=models.DateTimeField(auto_now=True)
    
