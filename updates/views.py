from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from rest_framework_api_key.permissions import HasAPIKey

class ProjectByRoundApiView(APIView):
    permission_classes = [HasAPIKey]

    def get_projects_by_round(self, round, start_date, end_date):
        '''
        Retrieves projects based on round and date range
        '''
        try:
            return Project.objects.filter(Round=round, DateOfLastUpdate__range=[start_date, end_date]).values(
                'ProjectCode', 'ProjectTitle', 'ProjectDescription', 'ProposalLink', 'Round', 'ContractStatus', 'TotalAmount', 'TotalDisbursed', 'TotalNumberOfMilestones', 'NumberOfDoneMilestones', 'DateOfLastUpdate'
            )
        except Project.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        '''
        Retrieves the Projects for the given round within the specified date range
        '''
        round = request.query_params.get('round')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not round or not start_date or not end_date:
            return Response(
                {"res": "Please provide round, start_date, and end_date"},
                status=status.HTTP_400_BAD_REQUEST
            )

        projects = self.get_projects_by_round(round, start_date, end_date)
        if not projects:
            return Response(
                {"res": "No projects found for the given round and date range"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectByCodeApiView(APIView):
    permission_classes = [HasAPIKey]

    def get_projects_by_code(self, project_code):
        print(f"Received project code: {project_code}")  # Log the received project code

        try:
            projects = Project.objects.filter(ProjectCode__iexact=project_code.strip()).values(
                'ProjectCode', 'ProjectTitle', 'ProjectDescription', 'ProposalLink', 'Round', 'ContractStatus', 'TotalAmount', 'TotalDisbursed', 'TotalNumberOfMilestones', 'NumberOfDoneMilestones', 'DateOfLastUpdate'
            )
            print(f"Projects found: {projects}")  # Log the found projects
            return projects
        except Project.DoesNotExist:
            return None

    def get(self, request, project_code, *args, **kwargs):
        '''
        Retrieves the Project for the given project code
        '''
        if not project_code:
            return Response(
                {"res": "Please provide a project code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        projects = self.get_projects_by_code(project_code)
        if not projects:
            return Response(
                {"res": "No projects found with the specified project code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
