import re
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound
)

def extract_video_id(youtube_url: str) -> str:
    """Extract the 11‑char YouTube ID from a URL via regex."""
    pattern = r"(?:v=|youtu\.be/|/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

def fetch_transcript(video_id: str, languages: list = ["en", "hi"]) -> str:
    """
    Instantiate the YouTubeTranscriptApi and call `.fetch()` per language.
    Returns the concatenated text or None.
    """
    api = YouTubeTranscriptApi()
    for lang in languages:
        try:
            snippets = api.fetch(video_id, languages=[lang])
            return " ".join(s.text for s in snippets)
        except (TranscriptsDisabled, NoTranscriptFound, Exception):
            continue
    return None
