<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { properties } from '$lib/properties';
	import { photoSrcset, heroFallback, PHOTO_SIZES_FULL } from '$lib/images';

	const heroProperty = properties[2];

	const includes = [
		'Accurate, scaled 2D floor plan via CubiCasa',
		'Room dimensions and total square footage',
		'Black-and-white or branded color versions',
		'Optional furniture layout for context',
		'Web + print-ready files for the MLS and flyers',
		'Turnaround within 24–48 hours',
	];
</script>

<Seo
	title="Real Estate Floor Plans (CubiCasa) | Full Scope Media · East Lansing, MI"
	description="Professional, accurately scaled real estate floor plans in East Lansing and greater Michigan, produced with CubiCasa. Room dimensions and square footage delivered in 24–48 hours. Starting at $200."
	ogTitle="Real Estate Floor Plans (CubiCasa) | Full Scope Media"
	ogDescription="Accurately scaled CubiCasa floor plans with room dimensions, serving East Lansing and greater Michigan."
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
			alt="Real estate floor plan photography"
			fetchpriority="high"
			class="absolute inset-0 w-full h-full object-cover"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Services</p>
		<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Floor Plans</h1>
	</div>
</section>

<!-- INTRO -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
		<div>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-6">Powered by CubiCasa</p>
			<h2 class="text-3xl md:text-4xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
				Help buyers picture the whole layout.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-6">
				Photos sell the feeling of a home; a floor plan sells the flow. Buyers want to know how the rooms connect, where the furniture goes, and whether the layout actually works for them — and listings with a floor plan hold attention longer.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-10">
				We produce clean, accurately scaled floor plans with <span class="text-gray-700">CubiCasa</span>, complete with room dimensions and total square footage. It's a small add-on that cuts down on wasted showings from buyers who were never the right fit.
			</p>
			<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">ADD A FLOOR PLAN</a>
		</div>
		<div>
			<p class="text-xs tracking-widest uppercase text-gray-500 mb-6">Every Floor Plan Includes</p>
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
				<p class="text-3xl font-light" style="font-family: var(--font-serif)">$200</p>
				<a href="/pricing" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity mt-4 inline-block">View Full Pricing</a>
			</div>
		</div>
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Add a Floor Plan to Your Listing</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
