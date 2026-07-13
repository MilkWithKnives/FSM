<!--
  EyeGate.svelte — the fullscope-media.com front door.

  Adapted from EyeReveal.svelte (standalone eye-blink reveal overlay): instead of a
  single click-to-open cover, the logo's eye idles and follows the cursor behind two
  boxed choice links — one per "site". Picking one blinks the eye shut, navigates
  mid-reveal, and the eye opens onto the chosen destination before removing itself.

  Must be rendered from the root layout (not a page) so it survives the navigation
  that happens partway through the reveal animation.
-->
<script lang="ts">
	import { goto } from '$app/navigation';

	type Choice = { label: string; href: string };

	let {
		choices = [
			{ label: 'Real Estate Media', href: '/real-estate-photography' },
			{ label: 'Studio', href: '/studio' },
		],
		onrevealstart = () => {},
		onrevealend = () => {},
	}: {
		choices?: Choice[];
		onrevealstart?: () => void;
		onrevealend?: () => void;
	} = $props();

	const ink = '#1f1d1b';
	const line = '#ecebe9';

	// unique mask id so two instances never collide
	const uid = 'eyeHole-' + Math.random().toString(36).slice(2, 9);

	let w = $state(typeof window !== 'undefined' ? window.innerWidth : 1920);
	let h = $state(typeof window !== 'undefined' ? window.innerHeight : 1080);

	let phase = $state<'idle' | 'closing' | 'opening' | 'expanding' | 'open'>('idle');
	let wink = $state(false); // playful blink when the eye itself is clicked
	let reduced = $state(false);
	let dx = $state(0),
		dy = $state(0),
		px = $state(0),
		py = $state(0);
	let timers: ReturnType<typeof setTimeout>[] = [];

	$effect(() => {
		reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		// The gate is the whole viewport — no scrolling while it covers the page.
		const prev = document.body.style.overflow;
		document.body.style.overflow = 'hidden';
		return () => {
			document.body.style.overflow = prev;
			timers.forEach(clearTimeout);
		};
	});

	// Eye geometry: the logo almond is ~88 x 46 user units centered at (287.22, 296.5).
	// Scale responsively: ~74% of viewport width, capped by 42% of height.
	const s = $derived(Math.min((w * 0.74) / 88, (h * 0.42) / 46));
	const cx = $derived(w / 2 + dx);
	const cy = $derived(h / 2 + dy);
	// how far the hole must grow to swallow the whole viewport
	const coverScale = $derived(Math.ceil((Math.max(w, h) * 2.6) / (46 * s)));

	function onPointerMove(e: PointerEvent) {
		if (phase !== 'idle') return;
		const fx = Math.max(-0.5, Math.min(0.5, e.clientX / w - 0.5));
		const fy = Math.max(-0.5, Math.min(0.5, e.clientY / h - 0.5));
		dx = Math.round(fx * 2 * 2.75 * s);
		dy = Math.round(fy * 2 * 1.44 * s);
		px = Math.round(fx * 2 * 13 * 10) / 10;
		py = Math.round(fy * 2 * 5.5 * 10) / 10;
	}

	// Clicking the eye itself doesn't navigate — it just blinks back at you.
	function blink() {
		if (phase !== 'idle' || wink || reduced) return;
		wink = true;
		timers.push(setTimeout(() => (wink = false), 170));
	}

	function choose(e: MouseEvent, href: string) {
		e.preventDefault();
		if (phase !== 'idle') return;
		if (reduced) {
			goto(href);
			return;
		}
		dx = dy = px = py = 0;
		phase = 'closing';
		onrevealstart();
		timers.push(
			setTimeout(() => (phase = 'opening'), 130),
			// Navigate the moment the hole starts expanding: the destination renders
			// underneath while the eye is still opening over it.
			setTimeout(() => {
				phase = 'expanding';
				goto(href);
			}, 860),
			setTimeout(() => {
				phase = 'open';
				onrevealend();
			}, 1650)
		);
	}

	const later = $derived(phase === 'expanding' || phase === 'open');

	const hole = $derived(
		later
			? { t: `translate(${cx}px, ${cy}px) scale(${coverScale}, ${coverScale})`, o: 1, trans: 'transform 780ms cubic-bezier(0.6, 0, 0.3, 1)' }
			: phase === 'opening'
				? { t: `translate(${cx}px, ${cy}px) scale(1, 1)`, o: 1, trans: 'transform 430ms cubic-bezier(0.25, 0.65, 0.3, 1)' }
				: { t: `translate(${cx}px, ${cy}px) scale(1, 0.001)`, o: 0, trans: 'transform 0s' }
	);

	const eye = $derived(
		later
			? { t: `translate(${cx}px, ${cy}px) scale(8) scaleY(1)`, o: 0, trans: 'transform 780ms cubic-bezier(0.6, 0, 0.3, 1), opacity 480ms 120ms ease-out' }
			: phase === 'opening'
				? { t: `translate(${cx}px, ${cy}px) scale(1) scaleY(1)`, o: 1, trans: 'transform 430ms cubic-bezier(0.25, 0.65, 0.3, 1)' }
				: phase === 'closing'
					? { t: `translate(${cx}px, ${cy}px) scale(1) scaleY(0.05)`, o: 1, trans: 'transform 120ms ease-in' }
					: { t: `translate(${cx}px, ${cy}px) scale(1) scaleY(${wink ? 0.06 : 1})`, o: 1, trans: 'transform 90ms linear' }
	);

	const irisO = $derived(phase === 'opening' || later ? 0 : 1);
	const chromeO = $derived(phase === 'idle' ? 1 : 0);
</script>

<svelte:window bind:innerWidth={w} bind:innerHeight={h} />

{#if phase !== 'open'}
	<div class="eye-gate">
		<svg
			viewBox="0 0 {w} {h}"
			onpointermove={onPointerMove}
			onclick={blink}
			aria-hidden="true"
		>
			<mask id={uid} maskUnits="userSpaceOnUse" x="0" y="0" width={w} height={h}>
				<rect x="0" y="0" width={w} height={h} fill="#fff" />
				<g style="transform: {hole.t}; transition: {hole.trans}; opacity: {hole.o};">
					<path transform="scale({s}) translate(-287.22 -296.5)" fill="#000"
						d="M245.65,299.61c18.28,17.07,38.03,22.15,58.72,15.1,13.23-4.51,22.65-12.8,25.33-15.33-20.53-16.76-40.93-21.76-60.67-14.87-12.7,4.43-21.08,12.66-23.38,15.11Z" />
				</g>
			</mask>
			<rect x="0" y="0" width={w} height={h} fill={ink} mask="url(#{uid})" />
			<g style="transform: {eye.t}; transition: {eye.trans}; opacity: {eye.o};">
				<g transform="scale({s}) translate(-287.22 -296.5)">
					<path fill={line} d="M286.81,319.69c-12.74,0-27.79-4.58-43.24-19.3l-.68-.65.61-.72c.37-.45,9.35-10.96,24.8-16.38,14.26-5,36.87-6.31,63.55,15.9l.83.69-.74.77c-.43.45-10.78,11.11-26.9,16.6-5.21,1.78-11.38,3.09-18.21,3.09ZM245.65,299.61c18.28,17.07,38.03,22.15,58.72,15.1,13.23-4.51,22.65-12.8,25.33-15.33-20.53-16.76-40.93-21.76-60.67-14.87-12.7,4.43-21.08,12.66-23.38,15.11Z" />
					<path fill={line} d="M329.94,290.08c-17.93-15.8-37.88-20.62-59.29-14.33-16.04,4.71-26.93,14.23-27.04,14.33l-1.33-1.5c.45-.4,11.28-9.88,27.73-14.73,15.22-4.49,38.2-5.57,61.25,14.73l-1.32,1.5Z" />
					<g class="iris" style="transform: translate({px}px, {py}px); opacity: {irisO};">
						<path fill={line} d="M287.37,313.49c-10.78,0-19.55-8.77-19.55-19.55,0-4.53,1.58-8.95,4.46-12.43l1.54,1.27c-2.58,3.13-4.01,7.1-4.01,11.16,0,9.68,7.87,17.55,17.55,17.55s17.55-7.87,17.55-17.55c0-3.66-1.12-7.17-3.23-10.15l1.63-1.16c2.36,3.32,3.6,7.23,3.6,11.31,0,10.78-8.77,19.55-19.55,19.55Z" />
						<circle fill={line} cx="287.22" cy="292.79" r="12.1" />
					</g>
				</g>
			</g>
		</svg>

		<!-- registration marks, Ionofolio-style -->
		<div class="marks" style="opacity: {chromeO};" aria-hidden="true">
			<span class="reg tl"></span><span class="reg tr"></span><span class="reg bl"></span><span class="reg br"></span>
		</div>

		<div class="wordmark" style="opacity: {chromeO};">FULL SCOPE MEDIA</div>

		<nav class="choices" style="opacity: {chromeO}; pointer-events: {phase === 'idle' ? 'auto' : 'none'};" aria-label="Choose a site">
			{#each choices as choice, i (choice.href)}
				<a href={choice.href} onclick={(e) => choose(e, choice.href)}>
					<span class="num">{String(i + 1).padStart(2, '0')}</span>
					<span class="label">{choice.label}</span>
				</a>
			{/each}
		</nav>
	</div>
{/if}

<style>
	.eye-gate {
		position: fixed;
		inset: 0;
		/* dvh keeps it covering the real visible area on mobile browsers */
		height: 100dvh;
		z-index: 9999;
		font-family: var(--font-studio, monospace);
		touch-action: manipulation;
	}
	svg {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		display: block;
		outline: none;
		-webkit-tap-highlight-color: transparent;
	}
	.iris {
		transition: transform 90ms linear, opacity 260ms ease-out;
	}

	.wordmark {
		position: absolute;
		top: max(5vh, calc(env(safe-area-inset-top) + 20px));
		left: 0;
		right: 0;
		text-align: center;
		pointer-events: none;
		color: #ecebe9;
		font-size: clamp(12px, 1.5vw, 15px);
		font-weight: 700;
		letter-spacing: 0.34em;
		transition: opacity 0.3s;
	}

	.choices {
		position: absolute;
		left: 0;
		right: 0;
		bottom: max(6vh, calc(env(safe-area-inset-bottom) + 24px));
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		gap: 14px;
		padding: 0 20px;
		transition: opacity 0.3s;
	}
	.choices a {
		display: inline-flex;
		align-items: baseline;
		gap: 12px;
		padding: 15px 24px;
		border: 1px solid rgba(236, 235, 233, 0.45);
		color: #ecebe9;
		text-decoration: none;
		font-size: clamp(11px, 1.4vw, 13px);
		font-weight: 700;
		letter-spacing: 0.28em;
		text-transform: uppercase;
		transition: border-color 0.2s, color 0.2s, background 0.2s;
	}
	.choices a .num {
		color: #ff5a00;
		font-weight: 400;
		letter-spacing: 0.1em;
	}
	.choices a:hover,
	.choices a:focus-visible {
		border-color: #ff5a00;
		background: rgba(255, 90, 0, 0.06);
		outline: none;
	}

	/* corner registration marks */
	.marks {
		position: absolute;
		inset: 18px;
		pointer-events: none;
		transition: opacity 0.3s;
	}
	.reg {
		position: absolute;
		width: 14px;
		height: 14px;
	}
	.reg::before,
	.reg::after {
		content: '';
		position: absolute;
		background: #ff5a00;
	}
	.reg::before {
		width: 14px;
		height: 1px;
		top: 7px;
	}
	.reg::after {
		width: 1px;
		height: 14px;
		left: 7px;
	}
	.tl { top: 0; left: 0; }
	.tr { top: 0; right: 0; }
	.bl { bottom: 0; left: 0; }
	.br { bottom: 0; right: 0; }

	@media (prefers-reduced-motion: reduce) {
		.iris {
			transition: none;
		}
	}
</style>
