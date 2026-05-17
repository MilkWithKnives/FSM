#!/usr/bin/env node
import { readdir, mkdir, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');
const OUT_DIR = join(ROOT, 'static', 'portfolio');

const WIDTHS = [800, 1400, 2000];
const WEBP_QUALITY = 78;
const JPEG_QUALITY = 82;

const properties = [
	{
		slug: '622-vine-st-st-joseph-mi-49085',
		sourceDir: '622-vine-st-st-joseph-mi-49085/images-for-web-or-mls',
		selected: [1, 9, 17, 25, 33, 41, 49, 58, 65, 73, 81, 89, 97, 105],
	},
	{
		slug: '4442-greenwood-dr-okemos-mi-48864',
		sourceDir: '4442-greenwood-dr-okemos-mi-48864/images-for-web-or-mls',
		selected: [1, 6, 11, 16, 21, 29, 31, 36, 41, 48, 51, 56, 61, 66],
	},
	{
		slug: '3977-stirrup-st-east-lansing-mi-48823',
		sourceDir: '3977-stirrup-st-east-lansing-mi-48823/images-for-web-or-mls',
		selected: [1, 4, 7, 10, 14, 16, 19, 22, 24, 28, 31, 34, 37, 40, 43],
	},
	{
		slug: '2877-bessemer-rd-coloma-mi-49038',
		sourceDir: '2877-bessemer-rd-coloma-mi-49038/images-for-web-or-mls',
		selected: [1, 4, 7, 10, 14, 16, 19, 21, 25, 28, 31, 34, 38],
	},
	{
		slug: '1904-carvel-ct-lansing-mi-48910',
		sourceDir: '1904-carvel-ct-lansing-mi-48910/images-for-web-or-mls',
		selected: [1, 4, 7, 10, 13, 16, 19, 21, 25, 27],
	},
];

const pad2 = (n) => String(n).padStart(2, '0');

const findSourceFile = async (sourceDir, index) => {
	const files = await readdir(sourceDir);
	const prefix = `${index}-`;
	const match = files.find((f) => f.startsWith(prefix) && /\.(jpe?g|png)$/i.test(f));
	return match ? join(sourceDir, match) : null;
};

const processOne = async ({ slug, sourceDir, selected }, opts) => {
	const srcDir = join(ROOT, sourceDir);
	const outDir = join(OUT_DIR, slug);
	await mkdir(outDir, { recursive: true });

	let made = 0;
	let skipped = 0;

	for (const idx of selected) {
		const src = await findSourceFile(srcDir, idx);
		if (!src) {
			console.warn(`  ! ${slug}: no file for index ${idx}`);
			continue;
		}
		const srcStat = await stat(src);

		for (const w of WIDTHS) {
			const webpOut = join(outDir, `${pad2(idx)}-${w}.webp`);
			const jpgOut = join(outDir, `${pad2(idx)}-${w}.jpg`);

			const needsWebp = !existsSync(webpOut) || (await stat(webpOut)).mtimeMs < srcStat.mtimeMs;
			const needsJpg = !existsSync(jpgOut) || (await stat(jpgOut)).mtimeMs < srcStat.mtimeMs;

			if (!needsWebp && !needsJpg && !opts.force) {
				skipped++;
				continue;
			}

			const pipeline = sharp(src).rotate().resize({ width: w, withoutEnlargement: true });

			if (needsWebp || opts.force) {
				await pipeline.clone().webp({ quality: WEBP_QUALITY, effort: 4 }).toFile(webpOut);
				made++;
			}
			if (needsJpg || opts.force) {
				await pipeline
					.clone()
					.jpeg({ quality: JPEG_QUALITY, progressive: true, mozjpeg: true })
					.toFile(jpgOut);
				made++;
			}
		}
	}

	console.log(`✓ ${slug}: made ${made}, skipped ${skipped}`);
};

const main = async () => {
	const force = process.argv.includes('--force');
	await mkdir(OUT_DIR, { recursive: true });
	for (const p of properties) {
		await processOne(p, { force });
	}
};

main().catch((err) => {
	console.error(err);
	process.exit(1);
});
