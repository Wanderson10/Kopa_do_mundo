
from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict

class TeamView(APIView):
    def post(self,request):
     team_data = request.data
    
     team = Team.objects.create(
        name=team_data['name'],
        titles = team_data['titles'],
        top_scorer= team_data['top_scorer'],
        fifa_code= team_data['fifa_code'],
        founded_at= team_data['founded_at']
     )
     return Response(model_to_dict(team), 201)


    def get(self,request):
        team =Team.objects.all()
        team_dic = []
        for team_convert in  team:
            t = model_to_dict(team_convert)
            team_dic.append(t)

      
        
        return Response(team_dic)

    
    
   


class TeamIdViews(APIView):
        def get(self, request, team_id):
         try:
          team = Team.objects.get(pk=team_id)
         except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)
        
         team_to_dict = model_to_dict(team)

         return Response(team_to_dict)

        def patch(self,request,team_id):
          try:
           team = Team.objects.get(pk=team_id)
        
          except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)
        
          for key, value in request.data.items():
                setattr(team,key,value)
        
          team.save()
        
          team_to_dict = model_to_dict(team)

          return Response(team_to_dict,200)
        def delete(self,request,team_id):
          try:
            team = Team.objects.get(pk=team_id)
        
          except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)
          team.delete()

          return Response(status = 204)
 




