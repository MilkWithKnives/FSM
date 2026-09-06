<script lang="ts">
	import './studio.css';
	import { page } from '$app/stores';

	let { children } = $props();

	const navLinks = [
		{ href: '/studio', label: 'Studio' },
		{ href: '/studio/web-design', label: 'Web Design' },
		{ href: '/studio/systems', label: 'Systems' },
		{ href: '/studio/photography', label: 'Photography' },
		{ href: '/studio/faq', label: 'FAQ' },
	];

	function isActive(href: string) {
		return $page.url.pathname === href;
	}
</script>

<div class="studio">
	<!-- HEADER: boxed cells on a hairline bar, black contact block at the end -->
	<header>
		<a href="/studio" class="brand" aria-label="Full Scope Media — Studio">
			<svg viewBox="240 270 94 52" class="mark" aria-hidden="true">
				<path fill="currentColor" d="M286.81,319.69c-12.74,0-27.79-4.58-43.24-19.3l-.68-.65.61-.72c.37-.45,9.35-10.96,24.8-16.38,14.26-5,36.87-6.31,63.55,15.9l.83.69-.74.77c-.43.45-10.78,11.11-26.9,16.6-5.21,1.78-11.38,3.09-18.21,3.09ZM245.65,299.61c18.28,17.07,38.03,22.15,58.72,15.1,13.23-4.51,22.65-12.8,25.33-15.33-20.53-16.76-40.93-21.76-60.67-14.87-12.7,4.43-21.08,12.66-23.38,15.11Z"/>
				<path fill="currentColor" d="M329.94,290.08c-17.93-15.8-37.88-20.62-59.29-14.33-16.04,4.71-26.93,14.23-27.04,14.33l-1.33-1.5c.45-.4,11.28-9.88,27.73-14.73,15.22-4.49,38.2-5.57,61.25,14.73l-1.32,1.5Z"/>
				<circle fill="currentColor" cx="287.22" cy="292.79" r="12.1"/>
			</svg>
			<span class="wordmark">FULL SCOPE MEDIA</span>
		</a>
		<nav aria-label="Studio">
			{#each navLinks as link (link.href)}
				<a href={link.href} class="cell" class:active={isActive(link.href)} aria-current={isActive(link.href) ? 'page' : undefined}>{link.label}</a>
			{/each}
		</nav>
		<a href="/studio/contact" class="contact">Contact</a>
	</header>

	<main>
		{@render children()}
	</main>

	<!-- FOOTER -->
	<footer>
		<div class="foot-cell foot-brand">
			<p>FULL SCOPE MEDIA LLC</p>
			<p class="st-dim">East Lansing, MI · © 2026</p>
		</div>
		<div class="foot-cell">
			<p class="foot-label">Studio</p>
			<ul>
				{#each navLinks as link (link.href)}
					<li><a href={link.href}>{link.label}</a></li>
				{/each}
				<li><a href="/studio/contact">Contact</a></li>
			</ul>
		</div>
		<div class="foot-cell">
			<p class="foot-label">Elsewhere</p>
			<ul>
				<li><a href="/real-estate-photography">Real Estate Media →</a></li>
				<li><a href="/">The Front Door (the eye) →</a></li>
				<li><a href="https://instagram.com/full.scope.media">@full.scope.media</a></li>
			</ul>
		</div>
		<div class="foot-cell">
			<p class="foot-label">Contact</p>
			<ul>
				<li><a href="tel:+19895257768">(989) 525-7768</a></li>
				<li><a href="mailto:rchampion@fullscope-media.com">rchampion@fullscope-media.com</a></li>
			</ul>
		</div>
	</footer>
</div>

<style>
	header {
		position: sticky;
		top: 0;
		z-index: 50;
		display: flex;
		align-items: stretch;
		background: var(--st-bg);
		border-bottom: 1px solid var(--st-line);
		height: 64px;
	}
	.brand {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 0 clamp(14px, 2.5vw, 28px);
		border-right: 1px solid var(--st-line);
	}
	.mark {
		width: 40px;
		color: var(--st-ink);
		flex-shrink: 0;
	}
	.wordmark {
		font-size: 12px;
		font-weight: 700;
		letter-spacing: 0.22em;
		white-space: nowrap;
	}
	nav {
		display: flex;
		align-items: stretch;
		overflow-x: auto;
		scrollbar-width: none;
	}
	nav::-webkit-scrollbar {
		display: none;
	}
	.cell {
		display: flex;
		align-items: center;
		padding: 0 clamp(12px, 2vw, 26px);
		border-right: 1px solid var(--st-line);
		font-size: 12px;
		font-weight: 500;
		letter-spacing: 0.12em;
		white-space: nowrap;
		position: relative;
		transition: color 0.2s;
	}
	.cell:hover {
		color: var(--st-accent);
	}
	/* active cell gets Ionofolio corner brackets */
	.cell.active::before,
	.cell.active::after {
		content: '';
		position: absolute;
		width: 7px;
		height: 7px;
		border-color: var(--st-accent);
		border-style: solid;
	}
	.cell.active::before {
		top: 10px;
		left: 6px;
		border-width: 1px 0 0 1px;
	}
	.cell.active::after {
		bottom: 10px;
		right: 6px;
		border-width: 0 1px 1px 0;
	}
	.contact {
		margin-left: auto;
		display: flex;
		align-items: center;
		padding: 0 clamp(20px, 3.5vw, 44px);
		background: var(--st-ink);
		color: var(--st-bg);
		font-size: 12px;
		font-weight: 700;
		letter-spacing: 0.18em;
		text-transform: uppercase;
		transition: background 0.2s;
	}
	.contact:hover {
		background: var(--st-accent);
		color: #fff;
	}

	main {
		flex: 1;
	}

	footer {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		border-top: 1px solid var(--st-line);
	}
	.foot-cell {
		padding: 26px clamp(16px, 2.5vw, 32px) 32px;
		border-right: 1px solid var(--st-line);
		font-size: 12px;
		line-height: 1.7;
	}
	.foot-cell:last-child {
		border-right: none;
	}
	.foot-brand p:first-child {
		font-weight: 700;
		letter-spacing: 0.18em;
		margin-bottom: 4px;
	}
	.foot-label {
		color: var(--st-dim);
		text-transform: uppercase;
		letter-spacing: 0.22em;
		font-size: 10px;
		margin-bottom: 10px;
	}
	.foot-cell ul {
		display: flex;
		flex-direction: column;
		gap: 6px;
	}
	.foot-cell a:hover {
		color: var(--st-accent);
	}

	@media (max-width: 860px) {
		.wordmark {
			display: none;
		}
		footer {
			grid-template-columns: 1fr 1fr;
		}
		.foot-cell {
			border-bottom: 1px solid var(--st-line);
		}
		.foot-cell:nth-child(even) {
			border-right: none;
		}
	}
	@media (max-width: 520px) {
		.brand {
			padding: 0 12px;
		}
		.mark {
			width: 32px;
		}
		.contact {
			padding: 0 16px;
		}
	}
</style>
