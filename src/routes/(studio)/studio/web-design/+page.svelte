<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { siteUrl } from '$lib/business';

	const deliverables = [
		{
			num: '01',
			name: 'Design & build',
			blurb:
				'A site designed around your business and built by hand — no page builders, no bloated themes. Fast on every phone, readable on every screen, shaped to make visitors act.',
			points: ['Custom design, not a template', 'Hand-coded, performance-first build', 'Mobile-responsive by default', 'Copy & content structure included'],
		},
		{
			num: '02',
			name: 'Local SEO',
			blurb:
				'Being found is the whole point. We build search into the site itself — the pages, titles, structure, and schema that put you in front of people searching for what you do.',
			points: ['Keyword research for your market', 'Location & service landing pages', 'Schema.org structured data', 'Google Business Profile optimization'],
		},
		{
			num: '03',
			name: 'Care & growth',
			blurb:
				"A website isn't done at launch. Hosting, updates, new pages, and search tuning as your business grows — handled, so you can run the business instead of the website.",
			points: ['Hosting & maintenance', 'Analytics that make sense', 'New pages & seasonal updates', 'Ongoing search-ranking work'],
		},
	];

	const steps = [
			{ num: '01', name: 'Discover', blurb: 'We learn what you do, who needs it, and what a useful website must help them accomplish.' },
			{ num: '02', name: 'Design', blurb: 'A look that fits your business — reviewed with you before a line is built.' },
			{ num: '03', name: 'Build', blurb: 'Hand-coded, fast, accessible. You watch it come together on a live preview.' },
			{ num: '04', name: 'Launch', blurb: 'We prepare indexing, analytics, and the technical SEO foundation, then support the site as it grows.' },
	];


	const webDesignJsonLd = {
			'@context': 'https://schema.org',
			'@graph': [
				{
					'@type': 'Service',
					'@id': `${siteUrl}/studio/web-design#service`,
					name: 'Custom web design and development',
					serviceType: 'Web design and development for small businesses',
					provider: { '@type': 'LocalBusiness', '@id': `${siteUrl}/#business`, name: 'Full Scope Media LLC' },
					areaServed: ['East Lansing, MI', 'Lansing, MI', 'Michigan'],
					url: `${siteUrl}/studio/web-design`,
					description:
						'Custom, responsive small-business websites with performance, accessibility, and technical SEO foundations.',
				},
				{
					'@type': 'BreadcrumbList',
					itemListElement: [
						{ '@type': 'ListItem', position: 1, name: 'Home', item: siteUrl },
						{ '@type': 'ListItem', position: 2, name: 'Studio', item: `${siteUrl}/studio` },
						{ '@type': 'ListItem', position: 3, name: 'Web Design', item: `${siteUrl}/studio/web-design` },
					],
				},
			],
	};
</script>

<Seo
	title="Web Design in Lansing & East Lansing, MI | Full Scope Media"
	description="Custom web design and development for small businesses in Lansing and East Lansing, MI. Responsive, performance-focused websites with strong SEO foundations."
/>

<svelte:head>
	{@html `<script type="application/ld+json">${JSON.stringify(webDesignJsonLd).replace(/</g, '\\u003c')}<\/script>`}
</svelte:head>

<!-- HERO -->
<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero">
		<p class="st-kicker">Web Design &amp; Development · Greater Lansing</p>
		<h1 class="st-h1">Custom web design for <span class="st-dim">Lansing &amp; East Lansing.</span></h1>
		<p class="st-body">
			Full Scope Media designs and develops responsive websites for small businesses in East Lansing,
			Lansing, and across Michigan. Each site is shaped around the business, its customers, and the
			actions visitors need to take — with performance, accessibility, and search fundamentals built in.
		</p>
		<div class="st-ctas">
			<a href="/studio/contact" class="st-btn st-btn-solid" data-analytics-event="web-design-contact">Discuss your website</a>
			<a href="#seo" class="st-btn">About the SEO</a>
		</div>
	</div>
</section>

<!-- DELIVERABLES -->
<section>
	{#each deliverables as item (item.num)}
		<div class="st-frame row">
			<span class="st-cross tl"></span><span class="st-cross tr"></span>
			<div class="st-num">{item.num}</div>
			<h2 class="row-name">{item.name}</h2>
			<div class="row-detail">
				<p class="st-body">{item.blurb}</p>
				<ul class="st-list">
					{#each item.points as point (point)}
						<li>{point}</li>
					{/each}
				</ul>
			</div>
		</div>
	{/each}
</section>

<!-- SEO SECTION -->
<section id="seo" class="st-frame">
	<div class="st-pad seo-grid">
		<div>
			<p class="st-kicker">SEO Specialist · Greater Lansing</p>
			<h2 class="st-h2">Ranking is a feature, <span class="st-dim">not an add-on.</span></h2>
		</div>
		<div class="seo-copy">
			<p class="st-body">
				Most "SEO specialists" are selling reports. We build the thing the reports ask for:
				pages that answer what your customers actually search, markup that Google can read,
				and a Google Business Profile that pulls its weight in the map pack.
			</p>
			<p class="st-body">
				It's how our own real estate photography side ranks in East Lansing — the same
				playbook, applied to your business: keyword research, location pages, structured
				data, reviews strategy, and the patience to keep tuning after launch.
			</p>
		</div>
	</div>
</section>

<!-- PROCESS -->
<section class="st-frame" aria-labelledby="process-heading">
	<div class="st-pad section-heading">
		<p class="st-kicker">How a project works</p>
		<h2 id="process-heading" class="st-h2">A clear path from first conversation to launch.</h2>
	</div>
	<div class="steps">
		{#each steps as step (step.num)}
			<div class="step">
				<p class="st-num">{step.num}</p>
				<h3>{step.name}</h3>
				<p class="st-body">{step.blurb}</p>
			</div>
		{/each}
	</div>
</section>

<!-- PROOF -->
<section class="st-frame">
	<div class="st-pad st-band-inner">
		<div class="proof">
			<p class="st-kicker">Proof of work</p>
			<p class="st-body">
				You're on it. This site — the eye, the photography side, the studio — was designed
				and hand-built by us, end to end.
			</p>
		</div>
		<a href="/real-estate-photography" class="st-btn">See the photography side</a>
	</div>
</section>

<!-- FAQ LINK -->
<section class="st-frame">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Questions about your website project?</h2>
		<a href="/studio/faq" class="st-btn">Read the studio FAQ</a>
	</div>
</section>

<!-- CTA -->
<section class="st-band">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Ready to be findable?</h2>
		<a href="/studio/contact" class="st-btn st-btn-invert" data-analytics-event="web-design-contact">Start a project</a>
	</div>
</section>

<style>
	.row {
		display: grid;
		grid-template-columns: clamp(48px, 6vw, 90px) 1fr 1.2fr;
		align-items: start;
		gap: clamp(16px, 3vw, 48px);
		padding: clamp(26px, 4vw, 52px) clamp(20px, 5vw, 72px);
		position: relative;
	}
	.row-name {
		font-size: clamp(20px, 2.6vw, 34px);
		font-weight: 800;
		line-height: 1.15;
	}
	.row-detail {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}

	.seo-grid {
		display: grid;
		grid-template-columns: 1fr 1.2fr;
		gap: clamp(20px, 4vw, 56px);
	}
	.seo-grid .st-kicker {
		margin-bottom: 14px;
	}
	.seo-copy {
		display: flex;
		flex-direction: column;
		gap: 14px;
	}

	.steps {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
	}
	.section-heading {
		display: flex;
		flex-direction: column;
		gap: 14px;
	}
	.step {
		padding: clamp(22px, 3vw, 40px) clamp(18px, 2.5vw, 34px);
		border-right: 1px solid var(--st-line);
		display: flex;
		flex-direction: column;
		gap: 10px;
	}
	.step:last-child {
		border-right: none;
	}
	.step h3 {
		font-size: 18px;
		font-weight: 800;
	}

	.proof {
		display: flex;
		flex-direction: column;
		gap: 10px;
		max-width: 560px;
	}


	@media (max-width: 860px) {
		.row,
		.seo-grid {
			grid-template-columns: 1fr;
			gap: 14px;
		}
		.steps {
			grid-template-columns: 1fr 1fr;
		}
		.step {
			border-bottom: 1px solid var(--st-line);
		}
		.step:nth-child(even) {
			border-right: none;
		}
		.step:nth-child(n + 3) {
			border-bottom: none;
		}
	}
</style>
