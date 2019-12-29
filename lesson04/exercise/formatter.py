from flask import Flask
from flask import request
from lib.tracing import init_tracer
from opentracing.ext import tags
from opentracing.propagation import Format

app = Flask(__name__)
tracer = init_tracer('formatter')


@app.route("/format")
def format():
    # extract from carrier of clients
    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    # span tags
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_active_span('format', child_of=span_ctx, tags=span_tags) as scope:
        # get baggage
        greeting = scope.span.get_baggage_item('greeting')
        if not greeting:
            greeting = 'Hello'
        hello_to = request.args.get('helloTo')
        return '%s, %s!' % (greeting, hello_to)


if __name__ == "__main__":
    app.run(port=8081)

