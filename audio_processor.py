import sounddevice as sd
import numpy as np

stream = None
GAIN = 10.0
POST_GAIN = 1.8

def list_devices():
    devices = sd.query_devices()
    return {
        "inputs": [d["name"] for d in devices if d["max_input_channels"] > 0],
        "outputs": [d["name"] for d in devices if d["max_output_channels"] > 0]
    }

def set_gain_values(gain, post_gain):
    global GAIN, POST_GAIN
    GAIN = gain
    POST_GAIN = post_gain

def apply_gain(signal):
    boosted = signal * GAIN
    compressed = np.tanh(boosted)
    return np.clip(compressed * POST_GAIN, -1.0, 1.0)

def callback(indata, outdata, frames, time, status):
    if status:
        print(f"[!] {status}")
    outdata[:] = apply_gain(indata)

def start_stream(config):
    global stream
    try:
        if stream:
            return {"status": "already_running"}

        input_index = sd.query_devices(config["input"], "input")["index"]
        output_index = sd.query_devices(config["output"], "output")["index"]

        stream = sd.Stream(
            device=(input_index, output_index),
            samplerate=44100,
            blocksize=256,
            channels=1,
            dtype="float32",
            latency="low",
            callback=callback
        )
        stream.start()
        return {"status": "running"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def stop_stream():
    global stream
    if stream:
        stream.stop()
        stream.close()
        stream = None
