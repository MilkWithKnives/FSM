import type { Property } from './properties';

export const PHOTO_WIDTHS = [800, 1400, 2000] as const;
export type PhotoWidth = (typeof PHOTO_WIDTHS)[number];

const pad = (n: number): string => String(n).padStart(2, '0');

const base = (slug: string, n: number): string => `/portfolio/${slug}/${pad(n)}`;

export const photoSrc = (slug: string, n: number, w: PhotoWidth = 1400): string =>
	`${base(slug, n)}-${w}.webp`;

export const photoFallback = (slug: string, n: number, w: PhotoWidth = 1400): string =>
	`${base(slug, n)}-${w}.jpg`;

export const photoSrcset = (slug: string, n: number, ext: 'avif' | 'webp' | 'jpg' = 'webp'): string =>
	PHOTO_WIDTHS.map((w) => `${base(slug, n)}-${w}.${ext} ${w}w`).join(', ');

export const heroPhoto = (p: Property, w: PhotoWidth = 2000): string => photoSrc(p.slug, p.selected[0], w);
export const heroFallback = (p: Property, w: PhotoWidth = 2000): string => photoFallback(p.slug, p.selected[0], w);

export const PHOTO_SIZES_GALLERY =
	'(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw';
export const PHOTO_SIZES_FULL = '100vw';
export const PHOTO_SIZES_HALF = '(min-width: 768px) 50vw, 100vw';
