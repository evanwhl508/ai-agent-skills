# Source Notes

This skill is unofficial and original synthesis. It is grounded in Google Search Central's public documentation. It is not affiliated with Google.

Last reviewed: 2026-05-20.

## Canonical sources

Primary source pages reviewed when authoring this skill:

- "Optimizing your website for generative AI features on Google Search."
  developers.google.com/search/docs/fundamentals/ai-optimization-guide
- "Google Search's guidance on using generative AI content on your website."
  developers.google.com/search/docs/fundamentals/using-gen-ai-content
- "Creating helpful, reliable, people-first content."
  developers.google.com/search/docs/fundamentals/creating-helpful-content
- "Search Essentials" (technical requirements, spam policies, key best practices).
  developers.google.com/search/docs/essentials
- "Spam policies for Google web search" (scaled content abuse and related).
  developers.google.com/search/docs/essentials/spam-policies
- "Maintaining your website's SEO" (technical SEO techniques and strategies).
  developers.google.com/search/docs/fundamentals/get-started
- "SEO starter guide."
  developers.google.com/search/docs/fundamentals/seo-starter-guide
- "Image SEO best practices."
  developers.google.com/search/docs/appearance/google-images
- "Video SEO best practices."
  developers.google.com/search/docs/appearance/video
- "Structured data introduction."
  developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- "Page experience."
  developers.google.com/search/docs/appearance/page-experience
- "JavaScript SEO basics."
  developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics

Supporting sources:

- Google Merchant Center help center (AI-generated content policy, product feed requirements).
  support.google.com/merchants
- Google Business Profile help center.
  business.google.com and support.google.com/business
- Agent-friendly website UX guidance.
  web.dev/articles/ai-agent-site-ux
- Universal Commerce Protocol.
  ucp.dev

Google updates its Search Central guidance regularly. Treat the "last reviewed" date above as the canonical version reflected in this skill. Re-review quarterly.

## Distilled principles

- Optimizing for generative AI search is still SEO. Google's AI features are grounded in core ranking and quality systems.
- A page must be indexable and snippet-eligible to be eligible to appear in AI Overviews or AI Mode.
- Generative AI features use retrieval-augmented generation (grounding) and query fan-out internally. Content visibility flows from the same Search index and ranking systems that classic Search uses.
- Non-commodity, experience-led content beats recycled common knowledge.
- Write for the human audience. Do not rewrite for AI parsing.
- Technical structure should be clear and crawlable but does not need to be pedantically perfect HTML.
- Page experience matters: HTTPS, mobile-friendly, fast, no intrusive interstitials.
- Structured data supports rich result eligibility, not AI search visibility on its own.
- Image and video SEO best practices apply to AI search too.
- Scaled content abuse policy applies regardless of whether the content is AI-generated.
- AI-generated content should meet Search Essentials independent of how it was produced. Disclose where it adds reader context. Follow Merchant Center policy for ecommerce.
- Merchant Center and Google Business Profile remain the primary surfaces for ecommerce and local visibility, including in AI responses.

## Myth-bust register (summary)

Five tactics Google has explicitly identified as ineffective for generative AI search visibility:

1. llms.txt files and other AI-targeted machine-readable files.
2. Content chunking for AI ingestion.
3. Rewriting prose specifically for AI systems.
4. Seeking inauthentic mentions.
5. Overfocusing on structured data for AI search benefit.

Plus a sixth derived from the scaled content abuse policy:

6. Scaled long-tail page generation per keyword variant.

For full text and citations, read `myth-bust-register.md` in this skill.

## Originality and attribution guidance

- Quote Google Search Central directly when the wording of the statement matters (especially in the myth-bust register).
- Paraphrase otherwise. Do not copy large sections of Google's documentation verbatim into this skill.
- Frame the skill as unofficial original synthesis, not as a re-host of Google's documentation.
- Strengthen examples with concrete, non-Google-sourced cases when illustrating rewrite patterns.

## What is original to this skill

- The 5-phase workflow (Frame, Audit, Diagnose, Rewrite, Plan).
- The refusal-first posture for AEO/GEO myths with citation.
- The content rewrite pattern library.
- The cross-harness portability structure shared with the rest of the `ai-agent-skills` collection.
- The action plan template oriented around blockers, high-impact, polish, and myth-bust lists with effort estimates.

## What is sourced from Google Search Central

- The list of myths and Google's stated positions on each (paraphrased and cited).
- The technical SEO checklist items (paraphrased from the technical guidance pages).
- The helpful-content principles (paraphrased from the helpful-content guidance).
- The Merchant Center and Business Profile signal expectations (paraphrased from the help centers).

When in doubt about whether a claim is supported by Google's public guidance, cite the specific page or remove the claim.
