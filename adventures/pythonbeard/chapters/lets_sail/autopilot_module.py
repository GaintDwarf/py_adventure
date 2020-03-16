from adventures.pythonbeard.common.location import Location, LocationTypes

# To avoid "magic numbers" in our code we can define constants which we will
# able to use in multiple other places.
# Commands:
Command = int
SAIL_FAST = 0
SAIL_SLOW = 1
STOP = 2

# A function which is already written...
def sail_at(current_location: Location) -> str:
    """
    sail_at a sertain location
    
    :param current_location: the location in which we need to sail
    :type current_location: Location
    :return: a string of what command pythonbeard should say
    :rtype: str
    """
    commamd = get_command(current_location.type)
    if commamd == SAIL_FAST:
        return "Fast"
    elif commamd == SAIL_SLOW:
        return "Slow down"
    elif commamd == STOP:
        return "Whales"
    else:
        return "I have no clue"


def get_command(location_type: int) -> Command:
    """
    Receive a location_type when:
        0 = open sea
        1 = shalow water
        2 = whale spot
    
    This function will return the current command which matches the type.
    
    SAIL_FAST  for an open sea terrain
    SAIL_SLOW  for a shallow water
    STOP       for a wale spot

    :param location_type: the location type 
    """
    # Your code here:
    pass
