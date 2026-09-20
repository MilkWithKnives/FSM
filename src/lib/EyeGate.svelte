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
	import { untrack } from 'svelte';
	import { goto } from '$app/navigation';
	import EyeArtwork from '$lib/EyeArtwork.svelte';

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
	type PendingTimer = { id?: ReturnType<typeof setTimeout>; remaining: number; started: number; callback: () => void };
 let timers: PendingTimer[] = [];
 function resumeTimer(timer: PendingTimer) {
  timer.started = performance.now();
  timer.id = setTimeout(() => {
   timers = timers.filter(item => item !== timer);
   timer.callback();
  }, timer.remaining);
 }
 function schedule(callback: () => void, delay: number) {
  const timer: PendingTimer = { remaining: delay, started: performance.now(), callback };
  timers.push(timer);
  if (visible && tabVisible) resumeTimer(timer);
 }
 function clearTimers() { timers.forEach(timer => clearTimeout(timer.id)); timers = []; }
 let chosenHref = '';

	let container = $state<HTMLDivElement>();
 let visible = $state(true);
 let tabVisible = $state(true);
 $effect(() => {
  const media = window.matchMedia('(prefers-reduced-motion: reduce)');
  const motion = () => { reduced = media.matches; if (media.matches) { dx = dy = px = py = 0; wink = false; if (chosenHref && phase !== 'open') { clearTimers(); goto(chosenHref); phase = 'open'; onrevealend(); } } };
  const visibility = () => { tabVisible = !document.hidden; };
  untrack(motion); visibility();
  media.addEventListener('change', motion);
  document.addEventListener('visibilitychange', visibility);
  const observer = new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; });
  if (container) observer.observe(container);
  return () => {
   observer.disconnect();
   media.removeEventListener('change', motion);
   document.removeEventListener('visibilitychange', visibility);
   clearTimers();
  };
 });
 $effect(() => {
  const paused = !visible || !tabVisible;
  for (const timer of timers) {
   if (paused && timer.id !== undefined) {
    clearTimeout(timer.id); timer.remaining = Math.max(0, timer.remaining - (performance.now() - timer.started)); timer.id = undefined;
   } else if (!paused && timer.id === undefined) resumeTimer(timer);
  }
  for (const animation of container?.getAnimations({ subtree: true }) ?? []) {
   if (paused) animation.pause(); else animation.play();
  }
 });

	// Eye geometry: the logo almond is ~88 x 46 user units centered at (287.22, 296.5).
	// Scale responsively: ~74% of viewport width, capped by 42% of height.
	const s = $derived(Math.min((w * 0.74) / 88, (h * 0.42) / 46));
	const cx = $derived(w / 2 + dx);
	const cy = $derived(h / 2 + dy);
	// how far the hole must grow to swallow the whole viewport
	const coverScale = $derived(Math.ceil((Math.max(w, h) * 2.6) / (46 * s)));

	function onPointerMove(e: PointerEvent) {
		if (phase !== 'idle' || reduced || !visible || !tabVisible) return;
		const fx = Math.max(-0.5, Math.min(0.5, e.clientX / w - 0.5));
		const fy = Math.max(-0.5, Math.min(0.5, e.clientY / h - 0.5));
		dx = Math.round(fx * 2 * 2.75 * s);
		dy = Math.round(fy * 2 * 1.44 * s);
		px = Math.round(fx * 2 * 13 * 10) / 10;
		py = Math.round(fy * 2 * 5.5 * 10) / 10;
	}

	// Clicking the eye itself doesn't navigate — it just blinks back at you.
	function blink() {
		if (phase !== 'idle' || wink || reduced || !visible || !tabVisible) return;
		wink = true;
		schedule(() => (wink = false), 170);
	}

	function choose(e: MouseEvent, href: string) {
		e.preventDefault();
		if (phase !== 'idle') return;
		if (reduced) {
			goto(href);
			return;
		}
		dx = dy = px = py = 0;
		chosenHref = href;
		phase = 'closing';
		onrevealstart();
			schedule(() => (phase = 'opening'), 130);
			// Navigate the moment the hole starts expanding: the destination renders
			// underneath while the eye is still opening over it.
			schedule(() => {
				phase = 'expanding';
				goto(href);
			}, 860);
			schedule(() => {
				phase = 'open';
				onrevealend();
			}, 1650);
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
	<div class="eye-gate" class:reduced={reduced} class:revealing={phase !== 'idle'} bind:this={container}>
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
					<EyeArtwork {line} {px} {py} {irisO} />
				</g>
			</g>
		</svg>

		<!-- registration marks, Ionofolio-style -->
		<div class="marks" style="opacity: {chromeO};" aria-hidden="true">
			<span class="reg tl"></span><span class="reg tr"></span><span class="reg bl"></span><span class="reg br"></span>
		</div>

		<div class="wordmark" style="opacity: {chromeO};">
			FULL SCOPE MEDIA
			<p class="tagline">Every detail under my eye</p>
		</div>

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
		position: absolute;
		inset: 0;
		/* dvh keeps it covering the real visible area on mobile browsers */
		height: 100dvh;
		z-index: 9999;
		font-family: var(--font-studio, monospace);
		touch-action: manipulation;
	}
	.eye-gate.revealing { position: fixed; }
	.eye-gate.reduced :global(g) { transition: none !important; }
	svg {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		display: block;
		outline: none;
		-webkit-tap-highlight-color: transparent;
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

	.tagline {
		margin: 10px 20px 0;
		color: #b6b3af;
		font-size: clamp(11px, 1.2vw, 13px);
		font-weight: 400;
		letter-spacing: 0.08em;
		line-height: 1.5;
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

</style>
