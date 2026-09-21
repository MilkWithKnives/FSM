<script lang="ts">
	import Seo from '$lib/Seo.svelte';

	const services = [
		{
			num: '01',
			name: 'Photography',
			href: '/studio/photography',
			blurb: 'Product, brand, and on-location shoots — imagery your identity can stand on.',
			points: ['Product & brand shoots', 'On-location & lifestyle', 'Aerial drone', 'Real estate media'],
		},
		{
			num: '02',
			name: 'Web design & build',
			href: '/studio/web-design',
			blurb: 'Sites designed and shipped end-to-end — fast, findable, built to convert.',
			points: ['Design & full build', 'Local SEO & Google Business', 'Performance-first engineering', 'Copy & content structure'],
		},
		{
			num: '03',
			name: 'Systems & data',
			href: '/studio/systems',
			blurb: 'Integrations that connect your tools so the whole operation runs as one.',
			points: ['Tool integrations & automation', 'Dashboards & reporting', 'Booking & CRM flows', 'Data cleanup & migration'],
		},
	];
</script>

<Seo
	title="Studio — Web Design, Photography & Systems | Full Scope Media · East Lansing, MI"
	description="Full Scope Media's studio side: web design & build, brand photography, and systems integration for small businesses in East Lansing and across Michigan. One studio for everything your brand needs to be seen."
/>

<!-- HERO -->
<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero">
		<p class="st-kicker">Photography · Web · Systems &amp; Data</p>
		<h1 class="st-h1">I see the <span class="st-dim">whole picture.</span></h1>
		<p class="st-body">
			One studio for everything your brand needs to be seen — photography, web design &amp;
			build, and the systems that tie it all together. Based in East Lansing, working with
			small businesses across Michigan.
		</p>
		<div class="st-ctas">
			<a href="/studio/contact" class="st-btn st-btn-solid">Start a project</a>
			<a href="#services" class="st-btn">Explore services</a>
		</div>
	</div>
</section>

<!-- SERVICES -->
<section id="services">
	<div class="st-frame">
		<h2 class="st-h2 st-pad services-title">Services</h2>
	</div>
	{#each services as service (service.num)}
		<a href={service.href} class="st-frame row">
			<span class="st-cross tl"></span><span class="st-cross tr"></span>
			<div class="row-num st-num">{service.num}</div>
			<div class="row-name">
				<h3>{service.name}</h3>
				<span class="row-go" aria-hidden="true">Explore →</span>
			</div>
			<div class="row-detail">
				<p class="st-body">{service.blurb}</p>
				<ul class="st-list">
					{#each service.points as point (point)}
						<li>{point}</li>
					{/each}
				</ul>
			</div>
		</a>
	{/each}
</section>

<!-- REAL ESTATE CROSS-LINK -->
<section class="st-frame cross">
	<div class="st-pad cross-inner">
		<div>
			<p class="st-kicker">Selling a property?</p>
			<h2 class="st-h2">Listing photography lives on <span class="st-dim">the other side.</span></h2>
			<p class="st-body">
				Real estate photography, cinematic video, aerial drone, 3D tours, floor plans and
				virtual staging across Greater Lansing. Photos are delivered within 24 hours;
				video tours, including drone video, within 3–5 business days.
			</p>
		</div>
		<a href="/real-estate-photography" class="st-btn">Visit Real Estate Media</a>
	</div>
</section>

<!-- CTA -->
<section class="st-band">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Let's put the whole picture together.</h2>
		<a href="/studio/contact" class="st-btn st-btn-invert">Start a project</a>
	</div>
</section>

<style>
	.services-title {
		padding-top: 34px;
		padding-bottom: 34px;
	}

	.row {
		display: grid;
		grid-template-columns: clamp(48px, 6vw, 90px) 1fr 1.2fr;
		align-items: start;
		gap: clamp(16px, 3vw, 48px);
		padding: clamp(26px, 4vw, 52px) clamp(20px, 5vw, 72px);
		position: relative;
		transition: background 0.2s;
	}
	.row:hover {
		background: #e4e2de;
	}
	.row-num {
		padding-top: 6px;
	}
	.row-name h3 {
		font-size: clamp(20px, 2.6vw, 34px);
		font-weight: 800;
		line-height: 1.15;
	}
	.row-go {
		display: inline-block;
		margin-top: 12px;
		font-size: 12px;
		letter-spacing: 0.18em;
		text-transform: uppercase;
		color: var(--st-dim);
		transition: color 0.2s;
	}
	.row:hover .row-go {
		color: var(--st-accent);
	}
	.row-detail {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}

	.cross-inner {
		display: flex;
		flex-wrap: wrap;
		align-items: flex-end;
		justify-content: space-between;
		gap: 28px;
	}
	.cross-inner > div {
		display: flex;
		flex-direction: column;
		gap: 14px;
	}

	@media (max-width: 760px) {
		.row {
			grid-template-columns: 1fr;
			gap: 14px;
		}
		.row-num {
			padding-top: 0;
		}
	}
</style>
