<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { journalPosts } from '$lib/journal';
</script>

<Seo
	title="Journal | Full Scope Media LLC · Real Estate Photography Tips & Insights"
	description="Tips, guides, and insights from the Full Scope Media LLC team — covering staging, photography techniques, listing preparation, and the Michigan real estate market."
	ogDescription="Real estate photography tips, staging guides, and insights from the Full Scope Media LLC team."
/>

<!-- HEADER -->
<section class="pt-20 pb-16 px-8 lg:px-20 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Insights & Ideas</p>
	<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Journal</h1>
	<p class="text-sm text-gray-500 mt-6 max-w-md leading-relaxed">Tips, stories, and resources from the Full Scope Media team — for agents, developers, and anyone passionate about beautiful spaces.</p>
</section>

<!-- POSTS GRID -->
<section class="px-8 lg:px-20 pb-28 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-16">
		{#each journalPosts as post (post.slug)}
			<article class="group">
				<a href="/journal/{post.slug}" class="block overflow-hidden aspect-[16/10] mb-6">
					<img
						src={post.image.src}
						alt={post.image.alt}
						width={post.image.width}
						height={post.image.height}
						loading="lazy"
						decoding="async"
						class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
					/>
				</a>
				<h2 class="text-2xl font-light mb-3 leading-snug" style="font-family: var(--font-serif)">
					<a href="/journal/{post.slug}" class="hover:opacity-60 transition-opacity">{post.title}</a>
				</h2>
				<p class="text-sm text-gray-500 leading-relaxed mb-5">{post.excerpt}</p>
				<a href="/journal/{post.slug}" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity">Read More<span class="sr-only">: {post.title}</span></a>
			</article>
		{/each}
	</div>
</section>

<!-- NEWSLETTER -->
<section class="bg-gray-50 py-20 px-8 text-center border-t border-gray-100">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Never Miss a Post</p>
	<h2 class="text-3xl font-light mb-6" style="font-family: var(--font-serif)">Stay Up To Date</h2>
	<form class="flex flex-col sm:flex-row gap-0 max-w-md mx-auto" onsubmit={(e) => e.preventDefault()}>
		<input
			type="email"
			placeholder="Your email address"
			class="input input-bordered rounded-none flex-1 border-gray-300 focus:outline-none focus:border-black text-sm"
		/>
		<button type="submit" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">SUBSCRIBE</button>
	</form>
</section>
