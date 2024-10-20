from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from django.db.models import Q

class ProjectApiView(APIView):
    def get_object(self, round,start_date,end_date):
        '''
        Helper method to get the projects with the given round
        '''
        try:
            return Project.objects.filter(Round=round,DateOfLastUpdate__range=[start_date, end_date])
        except Project.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, round, *args, **kwargs):
        '''
        Retrieves the Projects for the given round within the specified date range
        '''
        # Get start_date and end_date from query parameters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        round_instance = self.get_object(round,start_date, end_date)
        if not round_instance:
            return Response(
                {"res": "Projects with the specified round do not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Set many=True since you are serializing multiple instances
        serializer = ProjectSerializer(round_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
