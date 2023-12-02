from rest_framework.serializers import ModelSerializer
from recruter.models import Job


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobSerializers(ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'job_title',
            'job_salaire',
            'domain',
            'formationreq',
            'expreq',
            'skillreq',
            'job_description',
            'recruter'
        )