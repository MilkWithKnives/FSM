<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { enhance } from '$app/forms';

	let { form: actionResult } = $props();

	let services = $state<string[]>([]);

	const serviceOptions = [
		'Web design & build',
		'SEO',
		'Photography',
		'Systems & data',
		'Not sure yet',
	];

	function toggleService(service: string) {
		if (services.includes(service)) {
			services = services.filter((s) => s !== service);
		} else {
			services = [...services, service];
		}
	}
</script>

<Seo
	title="Start a Project — Studio | Full Scope Media · East Lansing, MI"
	description="Start a project with Full Scope Media's studio: web design & build, local SEO, brand photography, and systems integration for small businesses in East Lansing and across Michigan. Tell us what you're building."
/>

<!-- HEADER -->
<section class="st-frame">
	<span class="st-cross bl"></span><span class="st-cross br"></span>
	<div class="st-pad st-hero header">
		<p class="st-kicker">Contact · Studio</p>
		<h1 class="st-h1">Tell us what <span class="st-dim">you're building.</span></h1>
		<p class="st-body">
			A website, a rebrand, a stack of tools that won't cooperate — describe it in a couple of
			sentences and we'll follow up within 1–2 business days.
		</p>
	</div>
</section>

<!-- FORM + INFO -->
<section class="grid">
	<div class="form-cell">
		{#if actionResult?.success}
			<div class="success">
				<p class="st-num">✓</p>
				<h2 class="st-h2">Received.</h2>
				<p class="st-body">We've got your inquiry and will be in touch within 1–2 business days.</p>
			</div>
		{:else}
			{#if actionResult?.error}
				<p class="error">{actionResult.error}</p>
			{/if}

			<form method="POST" use:enhance>
				{#each services as s (s)}
					<input type="hidden" name="services" value={s} />
				{/each}

				<div class="pair">
					<div class="field">
						<label for="name">Name *</label>
						<input id="name" name="name" type="text" required placeholder="Jane Smith" />
					</div>
					<div class="field">
						<label for="email">Email *</label>
						<input id="email" name="email" type="email" required placeholder="jane@example.com" />
					</div>
				</div>

				<div class="pair">
					<div class="field">
						<label for="phone">Phone</label>
						<input id="phone" name="phone" type="tel" placeholder="(989) 555-0100" />
					</div>
					<div class="field">
						<label for="business">Business</label>
						<input id="business" name="business" type="text" placeholder="Your business or project name" />
					</div>
				</div>

				<div class="field">
					<p class="label-line">Interested in</p>
					<div class="toggles">
						{#each serviceOptions as service (service)}
							<button
								type="button"
								class="chip"
								class:on={services.includes(service)}
								onclick={() => toggleService(service)}
							>
								{service}
							</button>
						{/each}
					</div>
				</div>

				<div class="field">
					<label for="message">The project *</label>
					<textarea
						id="message"
						name="message"
						rows="6"
						required
						placeholder="What are you building, what's not working today, and what would 'done' look like?"
					></textarea>
				</div>

				<div>
					<button type="submit" class="st-btn st-btn-solid">Send inquiry</button>
				</div>
			</form>
		{/if}
	</div>

	<aside>
		<div class="info-cell">
			<p class="foot-label">Call</p>
			<a href="tel:+19895257768">(989) 525-7768</a>
		</div>
		<div class="info-cell">
			<p class="foot-label">Email</p>
			<a href="mailto:rchampion@fullscope-media.com">rchampion@fullscope-media.com</a>
		</div>
		<div class="info-cell">
			<p class="foot-label">Based in</p>
			<p>East Lansing, Michigan</p>
			<p class="st-dim small">Working with small businesses across Michigan — remote-friendly.</p>
		</div>
		<div class="info-cell">
			<p class="foot-label">Booking a shoot?</p>
			<p class="st-dim small">
				Real estate listings run through the <a class="inline-link" href="/contact">photography side</a> —
				scheduling calendar included.
			</p>
		</div>
	</aside>
</section>

<style>
	.header {
		gap: 18px;
	}

	.grid {
		display: grid;
		grid-template-columns: 1.6fr 1fr;
	}
	.form-cell {
		padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 72px);
		border-right: 1px solid var(--st-line);
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 22px;
		max-width: 640px;
	}
	.pair {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 18px;
	}
	.field {
		display: flex;
		flex-direction: column;
		gap: 7px;
	}
	label,
	.label-line {
		font-size: 10px;
		font-weight: 500;
		letter-spacing: 0.22em;
		text-transform: uppercase;
		color: var(--st-dim);
	}
	input,
	textarea {
		background: transparent;
		border: 1px solid var(--st-line);
		padding: 12px 14px;
		font-family: var(--font-studio);
		font-size: 13px;
		color: var(--st-ink);
		border-radius: 0;
		outline: none;
		transition: border-color 0.2s;
	}
	input::placeholder,
	textarea::placeholder {
		color: #a5a29c;
	}
	input:focus,
	textarea:focus {
		border-color: var(--st-ink);
	}
	textarea {
		resize: none;
	}

	.toggles {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}
	.chip {
		border: 1px solid var(--st-line);
		background: transparent;
		padding: 9px 14px;
		font-family: var(--font-studio);
		font-size: 11px;
		font-weight: 500;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		color: #4c4945;
		cursor: pointer;
		transition: border-color 0.2s, background 0.2s, color 0.2s;
	}
	.chip:hover {
		border-color: var(--st-ink);
		color: var(--st-ink);
	}
	.chip.on {
		background: var(--st-ink);
		border-color: var(--st-ink);
		color: var(--st-bg);
	}

	.error {
		margin-bottom: 22px;
		padding: 14px 16px;
		border: 1px solid var(--st-accent);
		color: var(--st-accent);
		font-size: 13px;
	}
	.success {
		display: flex;
		flex-direction: column;
		gap: 14px;
		padding: clamp(24px, 6vw, 80px) 0;
	}

	aside {
		display: flex;
		flex-direction: column;
	}
	.info-cell {
		padding: 26px clamp(20px, 3vw, 36px);
		border-bottom: 1px solid var(--st-line);
		font-size: 13px;
		line-height: 1.7;
	}
	.info-cell:last-child {
		border-bottom: none;
	}
	.foot-label {
		color: var(--st-dim);
		text-transform: uppercase;
		letter-spacing: 0.22em;
		font-size: 10px;
		margin-bottom: 8px;
	}
	.info-cell a:hover {
		color: var(--st-accent);
	}
	.small {
		font-size: 12px;
	}
	.inline-link {
		text-decoration: underline;
		text-underline-offset: 4px;
	}

	@media (max-width: 860px) {
		.grid {
			grid-template-columns: 1fr;
		}
		.form-cell {
			border-right: none;
			border-bottom: 1px solid var(--st-line);
		}
		.pair {
			grid-template-columns: 1fr;
		}
	}
</style>
