<script lang="ts">
	import Seo from '$lib/Seo.svelte';

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
		{ num: '01', name: 'Discover', blurb: 'What you do, who buys it, and what they type into Google.' },
		{ num: '02', name: 'Design', blurb: 'A look that fits your business — reviewed with you before a line is built.' },
		{ num: '03', name: 'Build', blurb: 'Hand-coded, fast, accessible. You watch it come together on a live preview.' },
		{ num: '04', name: 'Rank', blurb: 'Launch is the start: search console, indexing, and tuning until you show up.' },
	];
</script>

<Seo
	title="Small Business Website Design & SEO — Michigan | Full Scope Media"
	description="Full Scope Media designs and builds websites for small businesses in East Lansing, Lansing, and across Michigan — hand-coded, fast, and built to rank. Web design, local SEO, and Google Business Profile optimization from one studio."
/>

<!-- HERO -->
<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero">
		<p class="st-kicker">Web Design &amp; Build · Michigan</p>
		<h1 class="st-h1">Small business websites <span class="st-dim">built to be found.</span></h1>
		<p class="st-body">
			We design and build websites for small businesses in East Lansing, Lansing, and across
			Michigan — hand-coded, fast, and structured to rank on Google. Not a template with your
			logo on it: a site that works like a member of staff.
		</p>
		<div class="st-ctas">
			<a href="/studio/contact" class="st-btn st-btn-solid">Start a project</a>
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
<section class="st-frame steps">
	{#each steps as step (step.num)}
		<div class="step">
			<p class="st-num">{step.num}</p>
			<h3>{step.name}</h3>
			<p class="st-body">{step.blurb}</p>
		</div>
	{/each}
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

<!-- CTA -->
<section class="st-band">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Ready to be findable?</h2>
		<a href="/studio/contact" class="st-btn st-btn-invert">Start a project</a>
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
