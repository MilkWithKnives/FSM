import { readdir, open } from 'node:fs/promises';

const entries = await readdir('static', { recursive: true, withFileTypes: true });
const missing = [];
for (const entry of entries) {
	if (!entry.isFile()) continue;
	const path = `${entry.parentPath}/${entry.name}`;
	const file = await open(path, 'r');
	try {
		const buffer = Buffer.alloc(64);
		await file.read(buffer, 0, buffer.length, 0);
		if (buffer.toString().startsWith('version https://git-lfs.github.com/spec/v1')) missing.push(path);
	} finally {
		await file.close();
	}
}
if (missing.length) {
	console.error(`${missing.length} unresolved Git LFS files. Run git lfs pull before building.`);
	process.exit(1);
}
console.log('Static assets verified: no Git LFS pointers.');
