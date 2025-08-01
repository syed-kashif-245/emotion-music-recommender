# emotion_mapper.py

def get_playlist(emotion):
    emotion = emotion.lower()

    playlist_map = {
        "happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs&list=PLhInz4M-OzR38LVEvJvTu_Uu8u9whcPLb",
        "sad": "https://www.youtube.com/watch?v=6zXDo4dL7SU&list=PLhInz4M-OzR0vMZwSxJ_PxMjae0Id_ApK",
        "angry": "https://www.youtube.com/watch?v=btPJPFnesV4&list=PLhInz4M-OzR2we3zBk4Pqg_9BphS_n68r",
        "neutral": "https://www.youtube.com/watch?v=5qap5aO4i9A&list=PLhInz4M-OzR1q9Pf3UDBcXQvOpJtqzCOy"
    }

    return playlist_map.get(emotion, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # fallback link