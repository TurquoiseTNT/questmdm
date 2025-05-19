from flask import Blueprint, render_template, request, jsonify
from .adb_manager import connect_device, list_devices

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    devices = list_devices()
    return render_template('index.html', devices=devices)

@bp.route('/connect', methods=['POST'])
def connect():
    serial = request.form.get('serial')
    ip = request.form.get('ip')
    result = connect_device(serial, ip)
    return jsonify({"result": result})
