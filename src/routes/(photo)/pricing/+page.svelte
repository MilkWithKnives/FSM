<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { properties } from '$lib/properties';
	import { photoSrcset, photoFallback, PHOTO_SIZES_HALF } from '$lib/images';

	const tierImages = [
		{ slug: properties[2].slug, n: properties[2].selected[0] },
		{ slug: properties[1].slug, n: properties[1].selected[0] },
		{ slug: properties[0].slug, n: properties[0].selected[0] },
		{ slug: properties[3].slug, n: properties[3].selected[0] },
	];

	const tiers = [
		{
			sqft: '1,000 – 1,999 sqft',
			img: tierImages[0],
			services: [
				{ name: 'Photography', price: '$480' },
				{ name: 'Video Tour', price: '$480' },
				{ name: 'Floorplan', price: '$200' },
				{ name: 'Matterport 3D', price: '$300' },
			],
		},
		{
			sqft: '2,000 – 2,999 sqft',
			img: tierImages[1],
			services: [
				{ name: 'Photography', price: '$520' },
				{ name: 'Video Tour', price: '$980' },
				{ name: 'Floorplan', price: '$300' },
				{ name: 'Matterport 3D', price: '$400' },
			],
		},
		{
			sqft: '3,000 – 3,999 sqft',
			img: tierImages[2],
			services: [
				{ name: 'Photography', price: '$600' },
				{ name: 'Video Tour', price: '$1,100' },
				{ name: 'Floorplan', price: '$350' },
				{ name: 'Matterport 3D', price: '$500' },
			],
		},
		{
			sqft: '4,000 – 4,999 sqft',
			img: tierImages[3],
			services: [
				{ name: 'Photography', price: '$720' },
				{ name: 'Video Tour', price: '$1,400' },
				{ name: 'Floorplan', price: '$400' },
				{ name: 'Matterport 3D', price: '$600' },
			],
		},
	];
</script>

<Seo
	title="Pricing | Full Scope Media LLC · Real Estate Photography Packages East Lansing, MI"
	description="Transparent real estate photography and video pricing by property size. Packages starting at $480 for photography, $480 for video. Serving East Lansing and greater Michigan."
	ogTitle="Pricing | Full Scope Media LLC"
	ogDescription="Real estate photography packages starting at $480. Transparent pricing by property size, serving East Lansing, MI."
/>

<!-- HEADER -->
<section class="pt-20 pb-4 px-8 lg:px-20 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Transparent Pricing</p>
	<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Pricing</h1>
</section>

<!-- INTRO -->
<section class="px-8 lg:px-20 pb-16 max-w-6xl mx-auto">
	<p class="text-sm text-gray-500 max-w-xl leading-relaxed mt-4">
		All packages include 1 location, a 2–2.5 hour shoot, and 40 fully edited photos delivered with a guaranteed 24-hour turnaround. Custom packages available for larger estates.
	</p>
</section>

<!-- PRICING TIERS -->
<section class="px-8 lg:px-20 pb-28 max-w-6xl mx-auto flex flex-col gap-0">
	{#each tiers as tier, i}
		<div class="grid grid-cols-1 md:grid-cols-2 gap-0 border-t border-gray-100 {i === tiers.length - 1 ? 'border-b' : ''}">
			<div class="overflow-hidden aspect-[16/10] {i % 2 === 1 ? 'md:order-2' : ''}">
				<picture>
					<source type="image/avif" srcset={photoSrcset(tier.img.slug, tier.img.n, 'avif')} sizes={PHOTO_SIZES_HALF} />
					<source type="image/webp" srcset={photoSrcset(tier.img.slug, tier.img.n, 'webp')} sizes={PHOTO_SIZES_HALF} />
					<img
						src={photoFallback(tier.img.slug, tier.img.n)}
						srcset={photoSrcset(tier.img.slug, tier.img.n, 'jpg')}
						sizes={PHOTO_SIZES_HALF}
						alt={tier.sqft}
						loading="lazy"
						decoding="async"
						class="w-full h-full object-cover"
					/>
				</picture>
			</div>
			<div class="flex flex-col justify-center px-8 md:px-14 py-14 {i % 2 === 1 ? 'md:order-1' : ''}">
				<p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-4">{tier.sqft}</p>
				<div class="flex flex-col gap-4 mb-8">
					{#each tier.services as service}
						<div class="flex items-center justify-between border-b border-gray-100 pb-4">
							<span class="text-base font-light" style="font-family: var(--font-serif)">{service.name}</span>
							<span class="text-base font-light">{service.price}</span>
						</div>
					{/each}
				</div>
				<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs w-fit px-8">INQUIRE</a>
			</div>
		</div>
	{/each}
</section>


<!-- ADD-ONS -->
<section class="px-8 lg:px-20 pb-24 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-6">Add-Ons</p>
	<div class="flex items-center justify-between border-t border-b border-gray-100 py-6 gap-6">
		<div>
			<p class="text-base font-light" style="font-family: var(--font-serif)">Virtual Staging</p>
			<p class="text-xs text-gray-500 mt-1 max-w-md">Digitally furnish empty rooms so vacant listings feel like a home buyers can picture themselves in.</p>
		</div>
		<a href="/contact" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity whitespace-nowrap">Inquire for Pricing</a>
	</div>
</section>

<!-- FAQ -->
<section class="py-24 px-8 lg:px-20 max-w-4xl mx-auto text-center">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Common Questions</p>
	<h2 class="text-3xl md:text-4xl font-light mb-6" style="font-family: var(--font-serif)">Have Questions?</h2>
	<p class="text-sm text-gray-500 max-w-md mx-auto leading-relaxed mb-8">
		Turnaround times, what's included, payment, service area, and more — we've answered the questions we hear most.
	</p>
	<a href="/faq" class="btn btn-neutral rounded-none tracking-widest text-xs px-10">READ THE FAQ</a>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Ready to Book?</h2>
	<p class="text-sm text-white/70 mb-8 max-w-md mx-auto">Have a property in mind? Reach out and we'll get you on the calendar.</p>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">BOOK A SHOOT</a>
</section>
