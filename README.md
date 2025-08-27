# WerkScout
WerkScout

Plan and run many small, respectful search requests to discover links at scale.
WerkScout “slices” large search intents into safe chunks (API-first, HTML optional), with rate-limiting, backoff, and deduping built in.

⚖️ Use responsibly. Obey provider terms, robots, and local laws. Prefer official APIs whenever possible.

Why WerkScout?

Query planning: slice by alphabet, city/region, time windows, synonyms, include/exclude sites.

API-first: clean adapter for official search APIs (e.g., Bing Web Search API).

Polite: rate limits, jitter, retries, exponential backoff on challenge pages.

Resumable: caching + dedupe (hashing) to avoid refetching.

Pluggable: add providers/backends and exporters easily.

Simple outputs: JSONL/CSV/SQLite.
