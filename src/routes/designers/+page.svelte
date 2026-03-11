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
			{ threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	const benefits = [
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M9 14.25l6-6m4.5-3.493V21.75l-3.75-1.5-3.75 1.5-3.75-1.5-3.75 1.5V4.757c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0c1.1.128 1.907 1.077 1.907 2.185z"/>`,
			title: 'Партнёрская скидка',
			text: 'До 5% дополнительная скидка на всю продукцию фабрики. Скидка применяется по дополнительному согласованию.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M2.25 7.125C2.25 6.504 2.754 6 3.375 6h6c.621 0 1.125.504 1.125 1.125v3.75c0 .621-.504 1.125-1.125 1.125h-6a1.125 1.125 0 01-1.125-1.125v-3.75zM14.25 8.625c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v8.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-8.25zM3.75 16.125c0-.621.504-1.125 1.125-1.125h5.25c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125h-5.25a1.125 1.125 0 01-1.125-1.125v-2.25z"/>`,
			title: 'Образцы и каталоги',
			text: 'Бесплатный набор образцов материалов и актуальных каталогов с доставкой на адрес студии или клиента.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"/>`,
			title: 'Персональный менеджер',
			text: 'Выделенный менеджер отвечает в течение 2 часов, берёт на себя расчёт смет и контроль сроков производства.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>`,
			title: 'Приоритет в производстве',
			text: 'Заказы партнёров-дизайнеров выполняются в приоритетной очереди. Срок производства — от 15 рабочих дней.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5m.75-9l3-3 2.148 2.148A12.061 12.061 0 0116.5 7.605"/>`,
			title: '3D-визуализация',
			text: 'Доступ к профессиональным 3D-моделям и текстурам всей продукции для рендера в вашем проекте.'
		},
		{
			icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5"/>`,
			title: 'Обучение и шоурум',
			text: 'Приглашаем на закрытые презентации новых коллекций и профессиональные экскурсии по производству.'
		}
	];

	const tracks = [
		{
			id: 'studio',
			label: 'Дизайн-студиям',
			title: 'Программа для студий',
			description:
				'Подходит для дизайн-бюро и архитектурных студий с регулярным потоком проектов. Предусматривает корпоративный договор, сводные счета и персональные условия сотрудничества.',
			points: [
				'Скидка от 15% до 22% в зависимости от объёма',
				'Сводные акты и единый счёт раз в месяц',
				'Единый менеджер для всей команды студии',
				'Доступ к закрытым коллекциям и предпродажам',
				'Кредитная линия до 30 дней для постоянных партнёров',
				'Совместное участие в выставках и мероприятиях'
			]
		},
		{
			id: 'freelance',
			label: 'Фрилансерам',
			title: 'Программа для независимых дизайнеров',
			description:
				'Идеально для частных дизайнеров интерьеров: гибкие условия без минимального объёма, быстрая регистрация через онлайн-заявку и поддержка на каждом этапе проекта.',
			points: [
				'Фиксированная скидка 12% с первого заказа',
				'Без минимального объёма и ежемесячных обязательств',
				'Персональный кабинет с историей заказов и КП',
				'Бесплатные образцы к каждому проекту',
				'Онлайн-конструктор с вашим логином',
				'Реферальный бонус: 3% от заказов привлечённых клиентов'
			]
		}
	];

	let activeTrack = $state('studio');

	const steps = [
		{
			num: '01',
			title: 'Заполните заявку',
			text: 'Оставьте контактные данные и расскажите о своей деятельности. Это займёт не более 3 минут.'
		},
		{
			num: '02',
			title: 'Согласование условий',
			text: 'Менеджер свяжется с вами в течение одного рабочего дня и подберёт оптимальную программу.'
		},
		{
			num: '03',
			title: 'Подписание договора',
			text: 'Оформляем партнёрский договор: для студий — очно или через ЭДО, для фрилансеров — онлайн.'
		},
		{
			num: '04',
			title: 'Начало работы',
			text: 'Получаете доступ к личному кабинету, образцам и персональному менеджеру — и можно начинать.'
		}
	];

	/** @type {string} */
	let formName = $state('');
	/** @type {string} */
	let formType = $state('studio');
	/** @type {string} */
	let formPhone = $state('');
	/** @type {string} */
	let formEmail = $state('');
	let formSent = $state(false);

	function handleSubmit(/** @type {SubmitEvent} */ e) {
		e.preventDefault();
		formSent = true;
	}
</script>

<svelte:head>
	<title>Дизайнерам — ЗОВ | Партнёрская программа для студий и фрилансеров</title>
	<meta
		name="description"
		content="Партнёрская программа ЗОВ для дизайнеров интерьеров и архитектурных студий: скидки до 22%, образцы, 3D-модели, персональный менеджер и приоритет в производстве."
	/>
</svelte:head>

<!-- ==================== HERO ==================== -->
<section class="relative overflow-hidden bg-primary py-28 lg:py-36" id="designers-hero">
	<!-- Geometric decorations -->
	<div
		class="absolute top-0 left-0 h-64 w-64 -translate-x-1/2 -translate-y-1/2 border border-white/5"
	></div>
	<div
		class="absolute right-0 bottom-0 h-96 w-96 translate-x-1/3 translate-y-1/3 border border-white/5"
	></div>
	<div class="absolute top-20 right-24 h-32 w-32 border border-white/5"></div>

	<!-- Accent line -->
	<div
		class="absolute top-0 left-0 h-1 w-full bg-gradient-to-r from-transparent via-secondary to-transparent opacity-40"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="max-w-2xl">
			<div class="opacity-0" class:animate-fade-up={heroVisible} style="animation-delay: 0.2s">
				<span
					class="inline-flex items-center gap-2 border border-white/10 bg-white/5 px-4 py-2 text-[11px] tracking-[0.3em] text-accent uppercase backdrop-blur-sm"
				>
					<span class="h-1.5 w-1.5 rounded-full bg-accent"></span>
					Партнёрская программа
				</span>
			</div>

			<h1
				class="mt-6 text-5xl leading-[1.1] font-light text-white opacity-0 md:text-6xl lg:text-7xl"
				style="font-family: var(--font-heading); animation-delay: 0.4s"
				class:animate-fade-up={heroVisible}
			>
				Для дизайнеров<br />
				<span class="text-accent-light">и студий</span>
			</h1>

			<p
				class="mt-7 max-w-lg text-base leading-relaxed text-white/60 opacity-0 md:text-lg"
				class:animate-fade-up={heroVisible}
				style="animation-delay: 0.6s"
			>
				Станьте партнёром фабрики ЗОВ — и предлагайте клиентам премиальную мебель с эксклюзивными
				условиями, профессиональной поддержкой и приоритетным исполнением заказов.
			</p>

			<div
				class="mt-10 flex flex-wrap items-center gap-4 opacity-0"
				class:animate-fade-up={heroVisible}
				style="animation-delay: 0.8s"
			>
				<a
					href="#application"
					class="group inline-flex items-center gap-3 border border-accent bg-accent px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
				>
					Стать партнёром
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
					href="#how-it-works"
					class="inline-flex items-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white/80 uppercase transition-all duration-500 hover:border-white/50 hover:text-white"
				>
					Как это работает
				</a>
			</div>
		</div>

		<!-- Stats row -->
		<div
			class="mt-20 grid grid-cols-2 gap-px border border-white/10 opacity-0 md:grid-cols-4"
			class:animate-fade-up={heroVisible}
			style="animation-delay: 1s"
		>
			{#each [{ value: '5%', label: 'дополнительная скидка' }, { value: '500+', label: 'дизайнеров-партнёров' }, { value: '2 ч', label: 'время ответа менеджера' }, { value: '30 дн', label: 'срок производства' }] as stat}
				<div class="flex flex-col gap-1.5 bg-white/5 px-6 py-5 backdrop-blur-sm">
					<span
						class="text-3xl font-light text-accent-light"
						style="font-family: var(--font-heading);">{stat.value}</span
					>
					<span class="text-xs tracking-wide text-white/40">{stat.label}</span>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== BENEFITS ==================== -->
<section class="py-20 lg:py-28" id="benefits-section" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header -->
		<div
			class="mb-14 opacity-0 transition-all duration-700"
			class:animate-fade-up={sections['benefits-section']}
		>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Что вы получаете</span>
			<h2
				class="mt-3 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Преимущества партнёрства
			</h2>
		</div>

		<!-- Grid -->
		<div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
			{#each benefits as b, i}
				<div
					class="group border border-border-light bg-white p-8 opacity-0 shadow-card transition-all duration-500 hover:-translate-y-1 hover:shadow-elevated"
					class:animate-fade-up={sections['benefits-section']}
					style="animation-delay: {0.1 + i * 0.08}s"
				>
					<div
						class="mb-5 flex h-10 w-10 items-center justify-center border border-secondary/20 text-secondary transition-colors duration-300 group-hover:border-secondary group-hover:bg-secondary group-hover:text-white"
					>
						<svg
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="1.5"
						>
							{@html b.icon}
						</svg>
					</div>
					<h3
						class="text-lg font-medium text-primary transition-colors duration-300 group-hover:text-secondary"
						style="font-family: var(--font-heading);"
					>
						{b.title}
					</h3>
					<p class="mt-3 text-sm leading-relaxed text-text-secondary">
						{b.text}
					</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== TRACKS ==================== -->
<section class="bg-surface-warm py-20 lg:py-28" id="tracks-section" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header -->
		<div
			class="mb-10 opacity-0 transition-all duration-700"
			class:animate-fade-up={sections['tracks-section']}
		>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Выберите формат</span>
			<h2
				class="mt-3 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Программы сотрудничества
			</h2>
		</div>

		<!-- Tab switcher -->
		<div
			class="mb-10 flex gap-2 border-b border-border-light opacity-0 transition-all duration-700"
			class:animate-fade-up={sections['tracks-section']}
			style="animation-delay: 0.15s"
		>
			{#each tracks as track}
				<button
					class="relative pb-4 text-sm tracking-wide transition-colors duration-300
						{activeTrack === track.id ? 'text-primary' : 'text-text-muted hover:text-text-secondary'}"
					onclick={() => (activeTrack = track.id)}
					id="tab-{track.id}"
				>
					{track.label}
					{#if activeTrack === track.id}
						<span class="absolute bottom-0 left-0 h-0.5 w-full bg-secondary"></span>
					{/if}
				</button>
			{/each}
		</div>

		<!-- Content -->
		{#each tracks as track}
			{#if activeTrack === track.id}
				<div class="grid gap-12 lg:grid-cols-2 lg:gap-20">
					<!-- Left: description -->
					<div
						class="opacity-0 transition-all duration-500"
						class:animate-fade-up={sections['tracks-section']}
						style="animation-delay: 0.25s"
					>
						<h3
							class="text-3xl font-light text-primary lg:text-4xl"
							style="font-family: var(--font-heading);"
						>
							{track.title}
						</h3>
						<p class="mt-5 text-base leading-relaxed text-text-secondary">
							{track.description}
						</p>
						<a
							href="#application"
							class="group mt-8 inline-flex items-center gap-3 border border-primary bg-primary px-7 py-3.5 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
						>
							Оставить заявку
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

					<!-- Right: points -->
					<div
						class="opacity-0 transition-all duration-500"
						class:animate-fade-up={sections['tracks-section']}
						style="animation-delay: 0.35s"
					>
						<ul class="divide-y divide-border-light">
							{#each track.points as point, j}
								<li class="flex items-start gap-4 py-4">
									<span class="mt-0.5 flex-shrink-0 text-xs font-medium text-accent tabular-nums"
										>0{j + 1}</span
									>
									<span class="text-sm leading-relaxed text-text-primary">{point}</span>
								</li>
							{/each}
						</ul>
					</div>
				</div>
			{/if}
		{/each}
	</div>
</section>

<!-- ==================== HOW IT WORKS ==================== -->
<section class="py-20 lg:py-28" id="how-it-works" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header -->
		<div
			class="mb-14 opacity-0 transition-all duration-700"
			class:animate-fade-up={sections['how-it-works']}
		>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Просто и быстро</span>
			<h2
				class="mt-3 text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Как стать партнёром
			</h2>
		</div>

		<div class="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
			{#each steps as step, i}
				<div
					class="opacity-0"
					class:animate-fade-up={sections['how-it-works']}
					style="animation-delay: {0.1 + i * 0.1}s"
				>
					<!-- Number line -->
					<div class="mb-6 flex items-center gap-3">
						<span
							class="text-5xl leading-none font-light text-border-medium"
							style="font-family: var(--font-heading);"
						>
							{step.num}
						</span>
						{#if i < steps.length - 1}
							<div class="hidden h-px flex-1 bg-border-light lg:block"></div>
						{/if}
					</div>
					<h3 class="text-lg font-medium text-primary" style="font-family: var(--font-heading);">
						{step.title}
					</h3>
					<p class="mt-3 text-sm leading-relaxed text-text-secondary">
						{step.text}
					</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== APPLICATION FORM ==================== -->
<section class="relative overflow-hidden bg-primary py-20 lg:py-28" id="application" data-animate>
	<!-- Decorations -->
	<div
		class="absolute top-0 left-0 h-64 w-64 -translate-x-1/2 -translate-y-1/2 border border-white/5"
	></div>
	<div
		class="absolute right-0 bottom-0 h-80 w-80 translate-x-1/3 translate-y-1/3 border border-white/5"
	></div>

	<div class="relative mx-auto max-w-7xl px-6">
		<div class="grid gap-16 lg:grid-cols-2 lg:gap-24">
			<!-- Left: text -->
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['application']}
			>
				<span class="text-[11px] tracking-[0.3em] text-accent uppercase">Начните сегодня</span>
				<h2
					class="mt-4 text-4xl font-light text-white lg:text-5xl"
					style="font-family: var(--font-heading);"
				>
					Оставьте заявку —<br />
					<span class="text-accent-light">мы позвоним первыми</span>
				</h2>
				<p class="mt-6 text-base leading-relaxed text-white/55">
					Расскажите о себе, и мы предложим наиболее подходящие условия сотрудничества. Никаких
					долгих согласований — первый заказ можно разместить уже в день подписания договора.
				</p>

				<div class="mt-10 space-y-4">
					{#each [{ icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/>`, label: '+375 (29) 123-45-67' }, { icon: `<path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/>`, label: 'design@zov.by' }] as contact}
						<div class="flex items-center gap-3">
							<div class="flex h-9 w-9 shrink-0 items-center justify-center border border-white/10">
								<svg
									class="h-4 w-4 text-accent"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
									stroke-width="1.5"
								>
									{@html contact.icon}
								</svg>
							</div>
							<span class="text-sm text-white/60">{contact.label}</span>
						</div>
					{/each}
				</div>
			</div>

			<!-- Right: form -->
			<div
				class="opacity-0 transition-all duration-700"
				class:animate-fade-up={sections['application']}
				style="animation-delay: 0.2s"
			>
				{#if formSent}
					<div class="flex h-full flex-col items-center justify-center py-12 text-center">
						<div
							class="flex h-16 w-16 items-center justify-center border border-accent/30 bg-accent/10"
						>
							<svg
								class="h-8 w-8 text-accent"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1.5"
							>
								<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
							</svg>
						</div>
						<h3
							class="mt-6 text-2xl font-light text-white"
							style="font-family: var(--font-heading);"
						>
							Заявка отправлена
						</h3>
						<p class="mt-3 max-w-xs text-sm text-white/50">
							Менеджер свяжется с вами в течение одного рабочего дня.
						</p>
					</div>
				{:else}
					<form
						onsubmit={handleSubmit}
						class="border border-white/10 bg-white/5 p-8 backdrop-blur-sm lg:p-10"
					>
						<h3
							class="mb-8 text-xl font-light text-white"
							style="font-family: var(--font-heading);"
						>
							Заявка на партнёрство
						</h3>

						<!-- Type -->
						<div class="mb-6">
							<p class="mb-3 text-[11px] tracking-[0.2em] text-white/40 uppercase">Я работаю как</p>
							<div class="flex gap-3">
								<label
									class="flex flex-1 cursor-pointer items-center gap-3 border px-4 py-3 transition-colors duration-300
									{formType === 'studio' ? 'border-accent bg-accent/10' : 'border-white/10 hover:border-white/25'}"
								>
									<input type="radio" bind:group={formType} value="studio" class="sr-only" />
									<span
										class="flex h-4 w-4 shrink-0 items-center justify-center border {formType ===
										'studio'
											? 'border-accent'
											: 'border-white/30'}"
									>
										{#if formType === 'studio'}
											<span class="h-2 w-2 bg-accent"></span>
										{/if}
									</span>
									<span class="text-sm text-white/80">Студия</span>
								</label>
								<label
									class="flex flex-1 cursor-pointer items-center gap-3 border px-4 py-3 transition-colors duration-300
									{formType === 'freelance' ? 'border-accent bg-accent/10' : 'border-white/10 hover:border-white/25'}"
								>
									<input type="radio" bind:group={formType} value="freelance" class="sr-only" />
									<span
										class="flex h-4 w-4 shrink-0 items-center justify-center border {formType ===
										'freelance'
											? 'border-accent'
											: 'border-white/30'}"
									>
										{#if formType === 'freelance'}
											<span class="h-2 w-2 bg-accent"></span>
										{/if}
									</span>
									<span class="text-sm text-white/80">Фрилансер</span>
								</label>
							</div>
						</div>

						<!-- Name -->
						<div class="mb-5">
							<label
								for="form-name"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
							>
								Имя и фамилия*
							</label>
							<input
								id="form-name"
								type="text"
								bind:value={formName}
								required
								placeholder="Анна Смирнова"
								class="w-full border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							/>
						</div>

						<!-- Phone -->
						<div class="mb-5">
							<label
								for="form-phone"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
							>
								Телефон*
							</label>
							<input
								id="form-phone"
								type="tel"
								bind:value={formPhone}
								required
								placeholder="+375 (29) 000-00-00"
								class="w-full border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							/>
						</div>

						<!-- Email -->
						<div class="mb-8">
							<label
								for="form-email"
								class="mb-2 block text-[11px] tracking-[0.2em] text-white/40 uppercase"
							>
								Email*
							</label>
							<input
								id="form-email"
								type="email"
								bind:value={formEmail}
								required
								placeholder="your@email.com"
								class="w-full border border-white/15 bg-transparent px-4 py-3 text-sm text-white placeholder-white/25 transition-colors duration-300 outline-none focus:border-accent/60"
							/>
						</div>

						<button
							type="submit"
							class="group flex w-full items-center justify-center gap-3 border border-accent bg-accent py-4 text-xs tracking-[0.2em] text-primary uppercase transition-all duration-500 hover:border-accent-light hover:bg-accent-light"
						>
							Отправить заявку
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
						</button>

						<p class="mt-4 text-center text-[11px] text-white/25">
							Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности
						</p>
					</form>
				{/if}
			</div>
		</div>
	</div>
</section>
