function startWebcam() {
    const language = document.getElementById("language").value;

    fetch("/detect", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ language: language })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("emotion").innerText =
            "Detected Emotion: " + data.emotion;

        const list = document.getElementById("songs");
        list.innerHTML = "";

        data.songs.forEach(song => {
            const li = document.createElement("li");
            const a = document.createElement("a");
            a.href = song.url;
            a.target = "_blank";
            a.innerText = song.title;
            li.appendChild(a);
            list.appendChild(li);
        });
    });
}
