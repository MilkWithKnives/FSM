<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { properties } from '$lib/properties';
	import { photoSrcset, heroFallback, PHOTO_SIZES_FULL } from '$lib/images';

	const heroProperty = properties[3];

	const includes = [
		'Photorealistic digital furniture and decor',
		'Style matched to the home and its likely buyer',
		'Empty, dated, or cluttered rooms transformed',
		'Clear "virtually staged" labeling for MLS compliance',
		'Per-image pricing — stage only the rooms that need it',
		'Delivered within 2–3 business days',
	];
</script>

<Seo
	title="Virtual Staging | Full Scope Media · East Lansing, MI"
	description="Virtual staging for real estate in East Lansing and greater Michigan. Digitally furnish empty rooms so vacant listings feel like home — a fraction of the cost of physical staging. Delivered in 2–3 days."
	ogTitle="Virtual Staging | Full Scope Media"
	ogDescription="Photorealistic virtual staging for vacant listings, serving East Lansing and greater Michigan."
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
			alt="Virtual staging real estate photography"
			fetchpriority="high"
			class="absolute inset-0 w-full h-full object-cover"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Services</p>
		<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Virtual Staging</h1>
	</div>
</section>

<!-- INTRO -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
		<div>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-6">Furnish It Digitally</p>
			<h2 class="text-3xl md:text-4xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
				Help buyers see the home, not the empty room.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-6">
				Empty rooms photograph cold and make spaces look smaller than they are. Virtual staging fills them with photorealistic furniture so buyers can picture themselves living there — without the cost, logistics, or time of physically staging a vacant home.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-10">
				We match the style to the property and its target buyer, and every staged image is clearly labeled as virtually staged to keep your listing MLS-compliant. Stage one hero room or the whole house — it's priced per image.
			</p>
			<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">STAGE A LISTING</a>
		</div>
		<div>
			<p class="text-xs tracking-widest uppercase text-gray-500 mb-6">Every Staging Project Includes</p>
			<ul class="flex flex-col gap-3 mb-10">
				{#each includes as item}
					<li class="flex items-start gap-3 text-sm text-gray-600">
						<span class="text-black mt-1">—</span>
						{item}
					</li>
				{/each}
			</ul>
			<div class="pt-8 border-t border-gray-100">
				<p class="text-xs tracking-widest uppercase text-gray-500 mb-2">Pricing</p>
				<p class="text-3xl font-light" style="font-family: var(--font-serif)">Per image</p>
				<a href="/contact" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity mt-4 inline-block">Inquire for Pricing</a>
			</div>
		</div>
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Turn Empty Rooms Into Homes</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
