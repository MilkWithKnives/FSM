<script lang="ts">
 import { rate, priceLabel } from '$lib/pricing';
</script>
<section class="py-16 px-8 lg:px-20 max-w-6xl mx-auto">
 <p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">One photographer, direct contact</p>
 <h2 class="text-3xl md:text-4xl font-light mb-6" style="font-family: var(--font-serif)">A straightforward shoot, from first call to delivery.</h2>
 <p class="text-sm text-gray-600 leading-relaxed max-w-2xl">You speak directly with the person photographing your property. I deliver photos within 24 hours and work with you on scheduling. Tell me about unusual requests or last-minute additions so we can work through what the property needs.</p>
 <p class="text-sm text-gray-600 mt-4">Basic residential photos start at {priceLabel(rate('basic'))}, with a CubiCasa floor plan included. {rate('basic').qualifier}</p>
 <a href="tel:+19895257768" class="inline-block mt-6 text-sm underline underline-offset-4">Call me at (989) 525-7768</a>
</section>
