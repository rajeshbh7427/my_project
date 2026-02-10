from googleapiclient.discovery import build

API_KEY = "AIzaSyDQZca7mcB57S3ahAQ86sbiaDxLPRjG2vM"  

def get_youtube_songs(emotion, language):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    query = f"{language} {emotion} songs"

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        videoCategoryId="10",
        maxResults=5
    )

    response = request.execute()

    songs = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        url = f"https://music.youtube.com/watch?v={video_id}"
        songs.append({"title": title, "url": url})

    return songs
