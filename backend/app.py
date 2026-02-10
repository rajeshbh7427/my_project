from flask import Flask, render_template, request, jsonify
from emotion_detector import detect_emotion
from youtube_recommender import get_youtube_songs

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    language = request.json.get("language", "English")
    emotion = detect_emotion()
    songs = get_youtube_songs(emotion, language)

    return jsonify({
        "emotion": emotion,
        "songs": songs
    })

if __name__ == "__main__":
    app.run(debug=True)
