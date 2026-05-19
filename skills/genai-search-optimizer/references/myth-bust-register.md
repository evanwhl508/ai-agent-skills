# Myth Bust Register

Google Search Central has explicitly identified the tactics below as ineffective for generative AI search visibility. When a user proposes one, refuse it, cite Google's stated position, and propose the foundational SEO equivalent that actually applies.

Source: "Optimizing your website for generative AI features on Google Search" (developers.google.com/search/docs/fundamentals/ai-optimization-guide), section "Mythbusting generative AI search: what you don't need to do."

## Myth 1: llms.txt files and other AI-targeted machine-readable files

```text
Myth:
"Add an llms.txt or ai.txt file so Google AI features can consume your content."

Where it appears:
SEO and GEO blogs, YouTube tutorials, vendor marketing.

What Google says:
"You don't need to create new machine readable files, AI text files, markup, or Markdown to appear in generative AI search."

Why it does not work:
Google may discover and crawl many file types in addition to HTML, but that does not mean any file is treated in a special way by generative AI features. Google's AI features rely on the same Search index and ranking systems, not on AI-targeted side files.

What to do instead:
Focus on indexable, snippet-eligible HTML pages with strong primary content. Use robots.txt and sitemaps for crawl control as usual.

Citation:
developers.google.com/search/docs/fundamentals/ai-optimization-guide
```

## Myth 2: Content chunking for AI ingestion

```text
Myth:
"Break content into small chunks so AI can ingest and cite it better."

Where it appears:
Posts that conflate RAG architecture inside an LLM with how Google's grounding works on the open web.

What Google says:
"There's no requirement to break your content into tiny pieces for AI to better understand it. Google systems are able to understand the nuance of multiple topics on a page and show the relevant piece to users."

Why it does not work:
Google's systems can extract relevant passages from longer pages. Chunking does not improve grounding; it can fragment otherwise strong pages and dilute their value to readers.

What to do instead:
Write to the length the audience and subject need. Use headings and structure for human readers. Trust Google's systems to surface the relevant passage.

Citation:
developers.google.com/search/docs/fundamentals/ai-optimization-guide
```

## Myth 3: Rewriting content for AI systems

```text
Myth:
"Rewrite prose in a more AI-friendly style or cover every long-tail keyword variant so AI can parse it."

Where it appears:
"AEO" guides, AI-content-tooling marketing, keyword-variant generators.

What Google says:
"You don't need to write in a specific way just for generative AI search. AI systems can understand synonyms and general meanings of what someone is seeking, in order to connect them with content that might not use the same precise words."

Why it does not work:
AI search systems handle synonyms and intent. Rewriting for AI parsing typically degrades the experience for human readers, which is the audience Google's helpful-content systems prioritize.

What to do instead:
Write for the human audience. Use natural language. Cover the topic well, not every phrase variant. Avoid scaled keyword-variant pages, which can trigger Google's scaled content abuse policy.

Citation:
developers.google.com/search/docs/fundamentals/ai-optimization-guide
```

## Myth 4: Seeking inauthentic mentions

```text
Myth:
"Buy mentions or seed forum posts and blog references so AI features cite your brand."

Where it appears:
Reputation management services, "PR for GEO" packages, gray-hat link/mention campaigns.

What Google says:
"Seeking inauthentic 'mentions' across the web isn't as helpful as it might seem. Our core ranking systems focus on high-quality content while other systems block spam; our generative AI features depend on both."

Why it does not work:
Generative AI features rely on Google's core ranking and spam systems. Inauthentic mentions are exactly what those systems aim to discount or filter.

What to do instead:
Earn authentic mentions through useful content, real product value, and genuine community participation. If the goal is brand presence on the web, invest in original work that people would naturally reference.

Citation:
developers.google.com/search/docs/fundamentals/ai-optimization-guide
```

## Myth 5: Overfocusing on structured data

```text
Myth:
"Add as much schema.org markup as possible because AI search prefers structured data."

Where it appears:
Schema-stacking templates, "GEO checklist" downloads, plugin marketing.

What Google says:
"Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add. However, it's a good idea to continue using it as part of your overall SEO strategy, as it helps with being eligible for rich results on Google Search."

Why it does not work:
Structured data does not improve generative AI search visibility on its own. It supports rich result eligibility in classic Search, which is its actual purpose.

What to do instead:
Use structured data where it supports specific rich result types (recipes, events, jobs, products, etc.). Validate the markup. Do not add schema speculatively for AI search benefit.

Citation:
developers.google.com/search/docs/fundamentals/ai-optimization-guide
```

## Myth 6: Scaled long-tail page generation

```text
Myth:
"Generate a page for every variant of a query so AI search has more entry points."

Where it appears:
"Programmatic SEO" templates that produce thousands of near-duplicate pages, AI-content farms.

What Google says:
"While it might be tempting to create separate content for every possible variation of how people might search (for example, by focusing on other queries that people have asked, or fan-out queries), doing so primarily to manipulate rankings or generative AI responses in Google Search violates Google's scaled content abuse spam policy."

Why it does not work:
A high quantity of pages does not make a site higher quality or more relevant. Google's spam systems target scaled content abuse, and AI features depend on those systems.

What to do instead:
Produce fewer, deeper pages with unique perspective and expertise. Cover the user intent fully on a single page rather than fragmenting it across keyword variants.

Citation:
developers.google.com/search/docs/fundamentals/ai-optimization-guide and developers.google.com/search/docs/essentials/spam-policies
```

## How to refuse a myth in practice

When a user proposes any of the above:

1. Name the tactic and the myth number from this register.
2. Quote or paraphrase Google's stated position.
3. State why it does not work.
4. Propose the foundational SEO equivalent.
5. Link the citation so the user can verify.

Do not soften the refusal with "you can try it anyway." If Google has stated a tactic is unnecessary or against policy, the skill's job is to say so.
