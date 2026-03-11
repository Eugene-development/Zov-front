<script>
	import { onMount } from 'svelte';

	let heroVisible = $state(false);
	let sections = $state({});

	onMount(() => {
		heroVisible = true;

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						sections[entry.target.id] = true;
					}
				});
			},
			{ threshold: 0.05, rootMargin: '0px 0px -40px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	/** @type {Array<{id: number, date: string, category: string, title: string, excerpt: string}>} */
	const news = [
		{
			id: 1,
			date: '5 марта 2026',
			category: 'Производство',
			title: 'Запуск новой линейки кухонных фасадов «Арктика»',
			excerpt:
				'Фабрика ЗОВ представляет коллекцию матовых фасадов в холодных оттенках — от жемчужно-белого до серо-стального. Новинка уже доступна к заказу во всех салонах.'
		},
		{
			id: 2,
			date: '27 февраля 2026',
			category: 'Компания',
			title: 'ЗОВ открыл 15-й салон в Москве',
			excerpt:
				'В торгово-выставочном центре «Мега Химки» открылось новое пространство ЗОВ площадью 450 м². Посетители могут оценить действующие кухни и гардеробные комплексы в реальных интерьерах.'
		},
		{
			id: 3,
			date: '18 февраля 2026',
			category: 'Технологии',
			title: 'Внедрение 3D-визуализации в онлайн-конструктор',
			excerpt:
				'Обновлённый конструктор кухни на сайте ЗОВ получил фотореалистичный рендер в реальном времени. Теперь клиенты могут видеть итоговый проект ещё до обращения к дизайнеру.'
		},
		{
			id: 4,
			date: '10 февраля 2026',
			category: 'Награды',
			title: 'ЗОВ — лауреат премии «Мебель года 2025» в номинации «Лучший производитель кухонь»',
			excerpt:
				'На ежегодном отраслевом форуме в Санкт-Петербурге фабрика ЗОВ получила главную награду по итогам независимого голосования среди 120 тысяч покупателей по всей России.'
		},
		{
			id: 5,
			date: '2 февраля 2026',
			category: 'Партнёрство',
			title: 'Соглашение о сотрудничестве с ведущими европейскими поставщиками фурнитуры',
			excerpt:
				'ЗОВ подписал долгосрочные контракты с Blum и Grass. Вся новая мебель премиального сегмента оснащается немецкими и австрийскими механизмами с расширенной гарантией 10 лет.'
		},
		{
			id: 6,
			date: '24 января 2026',
			category: 'Акции',
			title: 'Специальные условия для проектировщиков и дизайнеров интерьеров',
			excerpt:
				'Фабрика запустила профессиональную программу для дизайнеров: персональный менеджер, приоритетный доступ к образцам материалов, расширенная партнёрская скидка и отсрочка платежа.'
		},
		{
			id: 7,
			date: '15 января 2026',
			category: 'Производство',
			title: 'Расширение цеха покраски: +2 000 м² и новый парк оборудования',
			excerpt:
				'Завершилась реконструкция главного производственного корпуса в Барановичах. Проектная мощность окрасочного цеха увеличилась на 35%, что позволит сократить сроки исполнения заказов.'
		},
		{
			id: 8,
			date: '7 января 2026',
			category: 'Компания',
			title: 'Итоги 2025 года: рост выручки на 22% и выход на рынок Казахстана',
			excerpt:
				'Фабрика завершила год с рекордными показателями. Общий объём исполненных заказов превысил 38 000 кухонь. В декабре открылись первые три партнёрских салона в Алматы и Астане.'
		}
	];

	const categories = [
		'Все',
		'Производство',
		'Компания',
		'Технологии',
		'Награды',
		'Партнёрство',
		'Акции'
	];
	let activeCategory = $state('Все');

	let filteredNews = $derived(
		activeCategory === 'Все' ? news : news.filter((n) => n.category === activeCategory)
	);
</script>

<svelte:head>
	<title>Новости — ЗОВ | Мебельная фабрика</title>
	<meta
		name="description"
		content="Актуальные новости фабрики ЗОВ: открытие салонов, новые коллекции, технологические обновления и события компании."
	/>
</svelte:head>

<!-- ==================== HERO ==================== -->
<section class="relative overflow-hidden bg-surface-warm pt-20 pb-16 lg:pt-28 lg:pb-20">
	<!-- Subtle geometric accent -->
	<div
		class="absolute top-0 right-0 h-80 w-80 translate-x-1/3 -translate-y-1/3 border border-border-light opacity-40"
	></div>
	<div class="absolute bottom-0 left-16 h-40 w-40 border border-border-light opacity-20"></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="opacity-0" class:animate-fade-up={heroVisible} style="animation-delay: 0.2s">
			<span
				class="inline-flex items-center gap-2 text-[11px] tracking-[0.3em] text-secondary uppercase"
			>
				<span class="h-px w-6 bg-secondary"></span>
				Мебельная фабрика ЗОВ
			</span>
			<h1
				class="mt-4 text-5xl font-light text-primary lg:text-6xl"
				style="font-family: var(--font-heading);"
			>
				Новости
			</h1>
			<p class="mt-4 max-w-lg text-base leading-relaxed text-text-secondary">
				События, обновления и достижения фабрики ЗОВ
			</p>
		</div>
	</div>
</section>

<!-- ==================== FILTER ==================== -->
<div
	class="sticky top-[80px] z-20 border-b border-border-light bg-white/95 backdrop-blur-md"
	id="filter-bar"
	data-animate
>
	<div class="mx-auto max-w-7xl px-6">
		<div class="scrollbar-none flex items-center gap-1 overflow-x-auto py-4">
			{#each categories as cat}
				<button
					class="border px-4 py-1.5 text-xs tracking-wider whitespace-nowrap transition-all duration-300
						{activeCategory === cat
						? 'border-primary bg-primary text-white'
						: 'border-border-light bg-transparent text-text-secondary hover:border-secondary hover:text-secondary'}"
					onclick={() => (activeCategory = cat)}
					id="filter-{cat}"
				>
					{cat}
				</button>
			{/each}
		</div>
	</div>
</div>

<!-- ==================== NEWS LIST ==================== -->
<section class="py-16 lg:py-20" id="news-section" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<div class="divide-y divide-border-light">
			{#each filteredNews as item, i (item.id)}
				<article
					class="group flex flex-col gap-3 py-8 opacity-0 transition-all duration-500 hover:bg-surface-warm/40 md:flex-row md:items-start md:gap-10 lg:px-4"
					class:animate-fade-up={sections['news-section']}
					style="animation-delay: {0.05 + i * 0.07}s"
				>
					<!-- Date + Category -->
					<div
						class="flex shrink-0 flex-row items-center gap-3 md:w-44 md:flex-col md:items-start md:gap-1.5"
					>
						<time class="text-xs text-text-muted tabular-nums">{item.date}</time>
						<span
							class="inline-block border border-secondary/30 px-2 py-0.5 text-[10px] tracking-[0.2em] text-secondary uppercase"
						>
							{item.category}
						</span>
					</div>

					<!-- Content -->
					<div class="min-w-0 flex-1">
						<h2
							class="text-lg leading-snug font-normal text-primary transition-colors duration-300 group-hover:text-secondary md:text-xl"
							style="font-family: var(--font-heading);"
						>
							{item.title}
						</h2>
						<p class="mt-2.5 text-sm leading-relaxed text-text-secondary">
							{item.excerpt}
						</p>
					</div>

					<!-- Arrow -->
					<div class="hidden shrink-0 items-center self-center md:flex">
						<span
							class="flex h-9 w-9 items-center justify-center border border-transparent text-text-muted transition-all duration-300 group-hover:border-secondary group-hover:text-secondary"
						>
							<svg
								class="h-4 w-4 translate-x-0 transition-transform duration-300 group-hover:translate-x-0.5"
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
						</span>
					</div>
				</article>
			{/each}
		</div>

		{#if filteredNews.length === 0}
			<div class="py-24 text-center">
				<p class="text-base text-text-muted">Новостей в этой категории пока нет</p>
			</div>
		{/if}
	</div>
</section>

<!-- ==================== CTA ==================== -->
<section
	class="relative overflow-hidden border-t border-border-light bg-surface-warm py-16 lg:py-20"
	id="news-cta"
	data-animate
>
	<div
		class="absolute top-0 right-0 h-48 w-48 translate-x-1/3 -translate-y-1/3 border border-border-medium opacity-30"
	></div>

	<div class="relative mx-auto max-w-3xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['news-cta']}>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase"
				>Хотите узнавать первыми?</span
			>
			<h2
				class="mt-4 text-3xl font-light text-primary lg:text-4xl"
				style="font-family: var(--font-heading);"
			>
				Посетите наши салоны
			</h2>
			<p class="mx-auto mt-4 max-w-md text-sm leading-relaxed text-text-secondary">
				Наши дизайнеры всегда в курсе последних новинок и акций. Приходите — расскажем всё лично.
			</p>
			<div class="mt-8 flex flex-wrap items-center justify-center gap-4">
				<a
					href="/showrooms"
					class="group inline-flex items-center gap-3 border border-primary bg-primary px-8 py-3.5 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
				>
					Найти ближайший салон
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
					href="/promotions"
					class="inline-flex items-center gap-2 border border-border-medium px-8 py-3.5 text-xs tracking-[0.15em] text-text-primary uppercase transition-all duration-500 hover:border-secondary hover:text-secondary"
				>
					Смотреть акции
				</a>
			</div>
		</div>
	</div>
</section>
