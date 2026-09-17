# VPS deployment

Live site: https://fullscope-media.com
App directory: /var/www/fsm/FSM
Runtime: Node 24, pnpm 11.24.0, SvelteKit adapter-node.
Nginx proxies HTTPS to 127.0.0.1:3000. Systemd runs the app as www-data and restarts it on failure and boot. Certbot renews HTTPS certificates automatically.

## Deploy changes

```sh
cd /var/www/fsm/FSM
git lfs pull
pnpm install --frozen-lockfile
pnpm check
pnpm build
systemctl restart fullscope-media
```

## Status and logs

```sh
systemctl status fullscope-media nginx
journalctl -u fullscope-media -n 100 --no-pager
```

## Contact email configuration

Contact forms require Proton SMTP credentials. Create /etc/fullscope-media.env with mode 600, owned by root:

```ini
SMTP_USER=your-email-address
SMTP_PASS=your-proton-smtp-token
```

Then run `systemctl restart fullscope-media`. Credentials are read at runtime; no rebuild is needed. Email delivery was not configured or tested during deployment.

Service configuration: /etc/systemd/system/fullscope-media.service
Nginx configuration: /etc/nginx/sites-available/fullscope-media
