# Claude Code Enrichment Has Gotten Scarily Good

**Author:** Patrick Spychalski  
**Date:** 2025  
**Profile:** https://linkedin.com/in/patrickspychalski  
**Topic:** Claude Code / AI enrichment / GTM stack

---

Claude Code enrichment has gotten scarily good. Here are a few learnings for people just getting started:

We've been experimenting over at The Kiln on what use cases Claude currently does well — not just for indie hackers, but for enterprise clients looking to use it in their GTM stack. One use case that has become clearly a frontrunner is enrichment.

**1. The success of enrichment in Claude Code is still fully contingent on the tools you connect to it.**  
While Claude Code is an incredible tool, it can't make company and person data appear out of thin air. For the large majority of use cases, you need to connect data APIs to do anything meaningful. I've been using BlitzAPI for a lot of our LinkedIn enrichment — it's $500/mo for unlimited data, which is absurdly cheap and while most of the data is a flat file, it's generally very recent and reliable. Combine that with an email validator, and you can source great lists for a fraction of a tool like ZoomInfo.

**2. Writing your data to a database is amazing for solving context bloat.**  
When you're enriching massive lists of companies and people, one thing you need to avoid is context bloat — giving the model a ton of information to ingest, decreasing performance. Connecting Claude to something like Supabase, so the model can read your database and reduce bloat, is absolutely necessary during large scale enrichment. Plus, it's a great way to visualize and gut check outputs.

**3. You need to be super specific on your desired output and process when using agents during enrichment.**  
This isn't anything new, but is specifically important in the context of enrichment in Claude Code. If you're going to send an agent off to retrieve data for you, be very specific about where it should find this data and how the data should be formatted when it returns in the column of your database. Otherwise, you'll get left with a ton of false and unstructured information. Even if the output looks good for sample runs, it can still hallucinate a lot at scale without the right specification.

Hope this is helpful! Would love to hear tips from others about what they've found from experimenting.

P.S — if you're building in the data for Claude Code space, DM me! We're always looking for great partners with great data to work with.