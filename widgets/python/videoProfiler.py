import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


import os
import cv2
import json
import tempfile
from moviepy.editor import VideoFileClip
import mediapipe as mp
from library.ai.gpt import  GPT

gpt = GPT()

def extract_audio_from_video(video_path, audio_output):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_output, logger=None)

def transcribe_segments(audio_path):
    import openai
    with open(audio_path, 'rb') as f:
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=f,
            response_format="verbose_json",
            timestamp_granularities=["segment"]
        )
    return transcript['segments']  # list of dicts with start, end, text

def analyze_video_by_segment(video_path, segments):
    import face_recognition
    import numpy as np

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    results = []

    for seg in segments:
        start_frame = int(seg['start'] * fps)
        end_frame = int(seg['end'] * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        face_count = 0
        motion_score = 0
        prev_frame = None
        total_frames = end_frame - start_frame

        for _ in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # Expression (face) detection
            faces = face_recognition.face_locations(rgb)
            if faces:
                face_count += 1

            # Motion (frame delta)
            gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
            if prev_frame is not None:
                frame_diff = cv2.absdiff(prev_frame, gray)
                score = np.sum(frame_diff) / 255
                motion_score += score
            prev_frame = gray

        expression_freq = face_count / total_frames if total_frames else 0
        motion_freq = min(motion_score / (total_frames * 1000), 1.0)

        results.append({
            "start": seg['start'],
            "end": seg['end'],
            "text": seg['text'],
            "expression_count": face_count,
            "motion_count": motion_score,
            "frames": total_frames,
            "expression_freq": expression_freq,
            "motion_freq": motion_freq
        })

    cap.release()
    return results


def synthesize_profile(segments):
    full = []
    for s in segments:
        prompt = f"""Social media video segment:

Text: "{s['text']}"
Facial expressions detected in {s['expression_count']} of {s['frames']} frames.
Body movements detected in {s['motion_count']} of {s['frames']} frames.

Profile this psychologically and physically.
Output JSON like this:

{{
  "text": "...",
  "emotion": "...",
  "psychological_inference": "...",
  "engagement": "...",
  "confidence_level": 0.0-1.0,
  "movement_intensity": "low|moderate|high",
  "expression_freq": float (0.0–1.0),
  "motion_freq": float (0.0–1.0)
}}
"""
        result = gpt.prompt(prompt, code=True)
        parsed = json.loads(result[0]) if result else {"error": "Parsing failed", "segment": s}
        parsed["start"] = s['start']
        parsed["end"] = s['end']
        full.append(parsed)
    return full

def build_final_profile(segments):
    avg_expr = sum(s["expression_freq"] for s in segments) / len(segments)
    avg_mot = sum(s["motion_freq"] for s in segments) / len(segments)
    return {
        "duration": round(segments[-1]['end'], 2),
        "platform": "Unspecified",
        "topic": "Analyzed Video",
        "visual_profile": {
            "avg_expression_freq": avg_expr,
            "avg_motion_freq": avg_mot,
        },
        "segments": segments
    }

def process_video(video_path):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as audio_file:
        extract_audio_from_video(video_path, audio_file.name)
        segments = transcribe_segments(audio_file.name)
        enriched = analyze_video_by_segment(video_path, segments)

        for s in enriched:
            s["expression_freq"] = s.get("expression_freq", 0)
            s["motion_freq"] = s.get("motion_freq", 0)


        profiled_segments = synthesize_profile(enriched)
        return build_final_profile(profiled_segments)






def action():
    for path in _.isData():
        # === RUN ===
        profile = process_video(path)

        # Save to JSON
        with open(path+'.json', "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=4)
        _.pr(path+'.json',c='cyan')

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)