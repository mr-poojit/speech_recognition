# Import the speech_recognition module and alias it as 'sr'
import speech_recognition as sr

# Create a Recognizer object which will help in recognizing speech
r = sr.Recognizer()

# Create a Microphone object which will be used as the audio source
m = sr.Microphone()

# Start a try-except block to catch any exceptions (like KeyboardInterrupt)
try:
    # Print a message indicating the start of ambient noise adjustment
    print("A moment of silence, please...")

    # Open the microphone and adjust for ambient noise levels
    with m as source:
        r.adjust_for_ambient_noise(source)
    
    # Print the set energy threshold that filters out background noise
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    # Enter an infinite loop to continuously listen for speech
    while True:
        # Prompt the user to say something
        print("Say something!")

        # Listen for speech input from the microphone
        with m as source:
            audio = r.listen(source)
        
        # Acknowledge that audio has been captured
        print("Got it! Now to recognize it...")

        # Try to recognize the captured speech using Google’s speech recognition
        try:
            # Convert the speech in 'audio' to text
            value = r.recognize_google(audio)

            # Print the recognized text
            print("You said {}".format(value))

            # Check if the recognized text is "close" to break the loop and exit
            if value.lower() == "close":
                print("Closing the program...")
                break

        # Handle the exception if speech is unintelligible
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        
        # Handle the exception if there's an issue with the Google Speech Recognition API request
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

# Handle a keyboard interrupt to exit gracefully
except KeyboardInterrupt:
    pass
