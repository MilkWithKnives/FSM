<script lang="ts">
 import { publishedTestimonials } from '$lib/testimonials';
 import { getProperty } from '$lib/properties';
 let { city }: { city?: string } = $props();
 const items = $derived(publishedTestimonials.filter(item => !city || item.city === city));
</script>
{#if items.length}
<section class="py-20 px-8 lg:px-20 max-w-6xl mx-auto" aria-label="Client testimonials">
 <p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-8">From clients</p>
 <div class="grid md:grid-cols-2 gap-12">
 {#each items as item}
 <figure class="border-t border-gray-100 pt-8">
  <blockquote class="text-2xl font-light leading-relaxed" style="font-family: var(--font-serif)">{item.quote}</blockquote>
  <figcaption class="text-sm text-gray-600 mt-6">{item.clientName} · {item.role} · {item.city}
   {#if item.propertySlug && getProperty(item.propertySlug)}<a href="/portfolio/{item.propertySlug}" class="block mt-3 underline underline-offset-4">View the property</a>{/if}
  </figcaption>
 </figure>
 {/each}
 </div>
</section>
{/if}
