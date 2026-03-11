<script>
	let scrolled = $state(false);
	let mobileMenuOpen = $state(false);

	const topLinks = [
		{ label: 'О фабрике', href: '/about' },
		{ label: 'Акции', href: '/promotions' },
		{ label: 'Новости', href: '/news' },
		{ label: 'Дизайнерам', href: '/designers' },
		{ label: 'Вакансии', href: '/careers' }
	];

	const mainNav = [
		{ label: 'Главная', href: '/' },
		{ label: 'Стили', href: '/styles' },
		{ label: 'Фасады', href: '/facades' },
		{ label: 'Фурнитура', href: '/furniture' },
		{ label: 'Салоны', href: '/showrooms' }
	];

	function handleScroll() {
		scrolled = window.scrollY > 50;
	}

	function toggleMenu() {
		mobileMenuOpen = !mobileMenuOpen;
		if (mobileMenuOpen) {
			document.body.style.overflow = 'hidden';
		} else {
			document.body.style.overflow = '';
		}
	}

	function closeMenu() {
		mobileMenuOpen = false;
		document.body.style.overflow = '';
	}
</script>

<svelte:window onscroll={handleScroll} />

<!-- Top Info Bar -->
<div
	class="relative z-50 hidden border-b border-border-light bg-surface-warm transition-all duration-500 lg:block"
	class:opacity-0={scrolled}
	class:h-0={scrolled}
	class:overflow-hidden={scrolled}
	class:h-10={!scrolled}
>
	<div class="mx-auto flex h-10 max-w-7xl items-center justify-between px-6">
		<div class="flex items-center gap-6">
			{#each topLinks as link}
				<a
					href={link.href}
					class="text-xs tracking-wider text-text-secondary transition-colors duration-300 hover:text-secondary"
				>
					{link.label}
				</a>
			{/each}
		</div>
		<div class="flex items-center gap-5">
			<a
				href="tel:+375291234567"
				class="flex items-center gap-1.5 text-xs tracking-wide text-text-secondary transition-colors duration-300 hover:text-secondary"
			>
				<svg
					class="h-3.5 w-3.5"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					stroke-width="1.5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"
					/>
				</svg>
				+7 915 400-00-20
			</a>
			<span class="h-3 w-px bg-border-medium"></span>
			<a
				href="mailto:info@zov.by"
				class="text-xs tracking-wide text-text-secondary transition-colors duration-300 hover:text-secondary"
			>
				info@zov.top
			</a>
		</div>
	</div>
</div>

<!-- Main Header -->
<header
	class="sticky top-0 z-40 transition-all duration-500 {scrolled
		? 'bg-white/95 shadow-soft backdrop-blur-lg'
		: 'border-b border-border-light bg-white'}"
>
	<div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-6 lg:h-20">
		<!-- Logo -->
		<a href="/" class="group flex items-center gap-3" onclick={closeMenu}>
			<span
				class="text-3xl font-light tracking-[0.2em] text-primary transition-colors duration-300 group-hover:text-secondary lg:text-4xl"
				style="font-family: var(--font-heading);"
			>
				ЗОВ
			</span>
			<span class="hidden text-[10px] tracking-[0.3em] text-text-muted uppercase lg:block">
				мебельная фабрика
			</span>
		</a>

		<!-- Desktop Nav -->
		<nav class="hidden items-center gap-1 lg:flex" id="main-nav">
			{#each mainNav as item}
				<a
					href={item.href}
					class="group relative px-5 py-2.5 text-sm tracking-wide text-text-primary transition-colors duration-300 hover:text-secondary"
				>
					{item.label}
					<span
						class="absolute bottom-0 left-1/2 h-px w-0 -translate-x-1/2 bg-secondary transition-all duration-500 group-hover:w-3/4"
					></span>
				</a>
			{/each}
		</nav>

		<!-- CTA Desktop -->
		<div class="hidden items-center gap-4 lg:flex">
			<a
				href="/showrooms"
				class="group relative overflow-hidden rounded-none border border-primary bg-primary px-7 py-2.5 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:bg-transparent hover:text-primary"
			>
				<span class="relative z-10">Найти салон</span>
			</a>
		</div>

		<!-- Mobile Burger -->
		<button
			class="relative z-50 flex h-10 w-10 flex-col items-center justify-center gap-1.5 lg:hidden"
			onclick={toggleMenu}
			aria-label="Меню"
			id="mobile-menu-toggle"
		>
			<span
				class="h-px w-6 bg-primary transition-all duration-300 {mobileMenuOpen
					? 'translate-y-[3.5px] rotate-45'
					: ''}"
			></span>
			<span
				class="h-px w-6 bg-primary transition-all duration-300 {mobileMenuOpen ? 'opacity-0' : ''}"
			></span>
			<span
				class="h-px w-6 bg-primary transition-all duration-300 {mobileMenuOpen
					? '-translate-y-[3.5px] -rotate-45'
					: ''}"
			></span>
		</button>
	</div>
</header>

<!-- Mobile Menu Overlay -->
{#if mobileMenuOpen}
	<div
		class="fixed inset-0 z-30 bg-black/20 backdrop-blur-sm lg:hidden"
		onclick={closeMenu}
		role="presentation"
	></div>
{/if}

<!-- Mobile Menu Panel -->
<div
	class="fixed top-0 right-0 z-35 flex h-full w-80 max-w-[85vw] flex-col bg-white pt-20 shadow-elevated transition-transform duration-500 lg:hidden {mobileMenuOpen
		? 'translate-x-0'
		: 'translate-x-full'}"
>
	<nav class="flex flex-col px-8 py-6">
		{#each mainNav as item, i}
			<a
				href={item.href}
				class="border-b border-border-light py-4 text-lg tracking-wide text-text-primary transition-colors duration-300 hover:text-secondary"
				style="font-family: var(--font-heading);"
				onclick={closeMenu}
			>
				{item.label}
			</a>
		{/each}
	</nav>

	<div class="mt-4 flex flex-col gap-3 px-8">
		{#each topLinks as link}
			<a
				href={link.href}
				class="text-sm text-text-secondary transition-colors duration-300 hover:text-secondary"
				onclick={closeMenu}
			>
				{link.label}
			</a>
		{/each}
	</div>

	<div class="mt-auto border-t border-border-light px-8 py-6">
		<a href="tel:+375291234567" class="block text-sm text-text-secondary"> +7 915 400-00-20 </a>
		<a href="mailto:info@zov.by" class="mt-2 block text-sm text-text-secondary"> info@zov.top </a>
		<a
			href="/showrooms"
			class="mt-5 block border border-primary bg-primary py-3 text-center text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-300 hover:bg-transparent hover:text-primary"
			onclick={closeMenu}
		>
			Найти салон
		</a>
	</div>
</div>
