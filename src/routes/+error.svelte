<script lang="ts">
	import { page } from '$app/stores';
	import EyeMotif from '$lib/EyeMotif.svelte';
</script>

<!-- Renders outside both route groups (no nav/footer), so it fills the viewport itself. -->
<section class="min-h-[100dvh] flex flex-col items-center justify-center text-center px-6">
	<EyeMotif size="large" intensity="full" />
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Full Scope Media</p>
	<h1 class="text-6xl md:text-7xl font-light mb-4" style="font-family: var(--font-serif)">{$page.status}</h1>
	<p class="text-sm text-gray-500 mb-8 max-w-sm">
		{$page.error?.message ?? 'Something went wrong. The page you’re looking for can’t be found.'}
	</p>
	<a href="/" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">BACK HOME</a>
</section>
