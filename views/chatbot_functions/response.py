import random
import time
def response_generator(prompt):
    response = prompt
    for word in response.split():
        yield word + " "
        time.sleep(0.05)