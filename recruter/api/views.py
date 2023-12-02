from rest_framework.decorators import api_view
from rest_framework.response import Response
from recruter.models import Job,Candidature
from .serializers import JobSerializer,JobSerializers
from recruter.api import serializers
from rest_framework import status
from django.http import JsonResponse




@api_view(['GET'])
def getJobs(request):
    room = Job.objects.all()
    serializer = JobSerializer(room, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def getJob(request, pk):
    room = Job.objects.get(id_job=pk)
    if request.method == 'GET':
        serializer = JobSerializer(room, many=False)
        data = {
            'data': serializer.data,
            'status':status.HTTP_200_OK
        }
        return Response(data)
    elif request.method == 'PUT':
        serializer = JobSerializers(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_201_CREATED})
        return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

    elif request.method == 'DELETE':
        room.delete()
        return Response({"status":status.HTTP_204_NO_CONTENT})

@api_view(['POST'])
def sendJob(request):
        serializer = JobSerializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_201_CREATED})
        return Response({"error":serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

@api_view(['POST'])
def accept_candidature(request):
    if request.method == 'POST':
        id_candidature = request.POST.get('id_candidature')

        try:
            candidature = Candidature.objects.get(id_candidature=id_candidature)
            candidature.status = 'Accepted'
            candidature.save()


            res = {
                'status': 200,
                'message': 'Candidate accepted successfully'
            }
            return JsonResponse(res)
        except Candidature.DoesNotExist:
            res = {
                'status': 500,
                'message': 'Candidature does not exist'
            }
            return JsonResponse(res)
        except Exception as e:
            res = {
                'status': 500,
                'message': str(e)
            }
            return JsonResponse(res)
    else:
        res = {
            'status': 500,
            'message': 'Invalid request method'
        }
        return JsonResponse(res)

@api_view(['POST'])
def reject_candidature(request):
    if request.method == 'POST':
        id_candidature = request.POST.get('id_candidature')

        try:
            candidature = Candidature.objects.get(id_candidature=id_candidature)
            candidature.status = 'Rejected'
            candidature.save()


            res = {
                'status': 200,
                'message': 'Candidate rejected successfully'
            }
            return JsonResponse(res)
        except Candidature.DoesNotExist:
            res = {
                'status': 500,
                'message': 'Candidature does not exist'
            }
            return JsonResponse(res)
        except Exception as e:
            res = {
                'status': 500,
                'message': str(e)
            }
            return JsonResponse(res)
    else:
        res = {
            'status': 500,
            'message': 'Invalid request method'
        }
        return JsonResponse(res)