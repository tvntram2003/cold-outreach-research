from youtube_transcript_api import YouTubeTranscriptApi
import os

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
        ("tavbnQ9Aah8", "mastering-outbound-growth-coldiq-2024"),
        ("lw_710PtAos", "coldiq-linkedin-success-system-2026"),
    ],
    "patrick-dang": [
        ("t0Pq1uRjszI", "ultimate-cold-email-guide-b2b-2024"),
        ("W-znS2Tkl8o", "top-5-cold-email-tips-b2b-saas"),
    ],
    "patrick-spychalski": [
        ("Pfk4YMulfsc", "clay-agency-secrets-40m-pipeline-2025"),
        ("PQ9WSCD9x24", "best-clay-outbound-tactics-2025"),
    ],
    "jack-reamer": [
        ("YZg1uBWN2pA", "truth-about-cold-email-jack-reamer"),
        ("8gBcbQcNvJo", "cold-outreach-podcast-breakdown"),
    ],
    "vin-matano": [
        ("sT3PfNQVa0M", "close-90-percent-leads-without-cold-call-2024"),
        ("tpTmil_Ydss", "cold-calls-ai-bots-demandbase-2024"),
    ],
    "michel-lieben": [
        ("j0tm-2eKgs0", "cold-outreach-for-beginners-coldiq-2024"),
        ("R9qgcrGPfsc", "build-scale-gtm-engineering-coldiq-2025"),
    ],
}

for author, video_list in videos.items():
    folder = f"research/youtube-transcripts/{author}"
    os.makedirs(folder, exist_ok=True)

    for video_id, title in video_list:
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