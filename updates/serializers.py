from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =fields = ['ProjectCode', 'ProjectTitle', 'ProjectDescription', 'ProposalLink', 'Round', 'Pool', 'ContractStatus', 'ContractLink', 'TotalAmount', 'TotalDisbursed', 'TotalNumberOfMilestones', 'NumberOfDoneMilestones', 'PercentageDone', 'ProjectStatus', 'DateOfLastUpdate', 'HasService', 'StartDate', 'EndDate', 'Remark']
