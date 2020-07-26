from rest_framework import serializers
from student import models




class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields  = ('id','password','url','first_name','last_name','email','dob','city','state','institute','department','upload_id','enrollment_no','contact_no','is_redressal','category')
        extra_kwargs = {
            'password':{
            'write_only':True,
            'style':{'input_type':'password'},
            },
            'is_redressal':
            {
            'read_only':True,
            },
        }

    def create(self,validated_data):
        '''Create and Return a new user'''
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
            dob=validated_data['dob'],
            city = validated_data['city'],
            state = validated_data['state'],
            institute = validated_data['institute'],
            department = validated_data['department'],
            upload_id = validated_data['upload_id'],
            enrollment_no = validated_data['enrollment_no'],
            contact_no = validated_data['contact_no'],
            category = validated_data['category'],
        )

        return user

class ComplaintSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes profile complaint item"""
    
    class Meta:
        model = models.Complaint
        fields = ('id','user_profile','url','category','sub_category','subject','complaint_text','upload_file','status','in_progress','finished','institute_name')
        # key = {'read_only':True} if not model.user_profile.is_redressal
        extra_kwargs = {'user_profile':{'read_only':True},
                         'institute_name':{'read_only':True},          
                       }       
        #                 'status':key,
        #                 'in_progress':key,
        #                 'finished':key,
        #                 }
        #if not model.user_profile.is_redressal:
         #    read_only_fields = ['status','in_progress','finished']
