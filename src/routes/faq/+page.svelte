<script lang="ts">
	import Seo from '$lib/Seo.svelte';

	const faqs = [
		{
			q: 'How quickly will I receive my photos?',
			a: 'We guarantee a 24-hour turnaround — your edited photos are delivered within 24 hours of your shoot via an online gallery. Same-day rush delivery is also available upon request for an additional fee.',
		},
		{
			q: 'What is included in each shoot?',
			a: 'Each photography package includes 1 location, a 2–2.5 hour shoot, and 40 fully edited, high-resolution photos delivered in web and print formats.',
		},
		{
			q: 'Do you offer video tours, aerial drone, and Matterport 3D?',
			a: 'Yes. Alongside photography we offer cinematic video tours, FAA-licensed aerial drone footage, floor plans, virtual staging, and Matterport 3D walkthroughs. These can be booked individually or bundled — see our Pricing page for package details.',
		},
		{
			q: 'How should I prepare the property for the shoot?',
			a: 'Declutter surfaces, turn on all interior lights, open blinds for natural light, and tuck away personal items, cords, and pet bowls. A little staging goes a long way — arriving to a camera-ready home means we can focus on capturing it at its best.',
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
			q: 'What are the usage rights for my photos?',
			a: 'You receive a license to use the images to market the photographed property across MLS, social media, print, and web for the duration of the listing. Full Scope Media LLC retains copyright. Reach out if you need extended or commercial usage rights.',
		},
		{
			q: 'What payment methods do you accept?',
			a: 'We accept all major credit cards, Zelle, and ACH bank transfer. Payment is due within 3 days of image delivery.',
		},
		{
			q: 'Do you shoot outside of East Lansing?',
			a: 'Absolutely. Our service area spans greater Michigan — Lansing, Okemos, Grand Ledge, and across Mid-Michigan to Bay City, Saginaw, and Midland, as well as Ann Arbor and the Metro Detroit area. We travel for larger projects — contact us to discuss any travel fees.',
		},
	];

	let openFaq = $state<number | null>(null);
</script>

<Seo
	title="FAQ | Full Scope Media LLC · Real Estate Photography East Lansing, MI"
	description="Answers to common questions about Full Scope Media LLC's real estate photography and video — turnaround times, what's included, service area, payment, and more. Serving East Lansing and greater Michigan."
	ogTitle="FAQ | Full Scope Media LLC"
	ogDescription="Common questions about real estate photography and video with Full Scope Media LLC — turnaround, pricing, service area, and more."
/>

<!-- FAQPage structured data for rich results -->
{@html `<script type="application/ld+json">${JSON.stringify({
	'@context': 'https://schema.org',
	'@type': 'FAQPage',
	mainEntity: faqs.map((f) => ({
		'@type': 'Question',
		name: f.q,
		acceptedAnswer: { '@type': 'Answer', text: f.a },
	})),
})}<\/script>`}

<!-- HEADER -->
<section class="pt-20 pb-4 px-8 lg:px-20 max-w-4xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Common Questions</p>
	<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">FAQ</h1>
</section>

<!-- INTRO -->
<section class="px-8 lg:px-20 pb-12 max-w-4xl mx-auto">
	<p class="text-sm text-gray-500 max-w-xl leading-relaxed mt-4">
		Everything you need to know about working with us — from turnaround times to what's included. Don't see your question? <a href="/contact" class="border-b border-black pb-0.5 hover:opacity-60 transition-opacity">Get in touch</a> and we'll be happy to help.
	</p>
</section>

<!-- FAQ ACCORDION -->
<section class="px-8 lg:px-20 pb-24 max-w-4xl mx-auto">
	<div class="flex flex-col">
		{#each faqs as faq, i}
			<div class="border-t border-gray-100 {i === faqs.length - 1 ? 'border-b' : ''}">
				<button
					class="w-full flex items-center justify-between py-5 text-left"
					onclick={() => openFaq = openFaq === i ? null : i}
				>
					<span class="text-base font-light pr-8" style="font-family: var(--font-serif)">{faq.q}</span>
					<span class="text-gray-500 text-lg flex-shrink-0">{openFaq === i ? '−' : '+'}</span>
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
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Still Have Questions?</h2>
	<p class="text-sm text-white/70 mb-8 max-w-md mx-auto">We're happy to walk you through anything. Reach out and we'll get you everything you need.</p>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
