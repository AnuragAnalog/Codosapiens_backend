from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=30)
    project_code = models.CharField(max_length=5)
    project_desc = models.CharField(max_length=300)
    project_start_date = models.DateField()

    def __str__(self):
        pname = self.project_name
        pcode = self.project_code

        return "Project Name: "+str(pname)+" "+"Project Code: "+str(pcode)