from flask import Flask, abort, request
import whisper
# from tempfile import NamedTemporaryFile
# from gevent import pywsgi

# Load the Whisper model:
model = whisper.load_model('large')

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def handler():
    app.logger.info("Received a request.")

    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)

    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        # temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(r'.\whisper')
        # Let's get the transcript of the temporary file.
        result = model.transcribe(r'.\whisper')


        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    # This will be automatically converted to JSON.
    return {'results': results}
# server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
# server.serve_forever()



# from flask import Flask, abort, request
# from tempfile import NamedTemporaryFile
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET'])
# def handler():
#     if not request.files:
#         # If the user didn't submit any files, return a 400 (Bad Request) error.
#         abort(400)
#
#     # For each file, let's store the results in a list of dictionaries.
#     results = []
#
#     # Loop over every file that the user submitted.
#     for filename, handle in request.files.items():
#         # Create a temporary file.
#         # The location of the temporary file is available in `temp.name`.
#         temp = NamedTemporaryFile()
#         # Write the user's uploaded file to the temporary file.
#         # The file will get deleted when it drops out of scope.
#         handle.save(temp)
#         # Now we can store the result object for this file.
#         results.append({
#             'filename': filename,
#             'transcript': 'Coming soon!',
#         })
#
#     # This will be automatically converted to JSON.
#     return {'results': results}