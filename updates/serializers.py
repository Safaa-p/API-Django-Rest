from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =fields = [ 'ProjectCode', 'ProjectTitle', 'ProjectDescription', 'ProposalLink', 'Round', 'ContractStatus', 'TotalAmount', 'TotalDisbursed', 'TotalNumberOfMilestones', 'NumberOfDoneMilestones', 'DateOfLastUpdate']

         