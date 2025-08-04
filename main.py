from flask import Flask, send_from_directory, jsonify, request
from flask_socketio import SocketIO, emit
from audio_processor import start_stream, stop_stream, list_devices, set_gain_values
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder="static", static_url_path="")
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route("/mic-amp")
def mic_amp():
    return send_from_directory("static/mic_amp", "index.html")

@socketio.on("get_devices")
def handle_get_devices():
    emit("devices", list_devices())

@socketio.on("start_stream")
def handle_start_stream(data):
    try:
        result = start_stream(data)
        emit("stream_status", result)
    except Exception as e:
        emit("stream_status", {"status": "error", "message": str(e)})

@socketio.on("stop_stream")
def handle_stop_stream():
    try:
        stop_stream()
        emit("stream_status", {"status": "stopped"})
    except Exception as e:
        emit("stream_status", {"status": "error", "message": str(e)})

@socketio.on("set_gain")
def handle_set_gain(data):
    try:
        set_gain_values(data["gain"], data["post_gain"])
        emit("gain_updated", {"status": "gain_updated"})
    except Exception as e:
        emit("gain_updated", {"status": "error", "message": str(e)})

@socketio.on("connect")
def handle_connect():
    print("Client connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")
    try:
        stop_stream()
    except:
        pass

if __name__ == "__main__":
    import logging

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 3030))
    debug = os.environ.get('DEBUG', 'false').lower() == 'true'

    print(f"Starting Mic Amp server on {host}:{port}")
    print(f"Debug mode: {debug}")
    print(f"Access the application at: http://localhost:{port}/mic-amp")

    try:
        socketio.run(
            app,
            debug=debug,
            host=host,
            port=port,
            allow_unsafe_werkzeug=True
        )
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    except Exception as e:
        print(f"Error starting server: {e}")
        exit(1)