<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { siteUrl } from '$lib/business';

	const faqs = [
		{
			question: 'Do you build websites for businesses in both Lansing and East Lansing?',
			answer:
				'Yes. Full Scope Media is based in East Lansing and works with small businesses in Lansing, East Lansing, and elsewhere in Michigan.',
		},
		{
			question: 'Are your websites responsive and accessible?',
			answer:
				'Yes. Responsive layouts, keyboard-friendly navigation, readable content, and performance-conscious development are part of the build process.',
		},
		{
			question: 'What SEO work is included in a website build?',
			answer:
				'Each build starts with crawlable page structure, descriptive titles and metadata, structured data where appropriate, performance fundamentals, and indexing setup. Ongoing content and search work can continue after launch.',
		},
		{
			question: 'Can you help with an existing small-business website?',
			answer:
				'Yes. The first step is to review the current site, business goals, content, and technical constraints so we can recommend whether focused improvements or a new build makes more sense.',
		},
	];

	const faqJsonLd = {
		'@context': 'https://schema.org',
		'@graph': [
			{
				'@type': 'FAQPage',
				'@id': `${siteUrl}/studio/faq#faq`,
				url: `${siteUrl}/studio/faq`,
				mainEntity: faqs.map((faq) => ({
					'@type': 'Question',
					name: faq.question,
					acceptedAnswer: { '@type': 'Answer', text: faq.answer },
				})),
			},
			{
				'@type': 'BreadcrumbList',
				itemListElement: [
					{ '@type': 'ListItem', position: 1, name: 'Home', item: siteUrl },
					{ '@type': 'ListItem', position: 2, name: 'Studio', item: `${siteUrl}/studio` },
					{ '@type': 'ListItem', position: 3, name: 'FAQ', item: `${siteUrl}/studio/faq` },
				],
			},
		],
	};
</script>

<Seo
	title="Studio FAQ | Web Design & SEO | Full Scope Media"
	description="Answers to common questions about Full Scope Media's web design services, responsive websites, SEO, and improvements to existing sites in Lansing and East Lansing."
/>

<svelte:head>
	{@html `<script type="application/ld+json">${JSON.stringify(faqJsonLd).replace(/</g, '\\u003c')}<\/script>`}
</svelte:head>

<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero">
		<p class="st-kicker">Common questions</p>
		<h1 class="st-h1">Studio FAQ</h1>
		<p class="st-body">What to know before starting a website project.</p>
		<div class="st-ctas">
			<a href="/studio/web-design" class="st-btn">Explore web design</a>
		</div>
	</div>
</section>

<section class="st-frame faq-grid" aria-label="Web design questions and answers">
	{#each faqs as faq (faq.question)}
		<article class="faq-item">
			<h2>{faq.question}</h2>
			<p class="st-body">{faq.answer}</p>
		</article>
	{/each}
</section>

<section class="st-band">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Still have questions?</h2>
		<a href="/studio/contact" class="st-btn st-btn-invert">Get in touch</a>
	</div>
</section>

<style>
	.faq-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
	}
	.faq-item {
		padding: clamp(24px, 4vw, 48px) clamp(20px, 5vw, 72px);
		border-top: 1px solid var(--st-line);
	}
	.faq-item:nth-child(odd) {
		border-right: 1px solid var(--st-line);
	}
	.faq-item h2 {
		font-size: 17px;
		font-weight: 800;
		line-height: 1.4;
		margin-bottom: 14px;
	}

	@media (max-width: 860px) {
		.faq-grid {
			grid-template-columns: 1fr;
		}
		.faq-item:nth-child(odd) {
			border-right: none;
		}
	}
</style>
