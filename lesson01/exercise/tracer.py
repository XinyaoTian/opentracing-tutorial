import opentracing

tracer = opentracing.tracer


# def say_hello(hello_to):
#     span = tracer.start_span('say-hello')
#     hello_str = 'Hello, %s!' % hello_to
#     print(hello_str)
#     span.finish()


# However, calling finish() manually is a bit tedious,
# we can use span as a context manager instead


# optimized function
def say_hello(hello_to):
    with tracer.start_span('say-hello') as span:
        hello_str = 'Hello, %s!' % hello_to
        print(hello_str)



