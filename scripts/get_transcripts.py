from youtube_transcript_api import YouTubeTranscriptApi

videos = {
    "eric-nowoslawski": [
        ("7ttZEC6khZ0", "cold-email-tech-stack-clay-smartlead"),
        ("WmrYeN3GE3w", "real-campaign-breakdowns"),
    ],
    "nick-abraham": [
        ("ILK_opONAUg", "cold-email-mastery-next-level-tactics-2024"),
        ("8gBcbQcNvJo", "cold-email-outreach-masterclass"),
    ],
    "daniel-fazio": [
        ("o_uzONiUG9g", "realistic-results-from-cold-email-2024"),
        ("t1QEt7JNx5E", "most-popular-cold-email-course-secrets"),
    ],
    "jason-bay": [
        ("8bRkHSUa0tc", "hot-take-future-of-cold-calling-2025"),
        ("c5DvcHlt1c8", "reigniting-outbound-2024"),
    ],
    "alex-vacca": [
        ("VIDEOID_1", "ten-video-1"),
        ("VIDEOID_2", "ten-video-2"),
    ],
    "jack-reamer": [
        ("VIDEOID_1", "ten-video-1"),
        ("VIDEOID_2", "ten-video-2"),
    ],
    "patrick-dang": [
        ("VIDEOID_1", "ten-video-1"),
        ("VIDEOID_2", "ten-video-2"),
    ],
    "patrick-spychalski": [
        ("VIDEOID_1", "ten-video-1"),
        ("VIDEOID_2", "ten-video-2"),
    ],
    "vin-matano": [
        ("VIDEOID_1", "ten-video-1"),
        ("VIDEOID_2", "ten-video-2"),
    ],
    "michel-lieben": [
        ("VIDEOID_1", "ten-video-1"),
        ("VIDEOID_2", "ten-video-2"),
    ],
}

import os

for author, video_list in videos.items():
    folder = f"research/youtube-transcripts/{author}"
    os.makedirs(folder, exist_ok=True)

    for video_id, title in video_list:
        if video_id.startswith("VIDEOID"):
            print(f"  Bỏ qua (chưa có ID): {author} — {title}")
            continue

        print(f"Đang lấy: {author} — {title}")
        try:
            fetcher = YouTubeTranscriptApi()
            transcript = fetcher.fetch(video_id)
            full_text = " ".join([entry.text for entry in transcript])

            filepath = f"{folder}/{title}.md"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title.replace('-', ' ').title()}\n\n")
                f.write(f"**Author:** {author}\n")
                f.write(f"**Video:** https://youtube.com/watch?v={video_id}\n\n")
                f.write("---\n\n")
                f.write(full_text)

            print(f"  Xong: {filepath}")

        except Exception as e:
            print(f"  Loi {video_id}: {e}")

print("\nHoan thanh!")