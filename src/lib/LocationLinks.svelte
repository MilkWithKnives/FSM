<script lang="ts">
 import { locations } from '$lib/locations';
 let { current = '' }: { current?: string } = $props();
 const nearby = $derived(locations.filter(location => location.slug !== current));
</script>
<section class="px-8 lg:px-20 py-12 max-w-6xl mx-auto">
 <p class="text-sm text-gray-600 leading-relaxed">
  See delivered local work in
  {#each nearby as location, i}{#if i > 0} and {/if}<a class="underline underline-offset-4" href="/real-estate-photographer/{location.slug}">{location.city}</a>{/each}.
  Each gallery shows a real property photographed by Full Scope Media.
 </p>
</section>
