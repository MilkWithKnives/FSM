export function inView(
	node: HTMLElement,
	{ threshold = 0.12, delay = 0 }: { threshold?: number; delay?: number } = {}
) {
	const observer = new IntersectionObserver(
		(entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					const run = () => node.classList.add('in-view');
					delay ? setTimeout(run, delay) : run();
					observer.unobserve(node);
				}
			});
		},
		{ threshold }
	);

	observer.observe(node);
	return { destroy: () => observer.disconnect() };
}
