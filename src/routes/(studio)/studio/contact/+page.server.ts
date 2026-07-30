import { fail } from '@sveltejs/kit';
import nodemailer from 'nodemailer';
import { SMTP_USER, SMTP_PASS } from '$env/static/private';
import type { Actions } from './$types';

// Mirrors the real-estate contact action ((photo)/contact) — same transport and
// email format, but studio-side fields: business instead of property address.
const transporter = nodemailer.createTransport({
	host: 'smtp.protonmail.ch',
	port: 587,
	secure: false,
	auth: {
		user: SMTP_USER,
		pass: SMTP_PASS,
	},
});

export const actions: Actions = {
	default: async ({ request }) => {
		const data = await request.formData();

		const name     = (data.get('name')     as string)?.trim();
		const email    = (data.get('email')    as string)?.trim();
		const phone    = (data.get('phone')    as string)?.trim();
		const business = (data.get('business') as string)?.trim();
		const message  = (data.get('message')  as string)?.trim();
		const services = data.getAll('services') as string[];

		if (!name || !email || !message) {
			return fail(400, { error: 'Please fill in all required fields.' });
		}

		const html = `
<div style="font-family:sans-serif;max-width:600px;color:#1a1a1a">
  <h2 style="font-size:22px;font-weight:300;border-bottom:1px solid #eee;padding-bottom:12px;margin-bottom:20px">
    New Studio Inquiry — ${name}
  </h2>
  <table style="width:100%;border-collapse:collapse;font-size:14px">
    <tr><td style="padding:8px 0;color:#666;width:140px">Name</td><td>${name}</td></tr>
    <tr><td style="padding:8px 0;color:#666">Email</td><td><a href="mailto:${email}">${email}</a></td></tr>
    ${phone ? `<tr><td style="padding:8px 0;color:#666">Phone</td><td>${phone}</td></tr>` : ''}
    ${business ? `<tr><td style="padding:8px 0;color:#666">Business</td><td>${business}</td></tr>` : ''}
    ${services.length ? `<tr><td style="padding:8px 0;color:#666">Interested In</td><td>${services.join(', ')}</td></tr>` : ''}
  </table>
  <div style="margin-top:20px;padding:16px;background:#f9f9f9;border-left:3px solid #ccc;font-size:14px;color:#444">${message}</div>
</div>`;

		const text = [
			`New studio inquiry from ${name}`,
			`Email: ${email}`,
			phone    ? `Phone: ${phone}` : '',
			business ? `Business: ${business}` : '',
			services.length ? `Interested in: ${services.join(', ')}` : '',
			`\nProject:\n${message}`,
		].filter(Boolean).join('\n');

		try {
			await transporter.sendMail({
				from: `"Full Scope Media" <${SMTP_USER}>`,
				to: SMTP_USER,
				replyTo: email,
				subject: `New Studio Inquiry — ${name}${business ? ` · ${business}` : ''}`,
				text,
				html,
			});

			return { success: true };
		} catch (err) {
			console.error('Mail error:', err);
			return fail(500, { error: 'Failed to send your message. Please email us directly at rchampion@fullscope-media.com.' });
		}
	},
};
