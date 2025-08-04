# Mic Amp

A real-time audio processor with web interface that amplifies and processes microphone input with configurable gain controls.

<img width="831" height="1378" alt="RLLDJnin4BtxLqovj3qa4PJs45KL8Q4G523AKlNGLj6mEzbOsRLNjZSHLFtl7Tkx-G8khD-ycNcU3-V2EZIkBWkua-byK5RpWKcNqb7gQaD2lCje8HN1x6huEBY_dbn1Mg2rGZZf2l9Em4xGWHbXqN6o91ZKcTGmDJebQwNAuIYYMnApS6Cxsg3A6NeFbqPlB9dUi92a74pmcOoeC5rXJd2oZvx0Nm7yz-idFRLkVm1j-nsD" src="https://github.com/user-attachments/assets/45a0e9af-fc74-401d-a514-57a1edf69a57" />


## Features

- **Real-time Audio Processing**: Low-latency audio streaming from input to output devices
- **Gain Control**: Adjustable input and output gain with soft compression
- **Device Selection**: Choose from available audio input and output devices
- **Web Interface**: Clean, easy control
- **WebSocket Communication**: Real-time updates between web interface and audio processor

## Prerequisites

- Python 3.7 or higher
- Audio input device (microphone)
- Audio output device (speakers, headphones, or virtual audio cable)

## Installation

1. **Clone or download the project**

   ```bash
   git clone https://github.com/d-freitas/mic-amp.git
   cd mic-amp
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv .
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

1. **Start the application**

   ```bash
   python3 main.py
   ```

2. **Open your web browser**
   Navigate to `http://localhost:3030`

3. **Configure audio devices**
   - Select your desired **Input Device** (microphone)
   - Select your desired **Output Device** (speakers/headphones)

4. **Adjust audio settings**
   - **Output Gain** (1-20): Controls the final volume sent to the output device
   - **Input Gain** (0.5-5): Controls the microphone volume before processing

## Audio Processing

The application applies the following audio processing chain:

1. **Input Gain**: Amplifies the incoming signal
2. **Soft Compression**: Uses `tanh()` function to prevent harsh clipping
3. **Output Gain**: Final volume adjustment
4. **Hard Limiting**: Clips output to [-1.0, 1.0] range

## Configuration

### Default Settings

- **Sample Rate**: 44,100 Hz
- **Block Size**: 256 samples
- **Channels**: Mono (1 channel)
- **Data Type**: 32-bit float
- **Latency**: Low latency mode
- **Default Output Gain**: 10.0
- **Default Input Gain**: 1.8

### Device Preferences

The application automatically selects devices with these preferences:

- **Input**: Devices containing "H510" in the name (fallback to first available)
- **Output**: Devices containing "BlackHole" in the name (fallback to first available)

## Troubleshooting

### Common Issues

#### No audio devices found

- Ensure your audio drivers are properly installed
- Check that your microphone and speakers are connected
- Try restarting the application

#### High latency or audio dropouts

- Close other audio applications
- Try different block sizes by modifying `blocksize` in `audio_processor.py`
- Ensure your system isn't under heavy CPU load

#### Distorted audio

- Reduce the Input Gain setting
- Lower the Output Gain if the output is clipping
- Check your microphone levels in system settings

#### Connection errors

- Ensure port 3030 is not being used by another application
- Try restarting the application
- Check firewall settings if accessing from another device


### API Endpoints

**WebSocket Events:**

- `get_devices`: Request available audio devices
- `start_stream`: Start audio streaming with specified devices
- `stop_stream`: Stop audio streaming
- `set_gain`: Update gain values in real-time

## Development

To modify the audio processing:

1. Edit `audio_processor.py` for audio processing logic
2. Edit `static/index.html` for UI changes
3. Edit `main.py` for server-side functionality

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Support

For issues or questions, please check the troubleshooting section above or create an issue in the repository.
