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
import cv2 # type: ignore
import json
import tempfile
import numpy as np # type: ignore
import face_recognition # type: ignore
from moviepy.editor import VideoFileClip # type: ignore
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["XDG_RUNTIME_DIR"] = "/tmp"

gpt = _.GPT()

def extract_audio_from_video(video_path, audio_output):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_output, logger=None)

def transcribe_segments(audio_path):
    import openai
    with open(audio_path, "rb") as f:
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=f,
            response_format="verbose_json",
            timestamp_granularities=["segment"],
        )
    return transcript["segments"]

# ---------- NO MEDIAPIPE: pure OpenCV + face_recognition ----------

def analyze_video_by_segment(video_path, segments):
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    results = []

    for seg in segments:
        start_f = int(seg["start"] * fps)
        end_f = int(seg["end"] * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_f)

        faces_seen = 0
        motion_score = 0
        prev_gray = None
        total_frames = max(end_f - start_f, 1)

        for _ in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                break

            small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            if len(faces) > 0:
                faces_seen += 1

            if prev_gray is not None:
                diff = cv2.absdiff(prev_gray, gray)
                motion_score += np.sum(diff) / 255
            prev_gray = gray

        expression_freq = faces_seen / total_frames
        motion_freq = min(motion_score / (total_frames * 1000), 1.0)

        results.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"],
            "expression_count": faces_seen,
            "motion_count": motion_score,
            "frames": total_frames,
            "expression_freq": expression_freq,
            "motion_freq": motion_freq
        })

    cap.release()
    return results

# -----------------------------------------------------------------

def synthesize_profile(segments):
    full = []
    for s in segments:
        prompt = f"""Social media video segment:

Text: "{s['text']}"
Facial expressions detected in {s['expression_count']} of {s['frames']} frames.
Motion score (0-1): {s['motion_freq']:.2f}

Profile this psychologically and physically.
Return JSON with keys: text, emotion, psychological_inference,
engagement, confidence_level, movement_intensity,
expression_freq, motion_freq.
"""
        reply = gpt.prompt(prompt, code=True)
        parsed = json.loads(reply[0]) if reply else {"error": "parse"}
        parsed.update({"start": s["start"], "end": s["end"]})
        full.append(parsed)
    return full

def normalize_segments(segments):
    for s in segments:
        try:
            s["expression_freq"] = float(s["expression_freq"])
        except:
            s["expression_freq"] = 0.0
        try:
            s["motion_freq"] = float(s["motion_freq"])
        except:
            s["motion_freq"] = 0.0
        s["expression_freq"] = round(s["expression_freq"], 4)
        s["motion_freq"] = round(s["motion_freq"], 4)
    return segments

def build_final_profile(segments):
    segments2 = normalize_segments(segments)
    try:
        avg_expr = sum(s["expression_freq"] for s in segments2) / len(segments)
    except:
        avg_expr = '-'
    try:
        avg_mot = sum(s["motion_freq"] for s in segments2) / len(segments)
    except:
        avg_mot = '-'
    return {
        "duration": round(segments[-1]["end"], 2),
        "platform": "Unspecified",
        "topic": "Analyzed Video",
        "visual_profile": {
            "avg_expression_freq": avg_expr,
            "avg_motion_freq": avg_mot,
        },
        "segments": segments,
    }

def process_video(video_path):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as audio:
        extract_audio_from_video(video_path, audio.name)
        segments  = transcribe_segments(audio.name)
        enriched  = analyze_video_by_segment(video_path, segments)
        profiles  = synthesize_profile(enriched)
        return build_final_profile(profiles)






def action():
    # print(_.isData())
    for path in _.isData():
        print(f"Processing video: {path}")
        # === RUN ===
        profile = process_video(path)

        try:
            data = json.dump(profile, indent=4)
        except:
            data = str(profile)

        # Save to JSON
        with open(path+'.json', "w", encoding="utf-8") as f:
            f.write(data)
        _.pr(path+'.json',c='cyan')

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)