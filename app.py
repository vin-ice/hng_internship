#!/usr/bin/python3
""""""
from flask import Flask, request, make_response, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/api', methods=['GET'], strict_slashes=False)
def api():
    """endpoint"""
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name and track:
        ts = datetime.utcnow()
        record = {
            'slack_name': slack_name,
            'current_day': ts.strftime('%A'),
            'utc_time': ts.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'track': track,
            'github_file_url': 'https://github.com/vin-ice/hng_internship/blob/master/0x01-stage_one/app.py',
            'github_repo_url': 'https://github.com/vin-ice/hng_internship',
            'status_code': "200"
        }
        return make_response(jsonify(record), 200)

    return make_response({'message': 'Requires arguments "slack_name" and "track"'}, 404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', threaded=True)
