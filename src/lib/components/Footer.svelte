<script>
	const currentYear = new Date().getFullYear();

	const footerNav = [
		{
			title: 'Каталог',
			links: [
				{ label: 'Стили', href: '/styles' },
				{ label: 'Фасады', href: '/facades' },
				{ label: 'Фурнитура', href: '/furniture' },
				{ label: 'Кухни', href: '/styles' },
				{ label: 'Шкафы', href: '/styles' }
			]
		},
		{
			title: 'Компания',
			links: [
				{ label: 'О фабрике', href: '/about' },
				{ label: 'Новости', href: '/news' },
				{ label: 'Акции', href: '/promotions' },
				{ label: 'Дизайнерам', href: '/designers' },
				{ label: 'Вакансии', href: '/careers' }
			]
		},
		{
			title: 'Покупателям',
			links: [
				{ label: 'Салоны', href: '/showrooms' },
				{ label: 'Как заказать', href: '/how-to-order' },
				{ label: 'Доставка', href: '/delivery' },
				{ label: 'Гарантия', href: '/warranty' },
				{ label: 'Контакты', href: '/contacts' }
			]
		}
	];

	const socials = [
		{
			label: 'Instagram',
			href: '#',
			icon: 'M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z'
		},
		{
			label: 'Facebook',
			href: '#',
			icon: 'M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z'
		},
		{
			label: 'YouTube',
			href: '#',
			icon: 'M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z'
		}
	];
</script>

<footer class="relative bg-primary text-text-inverse">
	<!-- Decorative Top Line -->
	<div class="h-px w-full bg-gradient-to-r from-transparent via-accent to-transparent"></div>

	<!-- Main Footer Content -->
	<div class="mx-auto max-w-7xl px-6 pt-16 pb-10 lg:pt-20 lg:pb-14">
		<div class="grid grid-cols-2 gap-x-6 gap-y-12 lg:grid-cols-12 lg:gap-8">
			<!-- Brand Column -->
			<div class="col-span-2 lg:col-span-4">
				<a href="/" class="group inline-block">
					<img
						src="/images/logo-rus.png"
						alt="ЗОВ — мебельная фабрика"
						class="h-14 w-auto brightness-0 invert transition-opacity duration-300 group-hover:opacity-75 lg:h-16"
					/>
				</a>
				<p class="mt-6 max-w-xs text-sm leading-relaxed text-white/60">
					Более 20 лет создаём кухни и мебель премиального качества. Белорусское производство с
					европейскими технологиями.
				</p>

				<!-- Social Links -->
				<div class="mt-8 flex items-center gap-4">
					{#each socials as social (social.label)}
						<a
							href={social.href}
							class="flex h-10 w-10 items-center justify-center rounded-full border border-white/15 text-white/50 transition-all duration-300 hover:border-accent hover:text-accent"
							aria-label={social.label}
						>
							<svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
								<path d={social.icon} />
							</svg>
						</a>
					{/each}
				</div>
			</div>

			<!-- Navigation Columns -->
			{#each footerNav as column (column.title)}
				<div class="col-span-1 lg:col-span-2">
					<h4 class="text-xs font-medium tracking-[0.2em] text-white/40 uppercase">
						{column.title}
					</h4>
					<ul class="mt-5 flex flex-col gap-3">
						{#each column.links as link (link.label)}
							<li>
								<a
									href={link.href}
									class="text-sm text-white/65 transition-colors duration-300 hover:text-accent-light"
								>
									{link.label}
								</a>
							</li>
						{/each}
					</ul>
				</div>
			{/each}

			<!-- Contact Column -->
			<div class="col-span-1 lg:col-span-2">
				<h4 class="text-xs font-medium tracking-[0.2em] text-white/40 uppercase">Контакты</h4>
				<div class="mt-5 flex flex-col gap-4">
					<a
						href="tel:+375291234567"
						class="text-sm text-white/65 transition-colors duration-300 hover:text-accent-light"
					>
						+7 915 400-00-20
					</a>
					<a
						href="mailto:info@zov.by"
						class="text-sm text-white/65 transition-colors duration-300 hover:text-accent-light"
					>
						info@zov.top
					</a>
					<p class="text-sm leading-relaxed text-white/65">
						230005, Республика Беларусь, г. Гродно, <br />ул. Мясницкая, 12
					</p>
				</div>

				<div class="mt-6">
					<p class="text-[10px] tracking-[0.2em] text-white/30 uppercase">Режим работы</p>
					<p class="mt-2 text-sm text-white/65">Пн–Пт: 9:00 — 18:00</p>
					<p class="text-sm text-white/65">Сб: 10:00 — 15:00</p>
				</div>
			</div>
		</div>
	</div>

	<!-- Bottom Bar -->
	<div class="border-t border-white/10">
		<div
			class="mx-auto flex max-w-7xl flex-col items-center justify-between gap-4 px-6 py-6 md:flex-row"
		>
			<p class="text-xs text-white/35">
				© {currentYear} ЗОВ. Все права защищены.
			</p>
			<div class="flex items-center gap-6">
				<a
					href="/privacy"
					class="text-xs text-white/35 transition-colors duration-300 hover:text-white/60"
				>
					Политика конфиденциальности
				</a>
				<a
					href="/terms"
					class="text-xs text-white/35 transition-colors duration-300 hover:text-white/60"
				>
					Пользовательское соглашение
				</a>
			</div>
		</div>
	</div>
</footer>
