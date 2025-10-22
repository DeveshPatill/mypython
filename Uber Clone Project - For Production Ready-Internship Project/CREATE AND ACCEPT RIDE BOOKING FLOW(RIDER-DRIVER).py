# Write your Python code here
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Ride
from .serializers import RideRequestSerializer
from driver.models import Driver

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_ride(request):
    # Check if user is a Rider
    # Save ride with rider and status = REQUESTED
    if hasattr(request.user,"driver"):
        return Response({"detail":" Drivers cannot request rides."}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = RideRequestSerializer(data=request.data)
    if serializer.is_valid():
        ride = serializer.save(rider = request.user, status=Ride.Status.REQUESTED)
        return Response(RideRequestSerializer(ride).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_rides(request):
    # Check if user is a Driver
    # Return rides with status = REQUESTED and no driver assigned
    try:
        driver = request.user.driver
    except Driver.DoesNotExist:
        return Response({"detail":"Only drivers can view available rides."}, status=status.HTTP_403_FORBIDDEN)

    rides = Ride.objects.filter(status = Ride.Status.REQUESTED, driver__isnull=True)
    serializer = RideRequestSerializer(rides, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_ride(request, ride_id):
    # Check if user is a Driver
    # Assign ride if not already taken
    try:
        driver = request.user.driver
    except Driver.DoesNotExist:
        return Response({"detail":"only drivers can accept rides."},status=status.HTTP_403_FORBIDDEN)
    
    with transaction.atomic():
        ride = get_object_or_404(Ride.objects.select_for_update(), pk=ride_id)

        if ride.status != Ride.Status.REQUESTED or ride.driver is not None:
            return Response({"detail":"Ride already accepted."}, status=status.HTTP_400_BAD_REQUEST)

        ride.driver = driver.user
        ride.status = Ride.Status.ONGOING
        ride.save()
    return Response(RideRequestSerializer(ride).data, status=status.HTTP_200_OK)