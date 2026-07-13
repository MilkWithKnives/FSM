<script lang="ts">
	import Seo from '$lib/Seo.svelte';

	const work = [
		{
			num: '01',
			name: 'Product & brand',
			blurb:
				'Clean, consistent product imagery and the brand shots that make a website, a menu, or a storefront feel like one thing. Shot to match how and where they will be used.',
			points: ['Product photography', 'Brand & team portraits', 'Menus, interiors & storefronts'],
		},
		{
			num: '02',
			name: 'On-location & lifestyle',
			blurb:
				'Your business as it actually runs — the work, the space, the people. The imagery that fills a website, a Google Business Profile, and a year of social posts in one shoot.',
			points: ['Working sessions & behind-the-scenes', 'Lifestyle & environmental shots', 'Google Business Profile photo sets'],
		},
		{
			num: '03',
			name: 'Aerial drone',
			blurb:
				"Drone work for the shots you can't get from the ground — facilities, land, events, and the establishing views that give everything else context.",
			points: ['Facilities & property aerials', 'Events & progress documentation', 'Establishing & context views'],
		},
	];
</script>

<Seo
	title="Brand & Product Photography — East Lansing, MI | Full Scope Media"
	description="Brand, product, on-location, and aerial drone photography for businesses in East Lansing and Greater Lansing, MI. Full Scope Media shoots the imagery your website, Google profile, and marketing actually need."
/>

<!-- HERO -->
<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero">
		<p class="st-kicker">Photography · East Lansing, MI</p>
		<h1 class="st-h1">Imagery your brand <span class="st-dim">can stand on.</span></h1>
		<p class="st-body">
			Product, brand, on-location, and aerial photography for businesses across Greater
			Lansing — shot for the places it will actually live: your website, your Google profile,
			your marketing.
		</p>
		<div class="st-ctas">
			<a href="/studio/contact" class="st-btn st-btn-solid">Book a shoot</a>
		</div>
	</div>
</section>

<!-- WORK -->
<section>
	{#each work as item (item.num)}
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

<!-- REAL ESTATE CROSS-LINK -->
<section class="st-frame">
	<div class="st-pad st-band-inner">
		<div class="cross">
			<p class="st-kicker">Listing a property?</p>
			<p class="st-body">
				Real estate photography is its own side of the house — photos, video, 3D tours,
				floor plans, and virtual staging, delivered in 24 hours.
			</p>
		</div>
		<a href="/real-estate-photography" class="st-btn">Visit Real Estate Media</a>
	</div>
</section>

<!-- CTA -->
<section class="st-band">
	<div class="st-pad st-band-inner">
		<h2 class="st-h2">Let's shoot the real thing.</h2>
		<a href="/studio/contact" class="st-btn st-btn-invert">Book a shoot</a>
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

	.cross {
		display: flex;
		flex-direction: column;
		gap: 10px;
		max-width: 560px;
	}

	@media (max-width: 860px) {
		.row {
			grid-template-columns: 1fr;
			gap: 14px;
		}
	}
</style>
