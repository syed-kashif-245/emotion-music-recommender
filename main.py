import cv2
from deepface import DeepFace
import webbrowser
import random
import collections
import time
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# ------------- 🎵 YOUR PERSONAL PLAYLISTS HERE -------------
emotion_to_youtube = {
    "happy": [
        "https://youtu.be/WxtJqyIyThU?si=2WcpoeabJq8OoCkn"
    ],
    "sad": [
        "https://www.youtube.com/watch?v=jHNNMj5bNQw",
        "https://www.youtube.com/watch?v=284Ov7ysmfA",
    ],
    "angry": [
        "https://youtu.be/v7K4vGYL9zI?si=kuGILEo5-sgL4N21"
    ],
    "surprise": [
        "https://youtu.be/91EzD9VgwGk?si=Naqj5NHd9-_S173P"
    ],
    "fear": [],
    "disgust": [],
    "neutral": [
        "https://www.youtube.com/watch?v=my-chill-song-1"
    ]
}
# -----------------------------------------------------------


def detect_emotion(frames=10, show_preview=True):
    """
    Capture `frames` images from the webcam, predict emotion on each,
    and return the majority vote. Optionally show a live preview window.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open webcam.")
        return None

    votes = []

    print(f"Capturing {frames} frames… Look at the camera 😊")
    time.sleep(1)

    for i in range(frames):
        time.sleep(0.3)
        ret, frame = cap.read()
        if not ret:
            continue

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False, detector_backend='opencv')[0]

            emotion = result['dominant_emotion']
            votes.append(emotion)

            if i == 0:
                print("\nRaw probabilities for first frame:")
                for k, v in result['emotion'].items():
                    print(f"  {k:<8}: {v:5.1f}%")

            if show_preview:
                disp = frame.copy()
                cv2.putText(
                    disp, f"{emotion}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 0), 2, cv2.LINE_AA
                )
                cv2.imshow("Detecting emotion – press q to skip", disp)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print("Detection error:", e)

    cap.release()
    cv2.destroyAllWindows()

    if not votes:
        print("No frames captured.")
        return None

    majority = collections.Counter(votes).most_common(1)[0][0]
    print(f"\n🧠 Majority‑voted emotion: {majority}")
    return majority


def play_music(emotion):
    """
    Opens a random YouTube song that the user configured for `emotion`.
    """
    playlist = emotion_to_youtube.get(emotion.lower(), [])
    if not playlist:
        print(f"⚠️  No songs configured for emotion '{emotion}'.")
        return

    url = random.choice(playlist)
    print(f"🎧 Opening: {url}")
    webbrowser.open(url)


if __name__ == "__main__":
    mood = detect_emotion(frames=10, show_preview=True)
    if mood:
        play_music(mood)
