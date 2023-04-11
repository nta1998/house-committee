from .serializers import MyTokenObtainPairSerializer, ProfileSerializer, AdsSerializer, PoolSerializer, PayAdsSerializer, VoteSerializer, ChatSerializer, ProductsSerializer, BuildingSerializer
from .models import Ads, Profile, Pool, Payment_ads, Vote, Chat, Product, Building
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
##############################################################################
# ---register--

    
@api_view(['POST'])
def registerBuilding(request):
    user = User.objects.create_user(
        username=request.data['user']['username'],
        email=request.data["user"]['email'],
        password=request.data["user"]['password']
    )
    user.is_active = True
    user.is_staff = True
    user.save()

    serializer = BuildingSerializer(data=request.data["building"], context={'user': request.user})
    if serializer.is_valid(): 
        serializer.save()
        request.data["profile"]["building_id"] = Building.objects.get(full_address = request.data["building"]["full_address"]).id
        request.data["profile"]["is_committee"] = True 
        serializer = ProfileSerializer(data=request.data["profile"], context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
        username=request.data['user']['username'],
        email=request.data["user"]['email'],
        password=request.data["user"]['password']
    )
    user.is_active = True
    user.is_staff = True
    user.save()
    serializer = ProfileSerializer(
        data=request.data["profile"], context={'user': user})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ---login--


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# ---full crud for login users--


@permission_classes([IsAuthenticated])
class allprofileView(APIView):
    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        my_model = Profile.objects.all()
        serializer = ProfileSerializer(my_model, many=True)
        for profile in serializer.data:
            profile["building_id"] = {
                "id": Profile.objects.get(id=profile["id"]).building_id.id,
                "full_address": Profile.objects.get(id=profile["id"]).building_id.full_address,
                "floors": Profile.objects.get(id=profile["id"]).building_id.floors,
                "vote_active": Profile.objects.get(id=profile["id"]).building_id.vote_active,
                "committee_name": Profile.objects.get(id=profile["id"]).building_id.committee_name,
                "committee_apartment": Profile.objects.get(id=profile["id"]).building_id.committee_apartment,
                "committee_phone": Profile.objects.get(id=profile["id"]).building_id.committee_phone,
                "payment_date": Profile.objects.get(id=profile["id"]).building_id.payment_date,
                "committee_monthly": Profile.objects.get(id=profile["id"]).building_id.committee_monthly}
            profile["user"] = Profile.objects.get(
                id=profile["id"]).user.email
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class BuildingView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request, id):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Building.objects.filter(id=id)
        serializer = BuildingSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = BuildingSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """
        parser_class = (MultiPartParser, FormParser)
        my_model = Building.objects.get(id=id)
        serializer = BuildingSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Building.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class crudView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        user = request.user
        my_model = user.profile_set.all()
        # my_model = Profile.objects.all()
        serializer = ProfileSerializer(my_model, many=True)
        for profile in serializer.data:
            profile["building_id"] = {
                "id": Profile.objects.get(id=profile["id"]).building_id.id,
                "full_address": Profile.objects.get(id=profile["id"]).building_id.full_address,
                "floors": Profile.objects.get(id=profile["id"]).building_id.floors,
                "vote_active": Profile.objects.get(id=profile["id"]).building_id.vote_active,
                "committee_name": Profile.objects.get(id=profile["id"]).building_id.committee_name,
                "committee_apartment": Profile.objects.get(id=profile["id"]).building_id.committee_apartment,
                "committee_phone": Profile.objects.get(id=profile["id"]).building_id.committee_phone,
                "payment_date": Profile.objects.get(id=profile["id"]).building_id.payment_date,
                "committee_monthly": Profile.objects.get(id=profile["id"]).building_id.committee_monthly}
            profile["user"] = Profile.objects.get(
                id=profile["id"]).user.email
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = ProfileSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """
        parser_class = (MultiPartParser, FormParser)
        my_model = Profile.objects.get(id=id)
        serializer = ProfileSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Profile.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class crudAdsView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Ads.objects.all()
        serializer = AdsSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = AdsSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """
        parser_class = (MultiPartParser, FormParser)
        my_model = Ads.objects.get(id=id)
        serializer = AdsSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Ads.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class cruPoolView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Pool.objects.all()
        serializer = PoolSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = PoolSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Pool.objects.get(id=id)
        serializer = PoolSerializer(my_model).data
        for user in list(serializer["answered"]):
            if int(user) == request.data["answered"][-1]:  
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        newAnswered = serializer["answered"]
        newAnswered.append(request.data["answered"][-1])
        my_model = Pool.objects.get(id=id)
        request.data["answered"] = newAnswered
        serializer = PoolSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Pool.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class crudPaymentAdtlView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Payment_ads.objects.all()
        serializer = PayAdsSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = PayAdsSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """
        parser_class = (MultiPartParser, FormParser)
        my_model = Payment_ads.objects.get(id=id)
        serializer = PayAdsSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Payment_ads.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class crudVoteView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Vote.objects.all()
        serializer = VoteSerializer(my_model, many=True)
        for vote in serializer.data:
            vote["profile_id"] = {"full_name": Vote.objects.get(id=vote["id"]).profile_id.full_name,
                                  "profile_pic": Vote.objects.get(id=vote["id"]).profile_id.profile_pic.name,
                                  "id": Vote.objects.get(id=vote["id"]).profile_id.id}
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = VoteSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Vote.objects.get(id=id)
        serializer = VoteSerializer(my_model).data
        for user in list(serializer["answered"]):
            if int(user) == request.data["answered"][-1]:  
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        newAnswered = serializer["answered"]
        newAnswered.append(request.data["answered"][-1])
        request.data["answered"] = newAnswered
        my_model = Vote.objects.get(id=id)
        serializer = VoteSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Vote.objects.get(profile_id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class ChatVoteView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Chat.objects.all()
        serializer = ChatSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = ChatSerializer(
            data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """

        my_model = Chat.objects.get(id=id)
        serializer = ChatSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Chat.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
class ProductsVoteView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """

    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        # user = request.user
        # print(user)
        # my_model = user.profile_set.all()
        my_model = Product.objects.all()
        serializer = ProductsSerializer(my_model, many=True)
        for product in serializer.data:
            product["profile_id"] = {
                "id": Product.objects.get(id=product["id"]).profile_id.id,
                "building_id": Product.objects.get(id=product["id"]).profile_id.building_id.id,
                "full_name": Product.objects.get(id=product["id"]).profile_id.full_name,
                "phone_number": Product.objects.get(id=product["id"]).profile_id.phone_number,
                "profile_pic": Product.objects.get(id=product["id"]).profile_id.profile_pic.name}
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        serializer = ProductsSerializer(
            data=request.data, context={'profile_id': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Handle PUT requests to update an existing Task object
        """

        my_model = Product.objects.get(id=id)
        serializer = ProductsSerializer(my_model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Product.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
