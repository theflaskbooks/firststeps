#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python quickstart.py
"""

from google.cloud import texttospeech
import os
import yaml
import random

# Instantiates a client
client = texttospeech.TextToSpeechClient()

def run_tts(text, gender="neutral"):
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    
    name="en-US-Wavenet-D" # default voice

    if gender=="male":
        ssml_gender = texttospeech.SsmlVoiceGender.MALE
        pitch = -5.6
    elif gender=="female":
        ssml_gender = texttospeech.SsmlVoiceGender.FEMALE
        name="en-US-Wavenet-E"
        pitch = 0.0
    else:
        ssml_gender = texttospeech.SsmlVoiceGender.NEUTRAL

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=ssml_gender,
        name = name
    )

    # Select the type of audio file you want returned

    audio_config = texttospeech.AudioConfig(
        audio_encoding = texttospeech.AudioEncoding.MP3,
        speaking_rate = 0.76,
        pitch = pitch,
        volume_gain_db = 6.0
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response

if __name__ == "__main__":

    filename = input("Please provide the file name : ")

    with open(filename + ".yaml") as f:
        os.mkdir(filename)

        animals = yaml.safe_load(f)

        for slide in animals:

            # os.mkdir(filename + "/" + slide)
            # get the list of text for the slide
            texts = animals[slide]

            # randomly select the speaking voice

            for text in texts:
                try:
                    voice = random.choice(["male", "female"])
                    response = run_tts(text, voice)
                    # The response's audio_content is binary.
                    with open(filename + "/" + voice +"_output_" + text[:25] +".mp3", "wb") as out:
                        # Write the response to the output file.
                        out.write(response.audio_content)
            

                except Exception as e:
                    print(e)
                    continue

            print('Audio content written for  ' + slide)
