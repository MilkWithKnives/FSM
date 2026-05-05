<script lang="ts">
	import { inView } from '$lib/actions/inView';

	const listings = [
		{
			address: 'Hagadorn Rd',
			area: 'East Lansing',
			tag: 'Photos + Video',
			img: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80&auto=format&fit=crop',
		},
		{
			address: 'Hamilton Rd',
			area: 'Okemos',
			tag: 'Photos',
			img: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80&auto=format&fit=crop',
		},
		{
			address: 'Oriole Ln',
			area: 'East Lansing',
			tag: 'Photos + Video',
			img: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&q=80&auto=format&fit=crop',
		},
	];

	const services = [
		{
			title: 'Photography',
			description: 'High-resolution, fully edited images that capture every detail — from wide-angle architectural shots to intimate interior moments.',
			img: 'https://images.unsplash.com/photo-1613977257592-4871e5fcd7c4?w=700&q=80&auto=format&fit=crop',
			href: '/photos',
		},
		{
			title: 'Video Tours',
			description: 'Cinematic property walkthroughs that immerse buyers in the experience before they ever set foot inside.',
			img: 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=700&q=80&auto=format&fit=crop',
			href: '/videos',
		},
		{
			title: 'Aerial Drone',
			description: "Stunning bird's-eye perspectives that showcase location, lot size, and surrounding amenities.",
			img: 'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=700&q=80&auto=format&fit=crop',
			href: '/pricing',
		},
	];

	const press = ['Architectural Digest', 'Wall Street Journal', 'Lansing State Journal', 'Robb Report'];
</script>

<svelte:head>
	<title>Full Scope Media LLC | Real Estate Photography & Video · East Lansing, MI</title>
	<meta name="description" content="Full Scope Media LLC elevates real estate listings through professional photography, cinematic video tours, and aerial drone services across East Lansing, Lansing, and Metro Detroit." />
	<meta property="og:title" content="Full Scope Media LLC | Real Estate Photography & Video" />
	<meta property="og:description" content="Elevating real estate listings through exceptional photography, video, and drone services in East Lansing, MI." />
</svelte:head>

<!-- HERO -->
<section class="relative h-[100dvh] min-h-[500px] overflow-hidden">
	<img
		src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1800&q=85&auto=format&fit=crop"
		alt="Luxury property exterior"
		fetchpriority="high"
		class="absolute inset-0 w-full h-full object-cover scale-105 transition-transform duration-[8s] ease-out"
		style="animation: heroZoom 8s ease forwards;"
	/>
	<div class="absolute inset-0 bg-black/35 flex flex-col items-center justify-center text-white text-center px-5">
		<p class="hero-line-1 text-xs tracking-[0.4em] uppercase mb-5 opacity-80">Real Estate Media Studio · East Lansing, MI</p>
		<h1 class="hero-line-2 text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-light max-w-3xl leading-tight" style="font-family: var(--font-serif)">
			Passionate about telling your home's story.
		</h1>
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
		{#each listings as listing, i}
			<a href="/portfolio" class="group block" use:inView={{ delay: i * 120 }}>
				<div class="reveal overflow-hidden aspect-[4/5] mb-3">
					<img
						src={listing.img}
						alt="{listing.address}, {listing.area}"
						loading="lazy"
						class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
					/>
				</div>
				<p class="reveal text-base font-light" style="font-family: var(--font-serif)">{listing.address}</p>
				<p class="text-sm text-gray-500">{listing.area} · {listing.tag}</p>
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
			<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-3">What We Offer</p>
			<h2 class="text-3xl md:text-5xl font-light" style="font-family: var(--font-serif)">Our Services</h2>
		</div>
		<div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-10">
			{#each services as service, i}
				<div class="group reveal" use:inView={{ delay: i * 150 }}>
					<div class="overflow-hidden aspect-[4/3] mb-5">
						<img
							src={service.img}
							alt="Real estate {service.title.toLowerCase()} by Full Scope Media LLC"
							loading="lazy"
							class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
					</div>
					<h3 class="text-xl md:text-2xl font-light mb-2" style="font-family: var(--font-serif)">{service.title}</h3>
					<p class="text-sm text-gray-500 leading-relaxed mb-4">{service.description}</p>
					<a href={service.href} class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity">Learn More</a>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- FULL-BLEED QUOTE -->
<section class="relative h-[50vh] md:h-[60vh] min-h-[300px] overflow-hidden">
	<img
		src="https://images.unsplash.com/photo-1613977257363-707ba9348227?w=1800&q=85&auto=format&fit=crop"
		alt="Luxury interior"
		loading="lazy"
		class="absolute inset-0 w-full h-full object-cover"
	/>
	<div class="absolute inset-0 bg-black/30 flex items-center justify-center px-5">
		<blockquote class="text-white text-center max-w-2xl reveal" use:inView>
			<p class="text-2xl sm:text-3xl md:text-5xl font-light italic" style="font-family: var(--font-serif)">"Every property has a story worth telling beautifully."</p>
		</blockquote>
	</div>
</section>

<!-- AS SEEN IN -->
<section class="py-16 md:py-20 px-5 border-b border-gray-100">
	<div class="max-w-5xl mx-auto text-center">
		<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-8 reveal" use:inView>Our Work As Seen In</p>
		<div class="flex flex-wrap items-center justify-center gap-6 md:gap-12">
			{#each press as pub, i}
				<p class="text-xs md:text-sm tracking-widest uppercase text-gray-400 font-light reveal" use:inView={{ delay: i * 100 }} style="font-family: var(--font-serif)">{pub}</p>
			{/each}
		</div>
	</div>
</section>

<!-- ABOUT TEASER -->
<section class="py-16 md:py-24 px-5 md:px-10 lg:px-20 max-w-7xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-16 items-center">
		<div class="order-2 md:order-1 reveal" use:inView>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-5">About Full Scope Media</p>
			<h2 class="text-3xl md:text-4xl lg:text-5xl font-light leading-snug mb-6" style="font-family: var(--font-serif)">
				We take pride in the value we bring to your properties.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-4">
				At Full Scope Media, we are a full-service real estate media studio. We work alongside agents, developers, and homeowners across East Lansing and greater Michigan to create imagery that moves markets.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-8">
				Great photography doesn't just document a property — it sells a lifestyle.
			</p>
			<a href="/about" class="btn btn-neutral rounded-none tracking-widest text-xs px-8 hover:scale-105 transition-transform duration-200">MEET THE TEAM</a>
		</div>
		<div class="overflow-hidden aspect-[4/5] order-1 md:order-2 reveal-scale" use:inView>
			<img
				src="https://images.unsplash.com/photo-1449844908441-8829872d2607?w=900&q=85&auto=format&fit=crop"
				alt="Luxury property at dusk"
				loading="lazy"
				class="w-full h-full object-cover"
			/>
		</div>
	</div>
</section>

<!-- NEWSLETTER -->
<section class="bg-gray-50 py-16 md:py-20 px-5 text-center">
	<div class="reveal" use:inView>
		<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-3">Stay In Touch</p>
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
