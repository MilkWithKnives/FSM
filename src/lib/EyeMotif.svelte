<script lang="ts">
 import EyeArtwork from '$lib/EyeArtwork.svelte';
 let { size = 'small', intensity = 'subtle' }: { size?: 'small' | 'large'; intensity?: 'subtle' | 'full' } = $props();
</script>
<svg class="motif" viewBox="238 267 98 59" width={size === 'large' ? 196 : 64} height={size === 'large' ? 118 : 39} aria-hidden="true" style:opacity={intensity === 'subtle' ? 0.45 : 1}>
 <EyeArtwork />
</svg>

<style>
 .motif:hover :global(.iris) { transform: translate(2px, 0) !important; }
 @media (prefers-reduced-motion: reduce) { .motif:hover :global(.iris) { transform: none !important; } }
</style>
