import sys
import time
from exercise.tracer_jeager import init_tracer


def say_hello(hello_to):
    hello_str = 'Hello, %s!' % hello_to
    print(hello_str)


assert len(sys.argv) == 2

hello_to = sys.argv[1]
say_hello(hello_to)

tracer = init_tracer('hello_world')

# yield to IOLoop to flush the spans
time.sleep(2)
tracer.close()


