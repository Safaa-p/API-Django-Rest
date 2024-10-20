from django.db import models

class Project(models.Model):

    ProjectCode = models.CharField(max_length=200, primary_key=True)
    ProjectTitle = models.CharField(max_length=200)
    ProjectDescription = models.TextField()
    ProposalLink = models.CharField(max_length=200)
    Round = models.CharField(max_length=200)
    Pool = models.CharField(max_length=200)
    ContractStatus = models.CharField(max_length=200)
    ContractLink = models.CharField(max_length=200)
    TotalAmount = models.FloatField()
    TotalDisbursed = models.FloatField()
    TotalNumberOfMilestones= models.IntegerField()
    NumberOfDoneMilestones= models.IntegerField()
    PercentageDone = models.FloatField()
    ProjectStatus = models.TextField()
    DateOfLastUpdate = models.TextField()
    HasService= models.BooleanField()
    StartDate = models.TextField()
    EndDate = models.TextField()
    Remark = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'Projects'
    def __str__(self):
        return self.ProjectTitle