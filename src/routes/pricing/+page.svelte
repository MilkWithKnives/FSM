<svelte:head>
	<title>Pricing | Full Scope Media LLC · Real Estate Photography Packages East Lansing, MI</title>
	<meta name="description" content="Transparent real estate photography and video pricing by property size. Packages starting at $480 for photography, $480 for video. Serving East Lansing and greater Michigan." />
	<meta property="og:title" content="Pricing | Full Scope Media LLC" />
	<meta property="og:description" content="Real estate photography packages starting at $480. Transparent pricing by property size, serving East Lansing, MI." />
</svelte:head>

<script lang="ts">
	const tiers = [
		{
			sqft: '1,000 – 1,999 sqft',
			img: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&q=80&auto=format&fit=crop',
			services: [
				{ name: 'Photography', price: '$480' },
				{ name: 'Video Tour', price: '$480' },
				{ name: 'Floorplan', price: '$200' },
				{ name: 'Matterport 3D', price: '$300' },
			],
		},
		{
			sqft: '2,000 – 2,999 sqft',
			img: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=900&q=80&auto=format&fit=crop',
			services: [
				{ name: 'Photography', price: '$520' },
				{ name: 'Video Tour', price: '$980' },
				{ name: 'Floorplan', price: '$300' },
				{ name: 'Matterport 3D', price: '$400' },
			],
		},
		{
			sqft: '3,000 – 3,999 sqft',
			img: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=900&q=80&auto=format&fit=crop',
			services: [
				{ name: 'Photography', price: '$600' },
				{ name: 'Video Tour', price: '$1,100' },
				{ name: 'Floorplan', price: '$350' },
				{ name: 'Matterport 3D', price: '$500' },
			],
		},
		{
			sqft: '4,000 – 4,999 sqft',
			img: 'https://images.unsplash.com/photo-1449844908441-8829872d2607?w=900&q=80&auto=format&fit=crop',
			services: [
				{ name: 'Photography', price: '$720' },
				{ name: 'Video Tour', price: '$1,400' },
				{ name: 'Floorplan', price: '$400' },
				{ name: 'Matterport 3D', price: '$600' },
			],
		},
	];

	const faqs = [
		{
			q: 'How quickly will I receive my photos?',
			a: 'Edited photos are delivered within 24–48 hours of your shoot via an online gallery. Rush delivery (same day) is available upon request for an additional fee.',
		},
		{
			q: 'What is included in each shoot?',
			a: 'Each photography package includes 1 location, a 2–2.5 hour shoot, and 40 fully edited, high-resolution photos delivered in web and print formats.',
		},
		{
			q: 'What if I need to reschedule?',
			a: 'We understand schedules change. Reschedules are accepted up to 48 hours before the shoot at no charge. Cancellations within 24 hours may incur a fee.',
		},
		{
			q: 'Do you offer packages for larger properties over 5,000 sqft?',
			a: 'Absolutely. For estates over 5,000 sqft or multi-location shoots, please contact us for a custom quote.',
		},
		{
			q: 'What payment methods do you accept?',
			a: 'We accept all major credit cards, Zelle, and ACH bank transfer. Payment is due within 3 days of image delivery.',
		},
		{
			q: 'Do you shoot outside of East Lansing?',
			a: 'Our primary service area is greater Michigan — including Lansing, Okemos, and Metro Detroit. We do travel for larger projects — contact us to discuss travel fees.',
		},
	];

	let openFaq = $state<number | null>(null);
</script>

<!-- HEADER -->
<section class="pt-20 pb-4 px-8 lg:px-20 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-4">Transparent Pricing</p>
	<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Pricing</h1>
</section>

<!-- INTRO -->
<section class="px-8 lg:px-20 pb-16 max-w-6xl mx-auto">
	<p class="text-sm text-gray-500 max-w-xl leading-relaxed mt-4">
		All packages include 1 location, a 2–2.5 hour shoot, and 40 fully edited photos delivered within 24–48 hours. Custom packages available for larger estates.
	</p>
</section>

<!-- PRICING TIERS -->
<section class="px-8 lg:px-20 pb-28 max-w-6xl mx-auto flex flex-col gap-0">
	{#each tiers as tier, i}
		<div class="grid grid-cols-1 md:grid-cols-2 gap-0 border-t border-gray-100 {i === tiers.length - 1 ? 'border-b' : ''}">
			<div class="overflow-hidden aspect-[16/10] {i % 2 === 1 ? 'md:order-2' : ''}">
				<img src={tier.img} alt={tier.sqft} class="w-full h-full object-cover" />
			</div>
			<div class="flex flex-col justify-center px-8 md:px-14 py-14 {i % 2 === 1 ? 'md:order-1' : ''}">
				<p class="text-xs tracking-[0.3em] uppercase text-gray-400 mb-4">{tier.sqft}</p>
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

<!-- AS SEEN IN -->
<section class="bg-gray-50 py-20 px-8 border-y border-gray-100">
	<div class="max-w-5xl mx-auto text-center">
		<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-10">Our Work As Seen In</p>
		<div class="flex flex-wrap items-center justify-center gap-12">
			{#each ['Architectural Digest', 'Wall Street Journal', 'Lansing State Journal', 'Robb Report'] as pub}
				<p class="text-sm tracking-widest uppercase text-gray-400 font-light" style="font-family: var(--font-serif)">{pub}</p>
			{/each}
		</div>
	</div>
</section>

<!-- FAQ -->
<section class="py-24 px-8 lg:px-20 max-w-4xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-4 text-center">Common Questions</p>
	<h2 class="text-3xl md:text-4xl font-light text-center mb-14" style="font-family: var(--font-serif)">FAQ</h2>
	<div class="flex flex-col">
		{#each faqs as faq, i}
			<div class="border-t border-gray-100 {i === faqs.length - 1 ? 'border-b' : ''}">
				<button
					class="w-full flex items-center justify-between py-5 text-left"
					onclick={() => openFaq = openFaq === i ? null : i}
				>
					<span class="text-base font-light pr-8" style="font-family: var(--font-serif)">{faq.q}</span>
					<span class="text-gray-400 text-lg flex-shrink-0">{openFaq === i ? '−' : '+'}</span>
				</button>
				{#if openFaq === i}
					<p class="text-sm text-gray-500 leading-relaxed pb-6">{faq.a}</p>
				{/if}
			</div>
		{/each}
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Ready to Book?</h2>
	<p class="text-sm text-white/70 mb-8 max-w-md mx-auto">Have a property in mind? Reach out and we'll get you on the calendar.</p>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">BOOK A SHOOT</a>
</section>
