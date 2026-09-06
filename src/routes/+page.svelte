<script lang="ts">
	import Seo from '$lib/Seo.svelte';
</script>

<Seo
	title="Full Scope Media — Real Estate Photography & Web Studio · East Lansing, MI"
	description="Full Scope Media is an East Lansing, MI media studio: real estate photography, video and 3D tours for listings — plus web design, SEO, and systems integration for small businesses across Michigan."
/>

<!-- The eye gate (rendered by the root layout) covers this page; this content exists
     for crawlers and no-JS visitors, and mirrors the gate's two destinations. -->
<main class="gateway">
	<h1>Full Scope Media</h1>
	<p>
		An East Lansing, Michigan media studio. Pick a side of the house: real estate photography,
		video, aerial drone and 3D tours for listings — or the studio: web design &amp; build, SEO,
		and the systems that tie a small business together.
	</p>
	<ul>
		<li><a href="/real-estate-photography">Real Estate Media — photography, video &amp; 3D tours for listings</a></li>
		<li><a href="/studio">Studio — web design, SEO &amp; systems for small businesses</a></li>
		<li><a href="/studio/web-design">Custom web design for Lansing and East Lansing businesses</a></li>
	</ul>
</main>

<style>
	.gateway {
		min-height: 100dvh;
		display: flex;
		flex-direction: column;
		justify-content: center;
		gap: 18px;
		padding: 48px clamp(20px, 6vw, 80px);
		background: #1f1d1b;
		color: #ecebe9;
		font-family: var(--font-studio, monospace);
	}
	h1 {
		font-family: var(--font-studio, monospace);
		font-size: clamp(28px, 4vw, 48px);
		font-weight: 700;
		letter-spacing: 0.08em;
	}
	p {
		max-width: 620px;
		line-height: 1.6;
		font-size: 15px;
		color: #b6b3af;
	}
	ul {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}
	a {
		color: #ecebe9;
		text-decoration: underline;
		text-underline-offset: 4px;
	}
	a:hover {
		color: #ff5a00;
	}
</style>
