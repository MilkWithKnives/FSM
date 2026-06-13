<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { inView } from '$lib/actions/inView';
	import { properties, propertyArea } from '$lib/properties';
	import {
		photoSrcset,
		photoFallback,
		heroFallback,
		PHOTO_SIZES_FULL,
		PHOTO_SIZES_GALLERY,
		PHOTO_SIZES_HALF,
	} from '$lib/images';

	const listings = properties.slice(0, 3);
	const heroProperty = properties[0];
	const quoteProperty = properties[1];
	const aboutProperty = properties[2];

	const services = [
		{
			title: 'Photography',
			description:
				'High-resolution, fully edited images that capture every detail — from wide-angle architectural shots to intimate interior moments.',
			slug: properties[2].slug,
			photoIndex: properties[2].selected[2] ?? properties[2].selected[0],
			href: '/photos',
		},
		{
			title: 'Video Tours',
			description:
				'Cinematic property walkthroughs that immerse buyers in the experience before they ever set foot inside.',
			slug: properties[3].slug,
			photoIndex: properties[3].selected[2] ?? properties[3].selected[0],
			href: '/videos',
		},
		{
			title: 'Aerial Drone',
			description:
				"Stunning bird's-eye perspectives that showcase location, lot size, and surrounding amenities.",
			slug: properties[0].slug,
			photoIndex: properties[0].selected[0],
			href: '/pricing',
		},
	];

</script>

<Seo
	title="Real Estate Photographer · East Lansing, MI | Full Scope Media"
	description="Full Scope Media is a professional real estate photographer in East Lansing, MI — photography, cinematic video, aerial drone, floor plans & virtual staging. Edited photos delivered in 24 hours for listings across Greater Lansing."
	ogTitle="East Lansing Real Estate Photographer | Full Scope Media"
	ogDescription="Professional real estate photography, video & drone in East Lansing, MI. Edited photos delivered in 24 hours."
/>

<!-- Preload the LCP hero image so the browser fetches it immediately,
     in parallel with CSS/fonts, instead of discovering it after parse.
     Matches the <picture> AVIF source exactly so there's no double-download. -->
<svelte:head>
	<link
		rel="preload"
		as="image"
		type="image/avif"
		imagesrcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'avif')}
		imagesizes={PHOTO_SIZES_FULL}
		fetchpriority="high"
	/>
</svelte:head>

<!-- HERO -->
<section class="relative h-[100dvh] min-h-[500px] overflow-hidden">
	<picture>
		<source type="image/avif" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'avif')} sizes={PHOTO_SIZES_FULL} />
		<source type="image/webp" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
		<img
			src={heroFallback(heroProperty)}
			srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'jpg')}
			sizes={PHOTO_SIZES_FULL}
			alt="{heroProperty.address}, {propertyArea(heroProperty)}"
			fetchpriority="high"
			class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[8s] ease-out"
			style="animation: heroZoom 8s ease forwards;"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/35 flex flex-col items-center justify-center text-white text-center px-5">
		<p class="hero-line-1 text-xs tracking-[0.4em] uppercase mb-5 opacity-80">Full Scope Media · East Lansing, MI</p>
		<h1 class="hero-line-2 text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-light max-w-3xl leading-tight" style="font-family: var(--font-serif)">
			East Lansing Real Estate Photographer
		</h1>
		<p class="hero-line-2 text-base sm:text-lg md:text-xl font-light max-w-xl leading-relaxed mt-5 opacity-90" style="font-family: var(--font-serif)">
			Passionate about telling your home's story.
		</p>
		<a href="/portfolio" class="hero-line-3 btn btn-outline btn-sm mt-8 rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-8 transition-all duration-300">
			VIEW PORTFOLIO
		</a>
	</div>
	<div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-white opacity-50 hidden sm:flex flex-col items-center gap-2 hero-line-3">
		<span class="text-xs tracking-widest uppercase">Scroll</span>
		<div class="w-px h-6 bg-white/60 animate-bounce" style="animation-duration:2s"></div>
	</div>
</section>

<style>
	@keyframes heroZoom {
		from { transform: scale(1.05); }
		to   { transform: scale(1); }
	}
</style>

<!-- FEATURED LISTINGS -->
<section class="py-16 md:py-24 px-5 md:px-10 lg:px-20 max-w-7xl mx-auto">
	<div class="reveal flex items-end justify-between mb-10 md:mb-14" use:inView>
		<h2 class="text-3xl md:text-5xl font-light" style="font-family: var(--font-serif)">Featured Work</h2>
		<a href="/portfolio" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity hidden sm:block">View All</a>
	</div>
	<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-5 md:gap-6">
		{#each listings as listing, i (listing.slug)}
			<a href="/portfolio/{listing.slug}" class="group block" use:inView={{ delay: i * 120 }}>
				<div class="reveal overflow-hidden aspect-[4/5] mb-3">
					<picture>
						<source type="image/avif" srcset={photoSrcset(listing.slug, listing.selected[0], 'avif')} sizes={PHOTO_SIZES_GALLERY} />
						<source type="image/webp" srcset={photoSrcset(listing.slug, listing.selected[0], 'webp')} sizes={PHOTO_SIZES_GALLERY} />
						<img
							src={photoFallback(listing.slug, listing.selected[0])}
							srcset={photoSrcset(listing.slug, listing.selected[0], 'jpg')}
							sizes={PHOTO_SIZES_GALLERY}
							alt="{listing.address}, {propertyArea(listing)}"
							loading="lazy"
							decoding="async"
							class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
					</picture>
				</div>
				<p class="reveal text-base font-light" style="font-family: var(--font-serif)">{listing.address}</p>
				<p class="text-sm text-gray-500">{propertyArea(listing)} · {listing.tag}</p>
			</a>
		{/each}
	</div>
	<div class="text-center mt-8 sm:hidden">
		<a href="/portfolio" class="text-xs tracking-widest uppercase border-b border-black pb-1">View All Work</a>
	</div>
</section>

<!-- SERVICES -->
<section class="bg-gray-50 py-16 md:py-24 px-5 md:px-10 lg:px-20">
	<div class="max-w-7xl mx-auto">
		<div use:inView class="reveal text-center mb-12 md:mb-16">
			<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-3">What We Offer</p>
			<h2 class="text-3xl md:text-5xl font-light" style="font-family: var(--font-serif)">Our Services</h2>
		</div>
		<div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-10">
			{#each services as service, i (service.title)}
				<div class="group reveal" use:inView={{ delay: i * 150 }}>
					<div class="overflow-hidden aspect-[4/3] mb-5">
						<picture>
							<source type="image/avif" srcset={photoSrcset(service.slug, service.photoIndex, 'avif')} sizes={PHOTO_SIZES_GALLERY} />
							<source type="image/webp" srcset={photoSrcset(service.slug, service.photoIndex, 'webp')} sizes={PHOTO_SIZES_GALLERY} />
							<img
								src={photoFallback(service.slug, service.photoIndex)}
								srcset={photoSrcset(service.slug, service.photoIndex, 'jpg')}
								sizes={PHOTO_SIZES_GALLERY}
								alt="Real estate {service.title.toLowerCase()} by Full Scope Media LLC"
								loading="lazy"
								decoding="async"
								class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
							/>
						</picture>
					</div>
					<h3 class="text-xl md:text-2xl font-light mb-2" style="font-family: var(--font-serif)">{service.title}</h3>
					<p class="text-sm text-gray-500 leading-relaxed mb-4">{service.description}</p>
					<a href={service.href} class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity">Learn More<span class="sr-only"> about real estate {service.title.toLowerCase()}</span></a>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- FULL-BLEED QUOTE -->
<section class="relative h-[50vh] md:h-[60vh] min-h-[300px] overflow-hidden">
	<picture>
		<source type="image/avif" srcset={photoSrcset(quoteProperty.slug, quoteProperty.selected[1] ?? quoteProperty.selected[0], 'avif')} sizes={PHOTO_SIZES_FULL} />
		<source type="image/webp" srcset={photoSrcset(quoteProperty.slug, quoteProperty.selected[1] ?? quoteProperty.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
		<img
			src={photoFallback(quoteProperty.slug, quoteProperty.selected[1] ?? quoteProperty.selected[0])}
			srcset={photoSrcset(quoteProperty.slug, quoteProperty.selected[1] ?? quoteProperty.selected[0], 'jpg')}
			sizes={PHOTO_SIZES_FULL}
			alt="Interior at {quoteProperty.address}"
			loading="lazy"
			decoding="async"
			class="absolute inset-0 w-full h-full object-cover"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/30 flex items-center justify-center px-5">
		<blockquote class="text-white text-center max-w-2xl reveal" use:inView>
			<p class="text-2xl sm:text-3xl md:text-5xl font-light italic" style="font-family: var(--font-serif)">"Every property has a story worth telling beautifully."</p>
		</blockquote>
	</div>
</section>


<!-- ABOUT TEASER -->
<section class="py-16 md:py-24 px-5 md:px-10 lg:px-20 max-w-7xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-16 items-center">
		<div class="order-2 md:order-1 reveal" use:inView>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-5">About Full Scope Media</p>
			<h2 class="text-3xl md:text-4xl lg:text-5xl font-light leading-snug mb-6" style="font-family: var(--font-serif)">
				We take pride in the value we bring to your properties.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-4">
				Full Scope Media is a professional real estate photographer based in East Lansing, MI. We work alongside agents, developers, and homeowners across Greater Lansing and Mid-Michigan to create imagery that moves markets.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-8">
				Great photography doesn't just document a property — it sells a lifestyle.
			</p>
			<a href="/about" class="btn btn-neutral rounded-none tracking-widest text-xs px-8 hover:scale-105 transition-transform duration-200">MEET THE TEAM</a>
		</div>
		<div class="overflow-hidden aspect-[4/5] order-1 md:order-2 reveal-scale" use:inView>
			<picture>
				<source type="image/avif" srcset={photoSrcset(aboutProperty.slug, aboutProperty.selected[0], 'avif')} sizes={PHOTO_SIZES_HALF} />
				<source type="image/webp" srcset={photoSrcset(aboutProperty.slug, aboutProperty.selected[0], 'webp')} sizes={PHOTO_SIZES_HALF} />
				<img
					src={heroFallback(aboutProperty)}
					srcset={photoSrcset(aboutProperty.slug, aboutProperty.selected[0], 'jpg')}
					sizes={PHOTO_SIZES_HALF}
					alt="{aboutProperty.address}, {propertyArea(aboutProperty)}"
					loading="lazy"
					decoding="async"
					class="w-full h-full object-cover"
				/>
			</picture>
		</div>
	</div>
</section>

<!-- NEWSLETTER -->
<section class="bg-gray-50 py-16 md:py-20 px-5 text-center">
	<div class="reveal" use:inView>
		<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-3">Stay In Touch</p>
		<h2 class="text-2xl md:text-4xl font-light mb-6" style="font-family: var(--font-serif)">Stay Up To Date</h2>
		<p class="text-sm text-gray-500 mb-6">Get the latest listings, tips, and studio news.</p>
		<form class="flex flex-col sm:flex-row max-w-md mx-auto" onsubmit={(e) => e.preventDefault()}>
			<input
				type="email"
				placeholder="Your email address"
				class="input input-bordered rounded-none flex-1 border-gray-300 focus:outline-none focus:border-black text-sm transition-colors duration-200"
			/>
			<button type="submit" class="btn btn-neutral rounded-none tracking-widest text-xs px-8 hover:scale-105 transition-transform duration-200">SUBSCRIBE</button>
		</form>
	</div>
</section>

<!-- WORK WITH US CTA -->
<section class="bg-neutral text-white py-20 md:py-28 px-5 text-center">
	<div class="reveal" use:inView>
		<p class="text-xs tracking-[0.4em] uppercase mb-5 opacity-60">Ready to get started?</p>
		<h2 class="text-3xl md:text-5xl lg:text-6xl font-light mb-8" style="font-family: var(--font-serif)">Let's Work Together</h2>
		<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10 transition-all duration-300">GET IN TOUCH</a>
	</div>
</section>
