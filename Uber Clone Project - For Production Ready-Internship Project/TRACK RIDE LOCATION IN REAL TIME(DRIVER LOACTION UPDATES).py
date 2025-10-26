# Write your Python code here
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ride.models import Ride
from driver.models import Driver
from rider.models import Rider

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_driver_location(request):
    # Check if request.user is a driver
    # Update driver's latitude and longitude from request.data
    try:
        driver = Driver.objects.get(user=request.user)
    except Driver.DoesNotExist:
        return Response({"error":"Only drivers can update location"}, status=status.HTTP_403_FORBIDDEN)

    latitude = request.data.get("latitude")
    longitude = request.data.get("longitude")

    if latitude is None or longitude is None:
        return Response({"error":"Latitude and Longitude are required"}, status=status.HTTP_400_BAD_REQUEST)

    driver.current_latitude = latitude
    driver.current_longitude = longitude
    driver.save()
    return Response({"message":"Location updated succesfully"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def track_ride_location(request, ride_id):
    # Get ride object
    # Check if request.user is the associated rider
    # Return driver’s current location if ride is ONGOING
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error":"Ride not Found."}, status=status.HTTP_404_NOT_FOUND)
    
    if ride.status != "ONGOING":
        return Response({"error":"Location tracking is only available for ongoing rides."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        rider = Rider.objects.get(user=request.user)
    except Rider.DoesNotExist:
        return Response({"error":"Only riders can track rides."}, status=status.HTTP_403_FORBIDDEN)
    
    if ride.rider != rider:
        return Response({"error":"Your are not authorized to track this ride."}, status=status.HTTP_403_FORBIDDEN)

    driver = ride.driver

    return Response({
        "driver_latitude":driver.current_latitude,
        "driver_longitude":driver.driver_longitude
    },status=status.HTTP_200_OK)