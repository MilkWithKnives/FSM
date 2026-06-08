<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { properties, propertyArea } from '$lib/properties';
	import { photoSrcset, photoFallback, PHOTO_SIZES_FULL, PHOTO_SIZES_HALF } from '$lib/images';

	const heroProperty = properties[0];

	const aboutPhotoSrcset = (ext: 'avif' | 'webp' | 'jpg') =>
		[800, 1400, 2000].map((w) => `/about/me-${w}.${ext} ${w}w`).join(', ');
</script>

<Seo
	title="About Us | Full Scope Media LLC · Luxury Real Estate Media"
	description="Meet the Full Scope Media LLC team — experienced real estate photographers and media professionals serving East Lansing, Lansing, and greater Michigan."
	ogTitle="About Us | Full Scope Media LLC"
	ogDescription="Meet the Full Scope Media LLC team — experienced real estate photographers serving East Lansing, MI."
/>

<!-- HERO -->
<section class="relative h-[55vh] overflow-hidden">
	<picture>
		<source type="image/avif" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'avif')} sizes={PHOTO_SIZES_FULL} />
		<source type="image/webp" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
		<img
			src={photoFallback(heroProperty.slug, heroProperty.selected[0])}
			srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'jpg')}
			sizes={PHOTO_SIZES_FULL}
			alt="{heroProperty.address}, {propertyArea(heroProperty)}"
			fetchpriority="high"
			class="absolute inset-0 w-full h-full object-cover"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Our Story</p>
		<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">About Us</h1>
	</div>
</section>

<!-- FOUNDERS INTRO -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
		<div>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-6">Based in East Lansing, Michigan</p>
			<h2 class="text-4xl md:text-5xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
				At Full Scope Media, we take pride in our work and the added value we bring to your properties.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-4">
				Full Scope Media LLC is a real estate media studio with a singular mission: to create photography that doesn't just show a home — it makes people fall in love with it.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-8">
				Based in East Lansing, we serve agents, developers, and homeowners across Michigan — from Lansing and Okemos to Grand Ledge and Metro Detroit.
			</p>
			<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">WORK WITH US</a>
		</div>
		<div class="overflow-hidden aspect-[4/5]">
			<picture>
				<source type="image/avif" srcset={aboutPhotoSrcset('avif')} sizes={PHOTO_SIZES_HALF} />
				<source type="image/webp" srcset={aboutPhotoSrcset('webp')} sizes={PHOTO_SIZES_HALF} />
				<img
					src="/about/me-1400.jpg"
					srcset={aboutPhotoSrcset('jpg')}
					sizes={PHOTO_SIZES_HALF}
					alt="Founder, Full Scope Media LLC"
					loading="lazy"
					decoding="async"
					class="w-full h-full object-cover"
				/>
			</picture>
		</div>
	</div>
</section>

<!-- VALUES -->
<section class="bg-gray-50 py-20 px-8 lg:px-20">
	<div class="max-w-6xl mx-auto">
		<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-4 text-center">What Drives Us</p>
		<h2 class="text-3xl md:text-4xl font-light text-center mb-16" style="font-family: var(--font-serif)">Our Values</h2>
		<div class="grid grid-cols-1 md:grid-cols-3 gap-10">
			<div class="text-center">
				<p class="text-4xl font-light mb-4" style="font-family: var(--font-serif)">01</p>
				<h3 class="text-xl font-light mb-3" style="font-family: var(--font-serif)">Artistry First</h3>
				<p class="text-sm text-gray-500 leading-relaxed">Every image is crafted with the same care as editorial photography — because your listing deserves nothing less.</p>
			</div>
			<div class="text-center">
				<p class="text-4xl font-light mb-4" style="font-family: var(--font-serif)">02</p>
				<h3 class="text-xl font-light mb-3" style="font-family: var(--font-serif)">Reliability</h3>
				<p class="text-sm text-gray-500 leading-relaxed">We show up on time, deliver on deadline, and communicate clearly — so you can focus on closing the deal.</p>
			</div>
			<div class="text-center">
				<p class="text-4xl font-light mb-4" style="font-family: var(--font-serif)">03</p>
				<h3 class="text-xl font-light mb-3" style="font-family: var(--font-serif)">Partnership</h3>
				<p class="text-sm text-gray-500 leading-relaxed">We think of ourselves as an extension of your team — invested in your success as much as our own craft.</p>
			</div>
		</div>
	</div>
</section>


<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Let's Create Something Together</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">INQUIRE NOW</a>
</section>
