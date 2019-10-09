#converse
def fahr_to_celsius(temp_farenheit):
    """
    The function use the value of temp_farenheit=</int>
    after that, it makes a operation to conver and give us
    the result </float>.
    """
    converted_temp=((temp_farenheit-32)/1.8)
    return converted_temp

#clasificator
def temp_classifier(temp_celsius):
    if(temp_celsius<-2):
        return 0
    if(temp_celsius>=-2 and temp_celsius< 2):
        return 1
    if(temp_celsius>=2 and temp_celsius< 15):
        return 2
    if(temp_celsius>=15):
        return 3
