<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { properties } from '$lib/properties';
	import { photoSrcset, heroFallback, PHOTO_SIZES_FULL } from '$lib/images';

	const heroProperty = properties[1];

	const includes = [
		'Your choice of Zillow 3D Home or Matterport — whichever fits your listing',
		'Fully navigable, room-to-room virtual walkthrough',
		'Matterport dollhouse + floor-plan views',
		'Embeds directly on the MLS, Zillow, and your website',
		'Hosted, shareable link — buyers tour anytime, anywhere',
		'Delivered within 2–3 business days',
	];
</script>

<Seo
	title="3D Virtual Tours — Matterport & Zillow 3D | Full Scope Media · East Lansing, MI"
	description="Interactive 3D home tours in East Lansing and greater Michigan. We shoot both Zillow 3D Home and Matterport tours, so buyers can walk through your listing online anytime. Starting at $300."
	ogTitle="3D Virtual Tours — Matterport & Zillow 3D | Full Scope Media"
	ogDescription="Interactive Matterport and Zillow 3D home tours, serving East Lansing and greater Michigan."
/>

<!-- HERO -->
<section class="relative h-[60vh] overflow-hidden">
	<picture>
		<source type="image/avif" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'avif')} sizes={PHOTO_SIZES_FULL} />
		<source type="image/webp" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
		<img
			src={heroFallback(heroProperty)}
			srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'jpg')}
			sizes={PHOTO_SIZES_FULL}
			alt="3D virtual tour real estate photography"
			fetchpriority="high"
			class="absolute inset-0 w-full h-full object-cover"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Services</p>
		<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">3D Tours</h1>
	</div>
</section>

<!-- INTRO -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
		<div>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-6">Matterport &amp; Zillow 3D Home</p>
			<h2 class="text-3xl md:text-4xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
				Let buyers walk through — before they ever arrive.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-6">
				A 3D tour turns your listing into an always-open house. Buyers move room to room, see how spaces connect, and revisit the home as many times as they like — which means the people who book a showing are already serious.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-10">
				We shoot both <span class="text-gray-700">Zillow 3D Home</span> and <span class="text-gray-700">Matterport</span>, and recommend whichever fits your listing and platform mix. Prefer one over the other? Just tell us — it's your call.
			</p>
			<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">BOOK A 3D TOUR</a>
		</div>
		<div>
			<p class="text-xs tracking-widest uppercase text-gray-500 mb-6">Every 3D Tour Includes</p>
			<ul class="flex flex-col gap-3 mb-10">
				{#each includes as item}
					<li class="flex items-start gap-3 text-sm text-gray-600">
						<span class="text-black mt-1">—</span>
						{item}
					</li>
				{/each}
			</ul>
			<div class="pt-8 border-t border-gray-100">
				<p class="text-xs tracking-widest uppercase text-gray-500 mb-2">Starting At</p>
				<p class="text-3xl font-light" style="font-family: var(--font-serif)">$300</p>
				<a href="/pricing" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity mt-4 inline-block">View Full Pricing</a>
			</div>
		</div>
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Give Your Listing a 3D Walkthrough</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
