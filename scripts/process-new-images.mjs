import sharp from 'sharp';
import { readdir, mkdir, stat, writeFile } from 'node:fs/promises';
// Originals stay untouched. Only this upload batch is processed; existing assets are unchanged.
const files = (await readdir('.')).filter(name => /^(DJI_\d+|\d+-print-Open Ended Media-\d+|OEM)\.jpe?g$/i.test(name)).sort();
const report = [];
for (const name of files) {
 const folder = /^DJI_/i.test(name) ? 'drone' : 'onondaga';
 const stem = name.replace(/\.jpe?g$/i, '').toLowerCase().replace(/\s+/g, '-');
 const dir = `static/uploads/${folder}`;
 await mkdir(dir, { recursive: true });
 const original = await stat(name);
 let webBytes = 0;
 for (const width of [800, 1400, 2000]) {
  for (const format of ['avif', 'webp', 'jpg']) {
   const out = `${dir}/${stem}-${width}.${format}`;
   const pipeline = sharp(name).rotate().resize({ width, withoutEnlargement: true });
   if (format === 'avif') await pipeline.avif({ quality: 50, effort: 4 }).toFile(out);
   else if (format === 'webp') await pipeline.webp({ quality: 78, effort: 4 }).toFile(out);
   else await pipeline.jpeg({ quality: 82, progressive: true, mozjpeg: true }).toFile(out);
   if (width === 1400 && format === 'webp') webBytes = (await stat(out)).size;
  }
 }
 report.push({ original: name, originalBytes: original.size, web1400Bytes: webBytes, path: `/uploads/${folder}/${stem}` });
 console.log(`${name}: ${Math.round(original.size/1024)} KB → ${Math.round(webBytes/1024)} KB (1400px WebP)`);
}
await writeFile('reports/new-images.json', JSON.stringify(report, null, 2)+'\n');
// Keep the public gallery numbering stable in the same sorted source order.
const { copyFile } = await import('node:fs/promises');
const onondaga = report.filter(item => item.path.includes('/onondaga/'));
await mkdir('static/portfolio/onondaga-mi', { recursive: true });
for (const [index, item] of onondaga.entries()) {
 for (const width of [800, 1400, 2000]) for (const format of ['avif', 'webp', 'jpg']) {
  await copyFile(`static${item.path}-${width}.${format}`, `static/portfolio/onondaga-mi/${String(index + 1).padStart(2, '0')}-${width}.${format}`);
 }
}
