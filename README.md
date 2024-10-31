

# Jarvis Voice Assistant

This Python script is a simple text-to-speech voice assistant that uses the `edge_tts` library for voice synthesis and `playsound` for audio playback. It can convert text to spoken audio using the specified voice, defaulting to the **Indian English voice (Neerja)**.

## Features

- **Text-to-Speech**: Converts input text to speech with adjustable voices.
- **Audio Playback**: Plays the generated speech in real-time.
- **Multithreading**: Uses threading for non-blocking audio playback.

## Requirements

Before running the script, make sure you have the following libraries installed:

```bash
pip install edge-tts playsound
```
## Usage

Import and initialize the function `speak()` with text and an optional voice parameter.

Run the Script: Execute the script to hear the default text output or change the input text to customize it.
```
speak("hello sir, I am Jarvis")

speak("how can I help you today?")
```

## Voice Customization

You can adjust the voice by passing a different voice argument to the `speak() function.` The default is "en-IN-NeerjaNeural", but you can replace it with any supported voice from edge-tts.
## Example Code

```
Example Usage

speak("hello sir, I am Jarvis", "en-US-JennyNeural")
```

## Notes

- **Temp Files**: Temporary audio files are created for playback and deleted after use.
- **Error Handling**: Catches and displays exceptions for easy debugging.

## Contributing

If you have suggestions or improvements, feel free to create an issue or submit a pull request.

## FAQ

#### Question 1. What do I need to run this script?

Answer: To run this script, you need Python installed, along with the edge-tts and playsound libraries. You can install them using:

```pip install edge-tts playsound```

#### Question 2. How can I change the voice in the speak function?

Answer: You can change the voice by passing a different voice parameter to the `speak()` function.

 For example:

```speak("Hello, this is a test.", "en-US-JennyNeural")```

To see a list of available voices, refer to the edge-tts documentation.

#### Question 3. I’m getting an error when trying to play the sound. What can I do?

Answer: Make sure that playsound is installed correctly and that your system has audio playback capabilities. If you're still having trouble, check that your Python environment supports audio output or try running the script with administrator privileges.

#### Question 4. Can I use this script on non-Windows systems?

Answer: Yes, this script can run on any operating system that supports Python and the required libraries. However, playsound may have limitations on some platforms. You may need to use a different library like pygame if playsound is not compatible with your system.

#### Question 5. Why are temporary files created, and how are they managed?

Answer: Temporary `.mp3` files are created to store the generated speech for playback. These files are automatically deleted after use, but you can manually delete them if needed by closing the script and removing them from your temp folder.


## Authors

- [Yash vardhan Namdeo](https://www.github.com/YashVardhan-coder)

