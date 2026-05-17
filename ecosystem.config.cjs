module.exports = {
	apps: [
		{
			name: 'fullscope-media',
			script: 'build/index.js',
			env: {
				NODE_ENV: 'production',
				PORT: 3000,
				HOST: '127.0.0.1',
				ORIGIN: 'https://fullscope-media.com',
			},
			instances: 1,
			exec_mode: 'fork',
			max_memory_restart: '300M',
			autorestart: true,
		},
	],
};
