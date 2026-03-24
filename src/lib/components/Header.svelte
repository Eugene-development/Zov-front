<script>
	import Modal from '$lib/components/Modal.svelte';
	import ShowroomForm from '$lib/components/ShowroomForm.svelte';
	import QuizForm from '$lib/components/QuizForm.svelte';
	import { regionState } from '$lib/state/region.svelte';

	let scrolled = $state(false);
	let showTopBar = $state(true);
	let lastScrollY = $state(0);

	let mobileMenuOpen = $state(false);
	let isShowroomModalOpen = $state(false);
	let isCityModalOpen = $state(false);
	let isQuizModalOpen = $state(false);
	let activeCountry = $state('Россия');

	const showroomsData = {
		Беларусь: ['Минск', 'Гродно', 'Брест', 'Витебск', 'Гомель', 'Могилёв'],
		Россия: [
			'Москва',
			'Санкт-Петербург',
			'Нижний Новгород',
			'Казань',
			'Екатеринбург',
			'Новосибирск',
			'Омск',
			'Тюмень',
			'Челябинск',
			'Уфа',
			'Самара',
			'Воронеж',
			'Краснодар',
			'Ростов-на-Дону',
			'Волгоград',
			'Пермь',
			'Красноярск',
			'Тюмень',
			'Челябинск',
			'Уфа',
			'Самара',
			'Воронеж',
			'Краснодар',
			'Ростов-на-Дону',
			'Волгоград',
			'Пермь',
			'Красноярск'
		]
	};

	const topLinks = [
		{ label: 'О фабрике', href: '/about' },
		{ label: 'Новости', href: '/news' },
		{ label: 'Акции', href: '/promotions' },
		{ label: 'Кухни', href: '/kitchens' },
		{ label: 'Шкафы', href: '/wardrobes' }
	];

	const mainNav = [
		{ label: 'Главная', href: '/' },
		{ label: 'Стили', href: '/styles' },
		{ label: 'Фасады', href: '/facades' },
		{ label: 'Фурнитура', href: '/furniture' },
		{ label: 'Салоны', href: '/showrooms' }
	];

	function handleScroll() {
		const currentScrollY = Math.max(0, window.scrollY);
		scrolled = currentScrollY > 50;

		if (currentScrollY > 50) {
			if (currentScrollY < lastScrollY - 2) {
				showTopBar = true;
			} else if (currentScrollY > lastScrollY + 2) {
				showTopBar = false;
			}
		} else {
			showTopBar = true;
		}

		lastScrollY = currentScrollY;
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

<div class="sticky top-0 z-50 flex w-full flex-col">
	<!-- Top Info Bar -->
	<div
		class="relative hidden overflow-hidden border-b border-border-light bg-surface-warm transition-all duration-500 lg:block"
		class:h-0={!showTopBar}
		class:h-10={showTopBar}
	>
		<div
			class="mx-auto flex h-10 max-w-7xl items-center justify-between px-6 transition-opacity duration-300"
			class:opacity-0={!showTopBar}
			class:opacity-100={showTopBar}
		>
			<div class="flex items-center gap-6">
				{#each topLinks as link}
					<a
						href={link.href}
						class="text-xs tracking-wider text-secondary transition-colors duration-300 hover:text-secondary"
					>
						{link.label}
					</a>
				{/each}
			</div>
			<div class="flex items-center gap-5">
				<a
					href="tel:+79154000020"
					class="flex items-center gap-1.5 text-xs tracking-wide text-secondary transition-colors duration-300 hover:text-secondary"
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
					class="text-xs tracking-wide text-secondary transition-colors duration-300 hover:text-secondary"
				>
					info@zov.top
				</a>
				<span class="h-3 w-px bg-border-medium"></span>
				<button
					class="flex cursor-pointer items-center gap-1.5 text-xs tracking-wide text-secondary transition-colors duration-300 hover:text-secondary"
					onclick={() => (isCityModalOpen = true)}
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
							d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
						/>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
						/>
					</svg>
					{regionState.selectedCity}
				</button>
			</div>
		</div>
	</div>

	<!-- Main Header -->
	<header
		class="w-full transition-all duration-500 {scrolled
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
				<span class="hidden text-[10px] tracking-[0.3em] text-muted uppercase lg:block">
					мебельная фабрика
				</span>
			</a>

			<!-- Desktop Nav -->
			<nav class="hidden items-center gap-1 lg:flex" id="main-nav">
				{#each mainNav as item}
					<a
						href={item.href}
						class="group relative rounded-sm px-5 py-2.5 text-sm tracking-wide text-primary transition-colors duration-300 hover:text-secondary"
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
				<button
					onclick={() => (isQuizModalOpen = true)}
					class="group relative flex cursor-pointer items-center gap-2 rounded-sm px-2 py-2.5 text-sm tracking-wide text-primary transition-colors duration-300 hover:text-secondary"
				>
					Расчёт проекта
					<svg
						class="h-4 w-4 transition-transform duration-500 group-hover:translate-x-1"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						stroke-width="1.5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
						/>
					</svg>
					<span
						class="absolute bottom-0 left-1/2 h-px w-0 -translate-x-1/2 bg-secondary transition-all duration-500 group-hover:w-full"
					></span>
				</button>
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
					class="h-px w-6 bg-primary transition-all duration-300 {mobileMenuOpen
						? 'opacity-0'
						: ''}"
				></span>
				<span
					class="h-px w-6 bg-primary transition-all duration-300 {mobileMenuOpen
						? '-translate-y-[3.5px] -rotate-45'
						: ''}"
				></span>
			</button>
		</div>
	</header>
</div>

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
				class="border-b border-border-light py-4 text-lg tracking-wide text-primary transition-colors duration-300 hover:text-secondary"
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
				class="text-sm text-secondary transition-colors duration-300 hover:text-secondary"
				onclick={closeMenu}
			>
				{link.label}
			</a>
		{/each}
	</div>

	<div class="mt-auto border-t border-border-light px-8 py-6">
		<button
			class="mb-4 flex w-full cursor-pointer items-center gap-2 text-sm text-secondary transition-colors duration-300 hover:text-secondary"
			onclick={() => {
				isCityModalOpen = true;
				closeMenu();
			}}
		>
			<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
				/>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
				/>
			</svg>
			{regionState.selectedCity}
		</button>
		<a href="tel:+375291234567" class="block text-sm text-secondary"> +7 915 400-00-20 </a>
		<a href="mailto:info@zov.by" class="mt-2 block text-sm text-secondary"> info@zov.top </a>
		<button
			onclick={() => {
				isQuizModalOpen = true;
				closeMenu();
			}}
			class="group relative mt-5 flex w-full cursor-pointer items-center justify-between border-t border-border-light pt-5 text-left text-sm tracking-wide text-primary transition-colors duration-300 hover:text-secondary"
		>
			Расчёт проекта
			<svg
				class="h-4 w-4 transition-transform duration-500 group-hover:translate-x-1"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
				stroke-width="1.5"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
				/>
			</svg>
		</button>
	</div>
</div>

<!-- Modals -->
<Modal bind:showModal={isShowroomModalOpen} title="Запись в салон">
	<ShowroomForm onSuccess={() => (isShowroomModalOpen = false)} />
</Modal>

<Modal bind:showModal={isCityModalOpen} title="Выберите город">
	<div class="flex flex-col gap-6">
		<div class="flex items-center gap-4 border-b border-border-light pb-4">
			{#each Object.keys(showroomsData) as country}
				<button
					class="relative text-sm font-medium tracking-wide transition-colors duration-300 {activeCountry ===
					country
						? 'text-primary'
						: 'text-muted hover:text-secondary'}"
					onclick={() => (activeCountry = country)}
				>
					{country}
					{#if activeCountry === country}
						<span class="absolute -bottom-[17px] left-0 h-px w-full animate-fade-in bg-primary"
						></span>
					{/if}
				</button>
			{/each}
		</div>

		<div class="grid grid-cols-2 gap-3 sm:grid-cols-3">
			{#each showroomsData[activeCountry] as city}
				<button
					class="rounded-lg border border-border-light px-4 py-3 text-xs tracking-wide transition-all duration-300 {regionState.selectedCity ===
					city
						? 'border-primary bg-primary text-white'
						: 'bg-transparent text-secondary hover:border-primary hover:text-primary'}"
					onclick={() => {
						regionState.setCity(city);
						isCityModalOpen = false;
					}}
				>
					{city}
				</button>
			{/each}
		</div>
	</div>
</Modal>

<Modal bind:showModal={isQuizModalOpen} title="Экспресс расчёт мебели за 1 час">
	<QuizForm onSuccess={() => (isQuizModalOpen = false)} />
</Modal>
