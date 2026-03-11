<script>
	import { onMount } from 'svelte';

	let heroVisible = $state(false);
	let sections = $state({});
	let activeFilter = $state('all');
	let timeLeft = $state({ days: 0, hours: 0, minutes: 0, seconds: 0 });
	let timerInterval;

	// Countdown timer — до конца сезонной акции
	function calcTimeLeft() {
		const target = new Date('2026-04-15T00:00:00');
		const now = new Date();
		const diff = target - now;
		if (diff <= 0) return { days: 0, hours: 0, minutes: 0, seconds: 0 };
		return {
			days: Math.floor(diff / (1000 * 60 * 60 * 24)),
			hours: Math.floor((diff / (1000 * 60 * 60)) % 24),
			minutes: Math.floor((diff / (1000 * 60)) % 60),
			seconds: Math.floor((diff / 1000) % 60)
		};
	}

	onMount(() => {
		heroVisible = true;
		timeLeft = calcTimeLeft();
		timerInterval = setInterval(() => {
			timeLeft = calcTimeLeft();
		}, 1000);

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting && entry.target.id) {
						sections = { ...sections, [entry.target.id]: true };
					}
				});
			},
			{ threshold: 0, rootMargin: '0px 0px 0px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => {
			observer.disconnect();
			clearInterval(timerInterval);
		};
	});

	const filters = [
		{ key: 'all', label: 'Все акции' },
		{ key: 'kitchen', label: 'Кухни' },
		{ key: 'wardrobe', label: 'Гардеробные' },
		{ key: 'living', label: 'Гостиная' }
	];

	const promotions = [
		{
			id: 1,
			category: 'kitchen',
			tag: 'Хит сезона',
			tagColor: 'accent',
			discount: '−30%',
			title: 'Кухни серии «Модерн»',
			description:
				'Полный комплект кухонного гарнитура с фасадами из матовой эмали. Столешница из искусственного камня и фурнитура Blum в подарок.',
			oldPrice: '320 000',
			newPrice: '224 000',
			image: '/images/promo-kitchen.png',
			until: '15 апреля 2026',
			features: ['Фасады из матовой эмали', 'Столешница из камня', 'Фурнитура Blum']
		},
		{
			id: 2,
			category: 'wardrobe',
			tag: 'Бесплатно',
			tagColor: 'secondary',
			discount: 'Дизайн-проект',
			title: 'Гардеробные системы',
			description:
				'При заказе гардеробной от 150 000 руб. — бесплатный выезд дизайнера и разработка 3D-проекта. Уникальная система хранения под ваши нужды.',
			oldPrice: null,
			newPrice: 'от 150 000',
			image: '/images/promo-wardrobe.png',
			until: '30 апреля 2026',
			features: ['Бесплатный 3D-проект', 'Выезд дизайнера', 'Установка за 1 день']
		},
		{
			id: 3,
			category: 'living',
			tag: 'Лимитировано',
			tagColor: 'primary',
			discount: '−25%',
			title: 'Гостиные «Эксклюзив»',
			description:
				'Мебельные комплекты для гостиной из коллекции «Эксклюзив»: TV-панели, открытые стеллажи, закрытые тумбы. Шпон натурального ореха.',
			oldPrice: '480 000',
			newPrice: '360 000',
			image: '/images/promo-living.png',
			until: '28 апреля 2026',
			features: ['Шпон натурального ореха', 'Интегрированная подсветка', 'Сборка в подарок']
		},
		{
			id: 4,
			category: 'kitchen',
			tag: 'Рассрочка',
			tagColor: 'accent',
			discount: '0%',
			title: 'Кухни в рассрочку',
			description:
				'Оформите любую кухню в рассрочку на 24 месяца без переплаты. Первый взнос от 20%. Быстрое одобрение за 15 минут.',
			oldPrice: null,
			newPrice: 'от 5 000/мес',
			image: '/images/hero-kitchen.png',
			until: '31 мая 2026',
			features: ['24 месяца без %', 'Первый взнос от 20%', 'Одобрение за 15 мин']
		},
		{
			id: 5,
			category: 'wardrobe',
			tag: 'Новинка',
			tagColor: 'secondary',
			discount: '−15%',
			title: 'Walk-in гардероб',
			description:
				'Гардеробные комнаты полного цикла: проектирование, изготовление, монтаж. Системы с подсветкой, зеркальными панелями и ящиками с мягким закрыванием.',
			oldPrice: '280 000',
			newPrice: '238 000',
			image: '/images/promo-wardrobe.png',
			until: '20 апреля 2026',
			features: ['LED-подсветка', 'Зеркальные панели', 'Мягкое закрывание']
		},
		{
			id: 6,
			category: 'kitchen',
			tag: 'Trade-in',
			tagColor: 'primary',
			discount: 'до −50 000 ₽',
			title: 'Обмен старой кухни',
			description:
				'Сдайте вашу старую кухню и получите скидку до 50 000 рублей на новый премиальный гарнитур. Мы вывезем старую мебель бесплатно.',
			oldPrice: null,
			newPrice: 'Оценка бесплатно',
			image: '/images/showroom.png',
			until: '15 мая 2026',
			features: ['Бесплатный вывоз', 'Оценка за 1 день', 'Скидка до 50 000 ₽']
		}
	];

	const benefits = [
		{
			icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.745 3.745 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.745 3.745 0 013.296-1.043A3.745 3.745 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.745 3.745 0 013.296 1.043 3.745 3.745 0 011.043 3.296A3.745 3.745 0 0121 12z"/></svg>`,
			title: 'Гарантия подлинности',
			text: 'Все скидки реальны, без скрытых условий и ограничений'
		},
		{
			icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 00-10.026 0 1.106 1.106 0 00-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12"/></svg>`,
			title: 'Бесплатная доставка',
			text: 'Доставка и подъём на этаж включены в каждую акцию'
		},
		{
			icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>`,
			title: 'Ограниченный срок',
			text: 'Акции действуют строго в указанный период — не упустите'
		},
		{
			icon: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"/></svg>`,
			title: 'Персональный дизайнер',
			text: 'Бесплатная консультация специалиста при любом заказе'
		}
	];

	let filteredPromos = $derived(
		activeFilter === 'all' ? promotions : promotions.filter((p) => p.category === activeFilter)
	);

	function pad(n) {
		return String(n).padStart(2, '0');
	}
</script>

<svelte:head>
	<title>Акции и спецпредложения — ЗОВ | Премиальная мебель со скидкой</title>
	<meta
		name="description"
		content="Актуальные акции и специальные предложения от фабрики ЗОВ. Скидки на кухни, гардеробные и мебель для гостиной до 30%. Ограниченные предложения."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-screen overflow-hidden bg-surface" id="promo-hero">
	<!-- Background Image with Overlay -->
	<div class="absolute inset-0">
		<img
			src="/images/promo-hero.png"
			alt="Акции ЗОВ — премиальная мебель"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<!-- Strengthened gradient: left side is almost white, right stays transparent -->
		<div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/75 to-white/10"></div>
		<div
			class="absolute inset-0 bg-gradient-to-t from-white/60 via-transparent to-transparent"
		></div>
	</div>

	<!-- Decorative vertical accent line -->
	<div
		class="absolute top-0 left-1/2 h-full w-px bg-gradient-to-b from-transparent via-secondary/10 to-transparent opacity-0"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1.2s"
	></div>

	<!-- Decorative watermark text (right side) -->
	<div
		class="pointer-events-none absolute right-0 bottom-20 hidden overflow-hidden opacity-0 select-none lg:block"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1s"
	>
		<span
			class="block text-[140px] leading-none font-light tracking-tighter text-primary/5 xl:text-[180px]"
			style="font-family: var(--font-heading); writing-mode: horizontal-tb;"
		>
			SALE
		</span>
	</div>

	<!-- Floating discount badge (top-right of viewport) -->
	<div
		class="absolute top-1/4 right-8 hidden opacity-0 lg:flex lg:flex-col lg:items-center lg:gap-1"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1.1s"
	>
		<div
			class="flex h-24 w-24 flex-col items-center justify-center border border-secondary/30 bg-white/50 text-center shadow-soft backdrop-blur-sm"
		>
			<span class="text-[10px] tracking-[0.2em] text-secondary/70 uppercase">до</span>
			<span
				class="text-3xl leading-none font-light text-secondary"
				style="font-family: var(--font-heading);">−30%</span
			>
			<span class="mt-0.5 text-[9px] tracking-[0.15em] text-text-muted uppercase">скидка</span>
		</div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-screen items-center pt-40 pb-32">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-2xl">
				<!-- Label -->
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span
						class="inline-flex items-center gap-2 border border-secondary/30 bg-white/70 px-4 py-2 text-[11px] tracking-[0.25em] text-secondary uppercase backdrop-blur-sm"
					>
						Специальные предложения 2026
					</span>
				</div>

				<!-- Heading -->
				<h1
					class="text-5xl leading-[1.1] font-light text-primary opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Акции &
					<br />
					<span class="font-normal text-secondary">спецпредложения</span>
				</h1>

				<!-- Stats row -->
				<div
					class="mt-10 flex items-center gap-8 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.65s"
				>
					<div class="flex flex-col gap-1">
						<span class="text-2xl font-light text-primary" style="font-family: var(--font-heading);"
							>6+</span
						>
						<span class="text-xs tracking-[0.15em] text-text-muted uppercase">акций сейчас</span>
					</div>
					<div class="h-8 w-px bg-border-medium"></div>
					<div class="flex flex-col gap-1">
						<span class="text-2xl font-light text-primary" style="font-family: var(--font-heading);"
							>−30%</span
						>
						<span class="text-xs tracking-[0.15em] text-text-muted uppercase">макс. скидка</span>
					</div>
					<div class="hidden h-8 w-px bg-border-medium sm:block"></div>
					<div class="hidden flex-col gap-1 sm:flex">
						<span class="text-2xl font-light text-primary" style="font-family: var(--font-heading);"
							>0 ₽</span
						>
						<span class="text-xs tracking-[0.15em] text-text-muted uppercase">за доставку</span>
					</div>
				</div>

				<!-- Description -->
				<p
					class="mt-6 max-w-md text-base leading-relaxed text-text-secondary opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Эксклюзивные предложения на кухни, гардеробные и мебель для гостиной. Только реальные
					скидки на премиальные решения от фабрики ЗОВ.
				</p>

				<!-- CTA Buttons -->
				<div
					class="mt-10 flex flex-wrap items-center gap-4 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.9s"
				>
					<a
						href="#promo-grid"
						class="group inline-flex items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
					>
						Смотреть акции
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
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
					</a>
					<a
						href="/showrooms"
						class="group inline-flex items-center gap-3 border border-border-medium bg-white/70 px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase backdrop-blur-sm transition-all duration-500 hover:border-secondary hover:text-secondary"
					>
						Записаться на консультацию
					</a>
				</div>
			</div>
		</div>
	</div>

	<!-- Scroll Indicator -->
	<div
		class="absolute bottom-10 left-1/2 -translate-x-1/2 opacity-0"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1.3s"
	>
		<div class="flex flex-col items-center gap-2">
			<span class="text-[10px] tracking-[0.3em] text-text-muted uppercase">Листайте</span>
			<div class="h-10 w-px bg-gradient-to-b from-text-muted to-transparent"></div>
		</div>
	</div>
</section>

<!-- ==================== COUNTDOWN TIMER ==================== -->
<section class="relative bg-surface pt-16 pb-24 lg:pt-24 lg:pb-32" id="timer-section" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<div
			class="relative flex flex-col items-center gap-16 lg:flex-row lg:justify-between lg:gap-24"
			class:opacity-0={!sections['timer-section']}
			class:animate-fade-up={sections['timer-section']}
		>
			<!-- Text content -->
			<div class="flex-1 text-center lg:text-left">
				<div class="mb-6 flex justify-center lg:justify-start">
					<span
						class="inline-flex items-center gap-2 border border-secondary/30 bg-transparent px-4 py-2 text-[10px] tracking-[0.3em] text-secondary uppercase"
					>
						<span class="h-1.5 w-1.5 rounded-full bg-secondary"></span>
						Главная акция сезона
					</span>
				</div>
				<h2
					class="text-4xl leading-[1.1] font-light text-primary md:text-5xl lg:text-6xl"
					style="font-family: var(--font-heading);"
				>
					Весенняя
					<span class="text-secondary italic">акция</span>
				</h2>
				<p class="mx-auto mt-6 max-w-md text-base leading-relaxed text-text-secondary lg:mx-0">
					Успейте оформить заказ премиальной мебели до 15 апреля. Бесплатный дизайн-проект и скидки
					до 30%.
				</p>
				<div class="mt-10">
					<a
						href="/showrooms"
						class="group inline-flex items-center gap-3 bg-primary px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:bg-secondary"
					>
						Успеть получить скидку
						<svg
							class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
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
					</a>
				</div>
			</div>

			<!-- Timer display -->
			<div class="flex flex-wrap items-center justify-center gap-4 sm:gap-6 lg:justify-end">
				{#each [{ v: timeLeft.days, l: 'Дней' }, { v: timeLeft.hours, l: 'Часов' }, { v: timeLeft.minutes, l: 'Минут' }, { v: timeLeft.seconds, l: 'Секунд' }] as unit, i}
					<div class="flex w-[70px] flex-col items-center gap-4 sm:w-[90px] lg:w-[110px]">
						<div
							class="group relative flex aspect-square w-full items-center justify-center border border-border-light bg-white shadow-soft"
						>
							<!-- Decorative inner border that appears on hover -->
							<div
								class="absolute inset-2 border border-border-light/50 opacity-0 transition-opacity duration-500 group-hover:opacity-100"
							></div>

							<span
								class="text-4xl font-light tracking-tighter text-primary tabular-nums sm:text-5xl lg:text-6xl"
								style="font-family: var(--font-heading);"
							>
								{pad(unit.v)}
							</span>
						</div>
						<span class="text-[10px] tracking-[0.25em] text-text-secondary uppercase">
							{unit.l}
						</span>
					</div>
					{#if i < 3}
						<div
							class="flex flex-col items-center pb-8 text-3xl font-light text-border-medium sm:text-4xl lg:pb-10 lg:text-5xl"
						>
							:
						</div>
					{/if}
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- ==================== PROMOTIONS GRID ==================== -->
<section class="relative py-section-sm lg:py-section" id="promo-grid" data-animate>
	<!-- Subtle Background Pattern -->
	<div
		class="absolute inset-0 opacity-[0.03]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%232c2c2c\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<!-- Section Header -->
		<div
			class="mb-12 flex flex-col items-start justify-between gap-6 md:flex-row md:items-end"
			class:opacity-0={!sections['promo-grid']}
			class:animate-fade-up={sections['promo-grid']}
		>
			<div>
				<span class="text-[11px] tracking-[0.3em] text-secondary uppercase"
					>Текущие предложения</span
				>
				<h2
					class="mt-3 text-4xl font-light text-primary lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Все акции
				</h2>
			</div>
			<!-- Filter Tabs -->
			<div class="flex flex-wrap gap-2">
				{#each filters as filter}
					<button
						onclick={() => (activeFilter = filter.key)}
						class="border px-5 py-2.5 text-xs tracking-[0.12em] uppercase transition-all duration-300"
						class:border-primary={activeFilter === filter.key}
						class:bg-primary={activeFilter === filter.key}
						class:text-white={activeFilter === filter.key}
						class:border-border-medium={activeFilter !== filter.key}
						class:text-text-secondary={activeFilter !== filter.key}
						class:hover:border-secondary={activeFilter !== filter.key}
						class:hover:text-secondary={activeFilter !== filter.key}
					>
						{filter.label}
					</button>
				{/each}
			</div>
		</div>

		<!-- Promo Cards Grid -->
		<div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
			{#each filteredPromos as promo, i (promo.id)}
				<article
					class="group relative flex flex-col overflow-hidden bg-white shadow-card transition-all duration-500 hover:-translate-y-2 hover:shadow-elevated"
					class:opacity-0={!sections['promo-grid']}
					class:animate-fade-up={sections['promo-grid']}
					style="animation-delay: {0.15 + i * 0.1}s"
				>
					<!-- Image -->
					<div class="relative aspect-[3/2] overflow-hidden">
						<img
							src={promo.image}
							alt={promo.title}
							class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
						<!-- Gradient overlay -->
						<div
							class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/10 to-transparent"
						></div>

						<!-- Tag badge -->
						<div class="absolute top-4 left-4">
							<span
								class="inline-flex items-center gap-1.5 px-3 py-1.5 text-[10px] font-medium tracking-[0.2em] uppercase"
								class:bg-accent={promo.tagColor === 'accent'}
								class:text-primary={promo.tagColor === 'accent'}
								class:bg-secondary={promo.tagColor === 'secondary'}
								class:text-white={promo.tagColor === 'secondary' || promo.tagColor === 'primary'}
								class:bg-primary={promo.tagColor === 'primary'}
							>
								{promo.tag}
							</span>
						</div>

						<!-- Discount badge -->
						<div class="absolute right-4 bottom-4">
							<div
								class="flex h-16 w-16 items-center justify-center rounded-full border border-white/30 bg-white/20 text-center text-xs font-medium text-white backdrop-blur-md"
							>
								<span class="leading-tight">{promo.discount}</span>
							</div>
						</div>
					</div>

					<!-- Content -->
					<div class="flex flex-1 flex-col p-6 lg:p-8">
						<h3
							class="text-xl font-medium text-primary transition-colors duration-300 group-hover:text-secondary lg:text-2xl"
							style="font-family: var(--font-heading);"
						>
							{promo.title}
						</h3>
						<p class="mt-3 text-sm leading-relaxed text-text-secondary">{promo.description}</p>

						<!-- Features -->
						<ul class="mt-4 flex flex-col gap-2">
							{#each promo.features as feat}
								<li class="flex items-center gap-2 text-xs text-text-secondary">
									<svg
										class="h-3.5 w-3.5 flex-shrink-0 text-accent"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
										stroke-width="2"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M4.5 12.75l6 6 9-13.5"
										/>
									</svg>
									{feat}
								</li>
							{/each}
						</ul>

						<!-- Price -->
						<div class="mt-6 border-t border-border-light pt-5">
							<div class="flex items-end justify-between">
								<div>
									{#if promo.oldPrice}
										<p class="text-xs text-text-muted line-through">{promo.oldPrice} ₽</p>
									{/if}
									<p
										class="text-2xl font-light text-primary"
										style="font-family: var(--font-heading);"
									>
										{promo.newPrice}
										{#if !promo.oldPrice}<span class="text-base"> ₽</span>{:else}<span
												class="text-base"
											>
												₽</span
											>{/if}
									</p>
								</div>
								<div class="text-right">
									<p class="text-[10px] tracking-[0.1em] text-text-muted uppercase">До</p>
									<p class="text-xs text-text-secondary">{promo.until}</p>
								</div>
							</div>

							<!-- CTA -->
							<a
								href="/showrooms"
								class="group/btn mt-4 flex w-full items-center justify-center gap-2 border border-primary bg-transparent px-6 py-3 text-xs tracking-[0.12em] text-primary uppercase transition-all duration-300 hover:bg-primary hover:text-white"
							>
								Узнать подробнее
								<svg
									class="h-3.5 w-3.5 transition-transform duration-300 group-hover/btn:translate-x-1"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
									stroke-width="2"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
									/>
								</svg>
							</a>
						</div>
					</div>
				</article>
			{/each}
		</div>

		<!-- Empty state -->
		{#if filteredPromos.length === 0}
			<div class="flex flex-col items-center py-24 text-center">
				<svg
					class="h-12 w-12 text-border-medium"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					stroke-width="1"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 005.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 009.568 3z"
					/>
					<path stroke-linecap="round" stroke-linejoin="round" d="M6 6h.008v.008H6V6z" />
				</svg>
				<p class="mt-4 text-base text-text-muted">Акций в этой категории пока нет</p>
			</div>
		{/if}
	</div>
</section>

<!-- ==================== FEATURED BANNER ==================== -->
<section class="relative z-10 px-6" id="featured-banner" data-animate>
	<div class="mx-auto max-w-7xl">
		<div
			class="relative overflow-hidden"
			class:opacity-0={!sections['featured-banner']}
			class:animate-scale-in={sections['featured-banner']}
		>
			<img
				src="/images/promo-kitchen.png"
				alt="Премиальные кухни со скидкой"
				class="h-[400px] w-full object-cover lg:h-[520px]"
			/>
			<div
				class="absolute inset-0 bg-gradient-to-r from-primary/90 via-primary/60 to-transparent"
			></div>

			<!-- Overlay Content -->
			<div class="absolute inset-0 flex items-center p-8 lg:p-16">
				<div class="max-w-xl">
					<span class="text-[11px] tracking-[0.3em] text-accent uppercase"
						>Специальное предложение</span
					>
					<h2
						class="mt-4 text-3xl font-light text-white lg:text-5xl"
						style="font-family: var(--font-heading);"
					>
						Кухня мечты
						<span class="text-accent-light"> −30%</span>
					</h2>
					<p class="mt-4 max-w-sm text-sm leading-relaxed text-white/75 lg:text-base">
						Закажите кухонный гарнитур серии «Модерн» до 15 апреля и получите скидку 30%, бесплатную
						установку и фурнитуру Blum в подарок.
					</p>
					<div class="mt-8 flex flex-wrap gap-4">
						<a
							href="/showrooms"
							class="group inline-flex items-center gap-3 border border-accent bg-accent px-7 py-3.5 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-300 hover:bg-accent-light"
						>
							Заказать со скидкой
							<svg
								class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
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
						</a>
						<a
							href="/showrooms"
							class="inline-flex items-center gap-3 border border-white/30 bg-white/10 px-7 py-3.5 text-xs tracking-[0.15em] text-white uppercase backdrop-blur-sm transition-all duration-500 hover:bg-white hover:text-primary"
						>
							Условия акции
						</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ==================== HOW IT WORKS SECTION ==================== -->
<section
	class="relative -mt-12 bg-surface-warm pt-28 pb-section-sm lg:-mt-20 lg:pt-40 lg:pb-section"
	id="how-section"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header -->
		<div
			class="mb-16 text-center"
			class:opacity-0={!sections['how-section']}
			class:animate-fade-up={sections['how-section']}
		>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Просто</span>
			<h2
				class="mt-3 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Как получить скидку
			</h2>
			<p class="mx-auto mt-4 max-w-lg text-base leading-relaxed text-text-secondary">
				Воспользоваться акцией легко — всего 3 шага до новой мебели по выгодной цене
			</p>
		</div>

		<!-- Steps -->
		<div class="grid gap-8 md:grid-cols-3">
			{#each [{ num: '01', title: 'Выберите акцию', text: 'Изучите текущие предложения и выберите подходящую для вашего проекта. Позвоните нам или запишитесь онлайн.' }, { num: '02', title: 'Получите консультацию', text: 'Наш дизайнер приедет к вам и разработает проект с учётом всех пожеланий. Бесплатно и в удобное время.' }, { num: '03', title: 'Оформите заказ', text: 'Подпишите договор, и мы приступим к производству. Гарантированная цена, никаких скрытых доплат.' }] as step, i}
				<div
					class="group relative flex flex-col gap-6 border border-border-light bg-white p-8 shadow-card transition-all duration-500 hover:-translate-y-1 hover:shadow-elevated lg:p-10"
					class:opacity-0={!sections['how-section']}
					class:animate-fade-up={sections['how-section']}
					style="animation-delay: {0.2 + i * 0.15}s"
				>
					<!-- Step number -->
					<span
						class="text-6xl font-light text-border-medium lg:text-7xl"
						style="font-family: var(--font-heading);"
					>
						{step.num}
					</span>
					<div>
						<h3
							class="text-xl font-medium text-primary transition-colors duration-300 group-hover:text-secondary"
							style="font-family: var(--font-heading);"
						>
							{step.title}
						</h3>
						<p class="mt-3 text-sm leading-relaxed text-text-secondary">{step.text}</p>
					</div>
					<!-- Connector arrow (between cards) -->
					{#if i < 2}
						<div
							class="absolute top-1/2 -right-4 hidden -translate-y-1/2 text-border-medium md:block"
						>
							<svg
								class="h-6 w-6"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
								/>
							</svg>
						</div>
					{/if}
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-primary py-section-sm lg:py-section"
	id="promo-cta"
	data-animate
>
	<!-- Decorative Elements -->
	<div class="absolute top-0 left-0 h-32 w-32 border border-white/5 lg:h-64 lg:w-64"></div>
	<div class="absolute right-0 bottom-0 h-48 w-48 border border-white/5 lg:h-80 lg:w-80"></div>
	<!-- Gold accent line -->
	<div
		class="absolute top-0 right-0 left-0 h-px bg-gradient-to-r from-transparent via-accent/50 to-transparent"
	></div>

	<div class="relative mx-auto max-w-3xl px-6 text-center">
		<div class:opacity-0={!sections['promo-cta']} class:animate-fade-up={sections['promo-cta']}>
			<span class="text-[11px] tracking-[0.3em] text-accent uppercase">Не упустите момент</span>
			<h2
				class="mt-4 text-4xl font-light text-white lg:text-6xl"
				style="font-family: var(--font-heading);"
			>
				Запишитесь на
				<span class="text-accent-light">бесплатную</span>
				<br /> консультацию
			</h2>
			<p class="mx-auto mt-6 max-w-lg text-base leading-relaxed text-white/60">
				Наш дизайнер поможет выбрать подходящую акцию, разработает проект и рассчитает точную
				стоимость с учётом скидок.
			</p>
			<div class="mt-10 flex flex-wrap items-center justify-center gap-4">
				<a
					href="/showrooms"
					class="group inline-flex items-center gap-3 border border-accent bg-accent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
				>
					Записаться на консультацию
					<svg
						class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
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
				</a>
				<a
					href="tel:+375291234567"
					class="inline-flex items-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-white/50"
				>
					<svg
						class="h-4 w-4"
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
					Позвонить
				</a>
			</div>
		</div>
	</div>
</section>
