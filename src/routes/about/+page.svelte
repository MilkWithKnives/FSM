<svelte:head>
	<title>About Us | Full Scope Media LLC · Luxury Real Estate Media</title>
	<meta name="description" content="Meet the Full Scope Media LLC team — experienced real estate photographers and media professionals serving East Lansing, Lansing, and greater Michigan." />
	<meta property="og:title" content="About Us | Full Scope Media LLC" />
	<meta property="og:description" content="Meet the Full Scope Media LLC team — experienced real estate photographers serving East Lansing, MI." />
</svelte:head>

<script lang="ts">
	const team = [
		{
			name: 'Angela R.',
			role: 'Luxury Interior Photographer',
			bio: 'Specializing in capturing the warmth and flow of luxury interiors, Angela brings over 12 years of editorial experience to every shoot.',
			img: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=600&q=80&auto=format&fit=crop&crop=face',
		},
		{
			name: 'Michelle K.',
			role: 'Architectural Photographer',
			bio: 'A Michigan-based photographer with more than 15 years of experience documenting high-end residential architecture.',
			img: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=600&q=80&auto=format&fit=crop&crop=face',
		},
		{
			name: 'Brittany M.',
			role: 'Operations Manager',
			bio: 'Brittany brings 10 years of operations expertise to Full Scope Media, ensuring every shoot runs seamlessly from booking to delivery.',
			img: 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=600&q=80&auto=format&fit=crop&crop=face',
		},
	];
</script>

<!-- HERO -->
<section class="relative h-[55vh] overflow-hidden">
	<img
		src="https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1800&q=85&auto=format&fit=crop"
		alt="Our studio"
		class="absolute inset-0 w-full h-full object-cover"
	/>
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
		<div class="grid grid-cols-2 gap-4">
			<div class="overflow-hidden aspect-[3/4] mt-12">
				<img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&q=80&auto=format&fit=crop&crop=face" alt="Arturo" class="w-full h-full object-cover" />
			</div>
			<div class="overflow-hidden aspect-[3/4]">
				<img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=600&q=80&auto=format&fit=crop&crop=face" alt="Lauren" class="w-full h-full object-cover" />
			</div>
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

<!-- TEAM -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-4 text-center">The People Behind the Lens</p>
	<h2 class="text-3xl md:text-4xl font-light text-center mb-16" style="font-family: var(--font-serif)">Meet the Team</h2>
	<div class="grid grid-cols-1 md:grid-cols-3 gap-10">
		{#each team as member}
			<div>
				<div class="overflow-hidden aspect-[3/4] mb-6">
					<img src={member.img} alt={member.name} class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-500" />
				</div>
				<h3 class="text-xl font-light mb-1" style="font-family: var(--font-serif)">{member.name}</h3>
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-3">{member.role}</p>
				<p class="text-sm text-gray-500 leading-relaxed">{member.bio}</p>
			</div>
		{/each}
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Let's Create Something Together</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">INQUIRE NOW</a>
</section>
