import { fail } from '@sveltejs/kit';
import nodemailer from 'nodemailer';
import { SMTP_USER, SMTP_PASS } from '$env/static/private';
import type { Actions } from './$types';

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

		const name    = (data.get('name')    as string)?.trim();
		const email   = (data.get('email')   as string)?.trim();
		const phone   = (data.get('phone')   as string)?.trim();
		const address = (data.get('address') as string)?.trim();
		const date    = (data.get('date')    as string)?.trim();
		const message = (data.get('message') as string)?.trim();
		const services = data.getAll('services') as string[];

		if (!name || !email || !address) {
			return fail(400, { error: 'Please fill in all required fields.' });
		}

		const html = `
<div style="font-family:sans-serif;max-width:600px;color:#1a1a1a">
  <h2 style="font-size:22px;font-weight:300;border-bottom:1px solid #eee;padding-bottom:12px;margin-bottom:20px">
    New Inquiry — ${name}
  </h2>
  <table style="width:100%;border-collapse:collapse;font-size:14px">
    <tr><td style="padding:8px 0;color:#666;width:140px">Name</td><td>${name}</td></tr>
    <tr><td style="padding:8px 0;color:#666">Email</td><td><a href="mailto:${email}">${email}</a></td></tr>
    ${phone ? `<tr><td style="padding:8px 0;color:#666">Phone</td><td>${phone}</td></tr>` : ''}
    <tr><td style="padding:8px 0;color:#666">Property</td><td>${address}</td></tr>
    ${date ? `<tr><td style="padding:8px 0;color:#666">Preferred Date</td><td>${date}</td></tr>` : ''}
    ${services.length ? `<tr><td style="padding:8px 0;color:#666">Services</td><td>${services.join(', ')}</td></tr>` : ''}
  </table>
  ${message ? `<div style="margin-top:20px;padding:16px;background:#f9f9f9;border-left:3px solid #ccc;font-size:14px;color:#444">${message}</div>` : ''}
</div>`;

		const text = [
			`New inquiry from ${name}`,
			`Email: ${email}`,
			phone    ? `Phone: ${phone}` : '',
			`Property: ${address}`,
			date     ? `Preferred date: ${date}` : '',
			services.length ? `Services: ${services.join(', ')}` : '',
			message  ? `\nNotes:\n${message}` : '',
		].filter(Boolean).join('\n');

		try {
			await transporter.sendMail({
				from: `"Full Scope Media" <${SMTP_USER}>`,
				to: SMTP_USER,
				replyTo: email,
				subject: `New Inquiry — ${name} · ${address}`,
				text,
				html,
			});

			return { success: true };
		} catch (err) {
			console.error('Mail error:', err);
			return fail(500, { error: 'Failed to send your message. Please email us directly at info@fullscope-media.com.' });
		}
	},
};
