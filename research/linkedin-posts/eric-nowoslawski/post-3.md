# Claude Code Doubled Response Rates for Enterprise Client — Autoresearch for Cold Email

**Author:** Eric Nowoslawski  
**Date:** 2025-04  
**Profile:** https://linkedin.com/in/outboundphd  

---

Claude Code doubled response rates in one week for an enterprise client.
We're starting to run Autoresearch for our customers.

## What is Autoresearch?

Andrej Karpathy dropped a public repo called Autoresearch — designed to give 
Machine Learning capabilities to anyone with a Claude Code or Codex account.
Originally built to run 5-minute experiments to improve AI on a task.

**Our adaptation:** Apply Autoresearch to cold email campaigns.

## How it works:

Pick one metric to improve → **Positive Response Rate**

Built a repo trained on:
- Client's past campaigns
- Current sales/marketing context  
- ICP definition
- Connected to DiscoLike / Prospeo for list creation

## The system runs 3 experiments automatically:

1. **List segmentation** — picks what won before or something new to try
2. **Copywriting** — angle + copy to match the list
3. **Upload** — pushes valid emails + copy straight into Smartlead via API

## Key lessons learned so far:

- Must give it rules for what CTA can be — otherwise it gives away 
  your product for free
- ALL data needs to be enriched in Clay first, then stored in Supabase
  so it doesn't make real-time enrichment decisions during campaigns

## Why this matters:

This is **Outbound 4.0** — a self-improving cold email system that runs 
experiments, learns what works, and uploads campaigns automatically.

Currently custom-built for one client. Working on standardizing for everyone.
Repo will be open-sourced when ready.