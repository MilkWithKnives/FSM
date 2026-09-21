<script lang="ts">
	import Seo from '$lib/Seo.svelte';

	const problems = [
		{
			num: '01',
			name: 'Automate the busywork',
			blurb:
				'The invoice that gets retyped into three places. The booking that has to be copied to the calendar, the spreadsheet, and the group chat. I wire your tools together so it happens once.',
			points: ['Bookings → calendar → invoicing flows', 'Automatic follow-ups & reminders', 'Form submissions routed where they belong'],
		},
		{
			num: '02',
			name: 'See your numbers',
			blurb:
				"Revenue lives in one app, jobs in another, ad spend in a third. I pull it into one dashboard so Monday morning starts with answers instead of tab-hopping.",
			points: ['One dashboard across your tools', 'Reports that send themselves', 'Numbers a non-accountant can read'],
		},
		{
			num: '03',
			name: 'Connect the stack',
			blurb:
				"CRM, point of sale, email list, website — most small-business tools can talk to each other; they just haven't been introduced. I build the connections and keep them healthy.",
			points: ['CRM & email list syncing', 'Website ↔ back-office integration', 'Data cleanup & migrations'],
		},
	];
</script>

<Seo
	title="Systems & Data Integration for Small Businesses — Michigan | Full Scope Media"
	description="Full Scope Media connects the tools your small business already uses — automations, dashboards, CRM and booking flows, data cleanup — so the whole operation runs as one. East Lansing, MI, serving businesses across Michigan."
/>

<!-- HERO -->
<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero">
		<p class="st-kicker">Systems &amp; Data · Michigan</p>
		<h1 class="st-h1">Your tools should <span class="st-dim">talk to each other.</span></h1>
		<p class="st-body">
			Most small businesses run on five apps and a lot of retyping. I build the integrations,
			automations, and dashboards that make them run as one operation — so the data moves
			itself and you get your evenings back.
		</p>
		<div class="st-ctas">
			<a href="/studio/contact" class="st-btn st-btn-solid">Tell me what's manual</a>
		</div>
	</div>
</section>

<!-- WHAT I FIX -->
<section>
	{#each problems as item (item.num)}
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

<!-- HOW IT PAIRS -->
<section class="st-frame">
	<div class="st-pad st-band-inner">
		<div class="pair">
			<p class="st-kicker">Better together</p>
			<p class="st-body">
				Systems work pairs naturally with a <a href="/studio/web-design" class="inline-link">website build</a> —
				the site becomes the front door of a back office that actually runs itself.
			</p>
		</div>
		<a href="/studio/web-design" class="st-btn">See web design</a>
	</div>
</section>

<!-- CTA -->
<section class="st-band">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Stop being your own integration.</h2>
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

	.pair {
		display: flex;
		flex-direction: column;
		gap: 10px;
		max-width: 560px;
	}
	.inline-link {
		text-decoration: underline;
		text-underline-offset: 4px;
	}
	.inline-link:hover {
		color: var(--st-accent);
	}

	@media (max-width: 860px) {
		.row {
			grid-template-columns: 1fr;
			gap: 14px;
		}
	}
</style>
